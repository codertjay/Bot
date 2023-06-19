import os
import time
from __future__ import absolute_import
from Deadline.Events import DeadlineEventListener
from Deadline.Scripting import PathUtils, RepositoryUtils

def GetDeadlineEventListener():
    return MyDeadlineEventListener()

class MyDeadlineEventListener (DeadlineEventListener):
    def __init__(self):
        self.OnJobStartedCallback += self.OnJobStarted
        self.OnTaskCompletedCallback += self.OnTaskCompleted

    def OnJobStarted(self, job):
        if job.JobStatus == "Rendering":
            self.ScheduleTaskChecking(job)

    def OnTaskCompleted(self, task):
        job = RepositoryUtils.GetJob(task.JobId)
        if job.JobStatus == "Rendering" and task.TaskStatus == "Completed":
            self.ScheduleTaskChecking(job)

    def ScheduleTaskChecking(self, job):
        jobFramesFolder = job.JobOutputDirectories[0]  # Cartella dei frame renderati
        completedTasks = RepositoryUtils.GetJobTasks(job, True, "Completed")  # Elenco dei task completati
        averageTime = self.CalculateAverageTime(completedTasks)  # Calcolo del tempo medio dei task completati

        for task in completedTasks:
            if task.TaskOutputFileByteSize == 0:  # Verifica se la dimensione finale del task è pari a zero byte
                RepositoryUtils.RequeueTask(task)  # Rimanda in rendering il task

        if len(completedTasks) >= 5:  # Verifica se ci sono almeno cinque task completati
            renderingTasks = RepositoryUtils.GetJobTasks(job, True, "Rendering")  # Elenco dei task in rendering

            for task in renderingTasks:
                if self.IsTaskExceedingTimeLimit(task, averageTime):  # Verifica se il tempo di rendering supera il limite
                    task.TaskStatus = "Suspended"  # Sospende il task
                    RepositoryUtils.RequeueTask(task)  # Rimanda in rendering il task

        self.ScheduleCallback(30)  # Richiama la verifica ogni 30 secondi

    def CalculateAverageTime(self, tasks):
        totalSeconds = 0

        for task in tasks:
            taskSeconds = (task.TaskEndTime - task.TaskStartTime).TotalSeconds
            totalSeconds += taskSeconds

        return totalSeconds / len(tasks)

    def IsTaskExceedingTimeLimit(self, task, averageTime):
        taskSeconds = (DateTime.Now - task.TaskStartTime).TotalSeconds
        return taskSeconds > (averageTime * 4)

    def ScheduleCallback(self, interval):
        deadlinePlugin = GetDeadlinePlugin()
        deadlinePlugin.SetScriptCallbackDeadlineCommand(interval)