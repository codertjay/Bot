function _$(id) {
    return document.getElementById(id);
}

var alert_no_answer;
var _debug = false;
var _document_root = ("https:" == document.location.protocol ? "https://polldaddy.com/swf/" : "http://i0.poll.fm/swf/");
var sc, _container, _global_ec, _global_ss, _global_wn;
var FlashDetect = new
function () {
    var a = this;
    a.installed = false;
    a.raw = "";
    a.major = -1;
    a.minor = -1;
    a.revision = -1;
    a.revisionStr = "";
    var b = [{
        name: "ShockwaveFlash.ShockwaveFlash.7",
        version: function (h) {
            return d(h)
        }
    },
        {
            name: "ShockwaveFlash.ShockwaveFlash.6",
            version: function (k) {
                var h = "6,0,21";
                try {
                    k.AllowScriptAccess = "always";
                    h = d(k)
                } catch (j) {
                }
                return h
            }
        },
        {
            name: "ShockwaveFlash.ShockwaveFlash",
            version: function (h) {
                return d(h)
            }
        }];
    var d = function (k) {
        var h = -1;
        try {
            h = k.GetVariable("$version")
        } catch (j) {
        }
        return h
    };
    var g = function (h) {
        var k = -1;
        try {
            k = new ActiveXObject(h)
        } catch (j) {
            k = {
                activeXError: true
            }
        }
        return k
    };
    var c = function (j) {
        var h = j.split(",");
        return {
            raw: j,
            major: parseInt(h[0].split(" ")[1], 10),
            minor: parseInt(h[1], 10),
            revision: parseInt(h[2], 10),
            revisionStr: h[2]
        }
    };
    var f = function (l) {
        var j = l.split(/ +/);
        var k = j[2].split(/\./);
        var h = j[3];
        return {
            raw: l,
            major: parseInt(k[0], 10),
            minor: parseInt(k[1], 10),
            revisionStr: h,
            revision: e(h)
        }
    };
    var e = function (h) {
        return parseInt(h.replace(/[a-zA-Z]/g, ""), 10) || a.revision
    };
    a.majorAtLeast = function (h) {
        return a.major >= h
    };
    a.minorAtLeast = function (h) {
        return a.minor >= h
    };
    a.revisionAtLeast = function (h) {
        return a.revision >= h
    };
    a.versionAtLeast = function (j) {
        var k = [a.major, a.minor, a.revision];
        var h = Math.min(k.length, arguments.length);
        for (i = 0; i < h; i++) {
            if (k[i] >= arguments[i]) {
                if (i + 1 < h && k[i] == arguments[i]) {
                    continue
                } else {
                    return true
                }
            } else {
                return false
            }
        }
    };
    a.FlashDetect = function () {
        if (navigator.plugins && navigator.plugins.length > 0) {
            var l = "application/x-shockwave-flash";
            var k = navigator.mimeTypes;
            if (k && k[l] && k[l].enabledPlugin && k[l].enabledPlugin.description) {
                var h = k[l].enabledPlugin.description;
                var m = f(h);
                a.raw = m.raw;
                a.major = m.major;
                a.minor = m.minor;
                a.revisionStr = m.revisionStr;
                a.revision = m.revision;
                a.installed = true
            }
        } else {
            if (navigator.appVersion.indexOf("Mac") == -1 && window.execScript) {
                var h = -1;
                for (var j = 0; j < b.length && h == -1; j++) {
                    var n = g(b[j].name);
                    if (!n.activeXError) {
                        a.installed = true;
                        h = b[j].version(n);
                        if (h != -1) {
                            var m = c(h);
                            a.raw = m.raw;
                            a.major = m.major;
                            a.minor = m.minor;
                            a.revision = m.revision;
                            a.revisionStr = m.revisionStr
                        }
                    }
                }
            }
        }
    }()
};
FlashDetect.JS_RELEASE = "1.0.4";
var evercookie = (function () {
    this._class = function () {
        var self = this;
        this._ec = {};
        var no_color = -1;
        var _ec_tests = 10;
        this.get = function (name, cb, dont_reset) {
            self._evercookie(name, cb, undefined, undefined, dont_reset)
        };
        this.set = function (name, value) {
            self._evercookie(name, function () {
            }, value)
        };
        this._evercookie = function (name, cb, value, i, dont_reset) {
            if (typeof self._evercookie == "undefined") {
                self = this
            }
            if (typeof i == "undefined") {
                i = 0
            }
            if (i == 0) {
                self.evercookie_database_storage(name, value);
                self._ec.userData = self.evercookie_userdata(name, value);
                self._ec.cookieData = self.evercookie_cookie(name, value);
                self._ec.localData = self.evercookie_local_storage(name, value);
                self._ec.globalData = self.evercookie_global_storage(name, value);
                self._ec.sessionData = self.evercookie_session_storage(name, value)
            }
            if (typeof value == "undefined") {
                if (((window.openDatabase && typeof self._ec.dbData == "undefined")) && i++ < _ec_tests) {
                    setTimeout(self._evercookie, 300, name, cb, value, i, dont_reset)
                } else {
                    var tmpec = self._ec;
                    self._ec = {};
                    var candidates = new Array();
                    var bestnum = 0;
                    var candidate;
                    for (var item in tmpec) {
                        if (typeof tmpec[item] != "undefined" && typeof tmpec[item] != "null" && tmpec[item] != "null" && tmpec[item] != "undefined") {
                            candidates[tmpec[item]] = typeof candidates[tmpec[item]] == "undefined" ? 1 : candidates[tmpec[item]] + 1
                        }
                    }
                    for (var item in candidates) {
                        if (candidates[item] > bestnum) {
                            bestnum = candidates[item];
                            candidate = item
                        }
                    }
                    if (typeof dont_reset == "undefined" || dont_reset != 1) {
                        self.set(name, candidate)
                    }
                    if (typeof cb == "function") {
                        cb(candidate, tmpec)
                    }
                }
            }
        };
        this.evercookie_userdata = function (name, value) {
            try {
                var elm = this.createElem("div", "userdata_el", 1);
                elm.style.behavior = "url(#default#userData)";
                if (typeof (value) != "undefined") {
                    elm.setAttribute(name, value);
                    elm.save(name)
                } else {
                    elm.load(name);
                    return elm.getAttribute(name)
                }
            } catch (e) {
            }
        };
        this.evercookie_local_storage = function (name, value) {
            try {
                if (window.localStorage) {
                    if (typeof (value) != "undefined") {
                        localStorage.setItem(name, value)
                    } else {
                        return localStorage.getItem(name)
                    }
                }
            } catch (e) {
            }
        };
        this.evercookie_database_storage = function (name, value) {
            try {
                if (window.openDatabase) {
                    var database = window.openDatabase("sqlite_evercookie", "", "evercookie", 1024 * 1024);
                    if (typeof (value) != "undefined") {
                        database.transaction(function (tx) {
                            tx.executeSql("CREATE TABLE IF NOT EXISTS cache(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, value TEXT NOT NULL, UNIQUE (name))", [], function (tx, rs) {
                            }, function (tx, err) {
                            });
                            tx.executeSql("INSERT OR REPLACE INTO cache(name, value) VALUES(?, ?)", [name, value], function (tx, rs) {
                            }, function (tx, err) {
                            })
                        })
                    } else {
                        database.transaction(function (tx) {
                            tx.executeSql("SELECT value FROM cache WHERE name=?", [name], function (tx, result1) {
                                if (result1.rows.length >= 1) {
                                    self._ec.dbData = result1.rows.item(0)["value"]
                                } else {
                                    self._ec.dbData = ""
                                }
                            }, function (tx, err) {
                            })
                        })
                    }
                }
            } catch (e) {
            }
        };
        this.evercookie_session_storage = function (name, value) {
            try {
                if (window.sessionStorage) {
                    if (typeof (value) != "undefined") {
                        sessionStorage.setItem(name, value)
                    } else {
                        return sessionStorage.getItem(name)
                    }
                }
            } catch (e) {
            }
        };
        this.evercookie_global_storage = function (name, value) {
            if (window.globalStorage) {
                var host = this.getHost();
                try {
                    if (typeof (value) != "undefined") {
                        eval("globalStorage[host]." + name + " = value")
                    } else {
                        return eval("globalStorage[host]." + name)
                    }
                } catch (e) {
                }
            }
        };
        this.evercookie_cookie = function (name, value, expire) {
            var cookie = this.getFromStr(name, document.cookie);
            if (typeof (value) != "undefined" && typeof (cookie) == "undefined") {
                var today = new Date();
                today.setTime(today.getTime());
                if (typeof expire == undefined || expire == null) {
                    expire = (60 * 60 * 24 * 365 * 20 * 1000)
                }
                var expires_date = new Date((today.getTime() + expire));
                document.cookie = name + "=" + value + "; expires=" + expires_date.toGMTString() + "; path=/"
            } else {
                return cookie
            }
        };
        this.createElem = function (type, name, append) {
            var el;
            if (typeof name != "undefined" && document.getElementById(name)) {
                el = document.getElementById(name)
            } else {
                el = document.createElement(type)
            }
            el.style.visibility = "hidden";
            el.style.position = "absolute";
            if (name) {
                el.setAttribute("id", name)
            }
            if (append) {
                if (_container) {
                    _container.appendChild(el)
                } else {
                    document.body.appendChild(el)
                }
            }
            return el
        };
        this.getFromStr = function (name, text) {
            if (typeof text != "string") {
                return
            }
            var nameEQ = name + "=";
            var ca = text.split(/[;&]/);
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) == " ") {
                    c = c.substring(1, c.length)
                }
                if (c.indexOf(nameEQ) == 0) {
                    return c.substring(nameEQ.length, c.length)
                }
            }
        };
        this.getHost = function () {
            var domain = document.location.host;
            if (domain.indexOf("www.") == 0) {
                domain = domain.replace("www.", "")
            }
            return domain
        }
    };
    return _class
})();
var swfstore = (function () {
    var b = 0;
    var a = /[^a-z0-9_]/ig;

    function c(d) {
        if (typeof d == "function") {
            throw "SwfStore Error: Functions cannot be used as keys or values."
        }
    }

    SwfStore = function (g) {
        this.config = g || {
            namespace: "swfstore",
            swf_url: _document_root + "storage.swf",
            onready: function () {
            },
            onerror: function () {
            },
            debug: _debug,
            timeout: 10
        };
        var j = this.namespace = this.config.namespace.replace(a, "_"),
            e = this.config.debug,
            m = this.config.timeout;

        function f() {
            return "SwfStore_" + j + "_" + (b++)
        }

        function d(q) {
            var o = f();
            p = document.getElementById(o);
            if (typeof p == "undefined" || p == null) {
                var p = document.createElement("div");
                if (typeof _container !== "undefined" || _container !== null) {
                    _container.appendChild(p)
                } else {
                    document.body.appendChild(p)
                }
                p.id = o;
                p.style.position = "absolute";
                p.style.top = "0px";
                p.style.left = "-2000px"
            }
            return p
        }

        if (e) {
            if (typeof console == "undefined") {
                var k = d();
                window.console = {
                    log: function (p) {
                        var o = d();
                        o.innerHTML = p;
                        k.appendChild(o)
                    }
                }
            }
            this.log = function (o, p, q) {
                p = (p == "swfStore") ? "swf" : p;
                log("SwfStore - " + j + ": " + o + " (" + p + "): " + q)
            }
        } else {
            this.log = function () {
            }
        }
        this.log("info", "js", "Initializing...");
        SwfStore[j] = this;
        var n = d(e);
        var l = f();
        var h = "logfn=SwfStore." + j + ".log&amp;onload=SwfStore." + j + ".onload&amp;onerror=SwfStore." + j + ".onerror";
        n.innerHTML = '<object height="1" width="1" codebase="https://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab" id="' + l + '" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000">	<param value="' + this.config.swf_url + '" name="movie">	<param value="' + h + '" name="FlashVars">	<param value="always" name="allowScriptAccess">	<embed height="1" align="middle" width="1" pluginspage="https://www.macromedia.com/go/getflashplayer" flashvars="' + h + '" type="application/x-shockwave-flash" allowscriptaccess="always" quality="high" loop="false" play="true" name="' + l + '" bgcolor="#ffffff" src="' + this.config.swf_url + '"></object>';
        this.swf = document[l] || window[l];
        this._timeout = setTimeout(function () {
            if (typeof SwfStore !== "undefined" && typeof SwfStore[j] !== "undefined") {
                SwfStore[j].log("Timeout reached, assuming the store.swf failed to load and firing the onerror callback.");
                if (typeof SwfStore[j].config.onerror !== "undefined") {
                    SwfStore[j].config.onerror()
                }
            }
        }, m * 1000)
    };
    SwfStore.prototype = {
        ready: false,
        namespace: "SwfStore_prototype",
        set: function (d, e) {
            if (this.namespace === SwfStore.prototype.namespace) {
                throw "Create a new SwfStore to set data"
            }
            if (this.ready) {
                c(d);
                c(e);
                this.swf.set(d, e)
            } else {
                throw "Attempted to save to uninitialized SwfStore."
            }
        },
        get: function (d) {
            if (this.namespace === SwfStore.prototype.namespace) {
                throw "Create a new SwfStore to set data"
            }
            if (this.ready) {
                c(d);
                return this.swf.get(d)
            } else {
                throw "Attempted to read from an uninitialized SwfStore."
            }
        },
        getAll: function (d) {
            if (this.namespace === SwfStore.prototype.namespace) {
                throw "Create a new SwfStore to set data"
            }
            if (this.ready) {
                c(d);
                return this.swf.get(d)
            } else {
                throw "Attempted to read from an uninitialized SwfStore."
            }
        },
        onload: function () {
            clearTimeout(this._timeout);
            this.ready = true;
            if (this.config.onready) {
                this.config.onready()
            }
        },
        onerror: function () {
            clearTimeout(this._timeout);
            if (this.config.onerror) {
                this.config.onerror()
            }
        }
    };
    return SwfStore
}());
sessvars = function () {
    var x = {};
    x.$ = {
        prefs: {
            memLimit: 2000,
            autoFlush: true,
            crossDomain: true,
            includeProtos: false,
            includeFunctions: false
        },
        parent: x,
        clearMem: function () {
            for (var i in this.parent) {
                if (i != "$") {
                    this.parent[i] = undefined
                }
            }
            this.flush()
        },
        usedMem: function () {
            x = {};
            return Math.round(this.flush(x) / 1024)
        },
        usedMemPercent: function () {
            return Math.round(this.usedMem() / this.prefs.memLimit)
        },
        flush: function (x) {
            var y, o = {},
                j = this.$$;
            x = x || top;
            for (var i in this.parent) {
                o[i] = this.parent[i]
            }
            o.$ = this.prefs;
            j.includeProtos = this.prefs.includeProtos;
            j.includeFunctions = this.prefs.includeFunctions;
            y = this.$$.make(o);
            if (x != top) {
                return y.length
            }
            if (y.length / 1024 > this.prefs.memLimit) {
                return false
            }
            x.name = y;
            return true
        },
        getDomain: function () {
            var l = location.href;
            l = l.split("///").join("//");
            l = l.substring(l.indexOf("://") + 3).split("/")[0];
            while (l.split(".").length > 2) {
                l = l.substring(l.indexOf(".") + 1)
            }
            return l
        },
        debug: function (t) {
            var t = t || this,
                a = arguments.callee;
            if (!document.body) {
                setTimeout(function () {
                    a(t)
                }, 200);
                return
            }
            t.flush();
            var d = document.getElementById("sessvarsDebugDiv");
            if (!d) {
                d = document.createElement("div");
                document.body.insertBefore(d, document.body.firstChild)
            }
            d.id = "sessvarsDebugDiv";
            d.innerHTML = '<div style="line-height:20px;padding:5px;font-size:11px;font-family:Verdana,Arial,Helvetica;z-index:10000;background:#FFFFCC;border: 1px solid #333;margin-bottom:12px"><b style="font-family:Trebuchet MS;font-size:20px">sessvars.js - debug info:</b><br/><br/>Memory usage: ' + t.usedMem() + " Kb (" + t.usedMemPercent() + '%)&nbsp;&nbsp;&nbsp;<span style="cursor:pointer"><b>[Clear memory]</b></span><br/>' + top.name.split("\n").join("<br/>") + "</div>";
            d.getElementsByTagName("span")[0].onclick = function () {
                t.clearMem();
                location.reload()
            }
        },
        init: function () {
            var o = {},
                t = this;
            try {
                o = this.$$.toObject(top.name)
            } catch (e) {
                o = {}
            }
            this.prefs = o.$ || t.prefs;
            if (this.prefs.crossDomain || this.prefs.currentDomain == this.getDomain()) {
                for (var i in o) {
                    this.parent[i] = o[i]
                }
            } else {
                this.prefs.currentDomain = this.getDomain()
            }
            this.parent.$ = t;
            t.flush();
            var f = function () {
                if (t.prefs.autoFlush) {
                    t.flush()
                }
            };
            if (window.addEventListener) {
                addEventListener("unload", f, false)
            } else {
                if (window.attachEvent) {
                    window.attachEvent("onunload", f)
                } else {
                    this.prefs.autoFlush = false
                }
            }
        }
    };
    x.$.$$ = {
        compactOutput: false,
        includeProtos: false,
        includeFunctions: false,
        detectCirculars: true,
        restoreCirculars: true,
        make: function (arg, restore) {
            this.restore = restore;
            this.mem = [];
            this.pathMem = [];
            return this.toJsonStringArray(arg).join("")
        },
        toObject: function (x) {
            if (!this.cleaner) {
                try {
                    this.cleaner = new RegExp('^("(\\\\.|[^"\\\\\\n\\r])*?"|[,:{}\\[\\]0-9.\\-+Eaeflnr-u \\n\\r\\t])+?$')
                } catch (a) {
                    this.cleaner = /^(true|false|null|\[.*\]|\{.*\}|".*"|\d+|\d+\.\d+)$/
                }
            }
            if (!this.cleaner.test(x)) {
                return {}
            }
            eval("this.myObj=" + x);
            if (!this.restoreCirculars || !alert) {
                return this.myObj
            }
            if (this.includeFunctions) {
                var x = this.myObj;
                for (var i in x) {
                    if (typeof x[i] == "string" && !x[i].indexOf("JSONincludedFunc:")) {
                        x[i] = x[i].substring(17);
                        eval("x[i]=" + x[i])
                    }
                }
            }
            this.restoreCode = [];
            this.make(this.myObj, true);
            var r = this.restoreCode.join(";") + ";";
            eval('r=r.replace(/\\W([0-9]{1,})(\\W)/g,"[$1]$2").replace(/\\.\\;/g,";")');
            eval(r);
            return this.myObj
        },
        toJsonStringArray: function (arg, out) {
            if (!out) {
                this.path = []
            }
            out = out || [];
            var u;
            switch (typeof arg) {
                case "object":
                    this.lastObj = arg;
                    if (this.detectCirculars) {
                        var m = this.mem;
                        var n = this.pathMem;
                        for (var i = 0; i < m.length; i++) {
                            if (arg === m[i]) {
                                out.push('"JSONcircRef:' + n[i] + '"');
                                return out
                            }
                        }
                        m.push(arg);
                        n.push(this.path.join("."))
                    }
                    if (arg) {
                        if (arg.constructor == Array) {
                            out.push("[");
                            for (var i = 0; i < arg.length; ++i) {
                                this.path.push(i);
                                if (i > 0) {
                                    out.push(",\n")
                                }
                                this.toJsonStringArray(arg[i], out);
                                this.path.pop()
                            }
                            out.push("]");
                            return out
                        } else {
                            if (typeof arg.toString != "undefined") {
                                out.push("{");
                                var first = true;
                                for (var i in arg) {
                                    if (!this.includeProtos && arg[i] === arg.constructor.prototype[i]) {
                                        continue
                                    }
                                    this.path.push(i);
                                    var curr = out.length;
                                    if (!first) {
                                        out.push(this.compactOutput ? "," : ",\n")
                                    }
                                    this.toJsonStringArray(i, out);
                                    out.push(":");
                                    this.toJsonStringArray(arg[i], out);
                                    if (out[out.length - 1] == u) {
                                        out.splice(curr, out.length - curr)
                                    } else {
                                        first = false
                                    }
                                    this.path.pop()
                                }
                                out.push("}");
                                return out
                            }
                        }
                        return out
                    }
                    out.push("null");
                    return out;
                case "unknown":
                case "undefined":
                case "function":
                    if (!this.includeFunctions) {
                        out.push(u);
                        return out
                    }
                    arg = "JSONincludedFunc:" + arg;
                    out.push('"');
                    var a = ["\n", "\\n", "\r", "\\r", '"', '\\"'];
                    arg += "";
                    for (var i = 0; i < 6; i += 2) {
                        arg = arg.split(a[i]).join(a[i + 1])
                    }
                    out.push(arg);
                    out.push('"');
                    return out;
                case "string":
                    if (this.restore && arg.indexOf("JSONcircRef:") == 0) {
                        this.restoreCode.push("this.myObj." + this.path.join(".") + "=" + arg.split("JSONcircRef:").join("this.myObj."))
                    }
                    out.push('"');
                    var a = ["\n", "\\n", "\r", "\\r", '"', '\\"'];
                    arg += "";
                    for (var i = 0; i < 6; i += 2) {
                        arg = arg.split(a[i]).join(a[i + 1])
                    }
                    out.push(arg);
                    out.push('"');
                    return out;
                default:
                    out.push(String(arg));
                    return out
            }
        }
    };
    x.$.init();
    return x
}();
var supercookie = (function () {
    this._class = function () {
        if (_$("PD_superContainer") == null) {
            document.write('<div id="PD_superContainer"></div>')
        }
        _container = _$("PD_superContainer");
        _global_ec = new evercookie();
        log("Flash version:: " + FlashDetect.raw);
        if (FlashDetect.versionAtLeast(9, 0, 31)) {
            _global_ss = new swfstore()
        }
        this.showCookies = function (a, c) {
            for (var b in c) {
                log("Storage mechanism " + b + " returned: " + c[b])
            }
        };
        this.isEnabled = function () {
            var a = "pd-test-cookie";
            var b;
            _global_ec.evercookie_cookie(a, "true", (1000 * 5));
            b = _global_ec.getFromStr(a, document.cookie);
            log("Cookies are enabled: " + b);
            return b == "true"
        };
        this.set = function (a, b) {
            _global_ec.set(a, b);
            if (_global_ss && _global_ss.ready) {
                _global_ss.set(a, b)
            }
            sessvars[a] = b;
            sessvars.$.flush()
        };
        this.get = function (b) {
            var d, a, c;
            if (_debug) {
                _global_ec.get(b, this.showCookies, 1)
            }
            _global_ec.get(b, function (e) {
                d = e
            }, 1);
            log("Super Get- cookie_value::" + d);
            if (_global_ss && _global_ss.ready) {
                a = _global_ss.get(b)
            }
            log("Super Get- lso_value::" + a);
            c = sessvars[b];
            log("Super Get- wn_value::" + c);
            return d || a || c
        }
    };
    return this._class
})();

function countchars(elm) {
    if (elm.value.length > 4000) {
        elm.value = left(elm.value, 4000);
    }
    _$('charcount').innerHTML = elm.value.length;
}

function setCookie(name, e) {
    var path = '/';
    var domain = '';
    var secure = '';
    var expires = 0;
    if (typeof (e) !== 'undefined') {
        expires = parseInt(e);
    }
    if (expires > 0) {
        expires = expires * 1000;
    } else {
        expires = 60 * 60 * 24 * 30 * 1000;
    }
    var today = new Date();
    today.setTime(today.getTime());

    expires = today.getTime() + (expires);
    var expires_date = new Date(expires);

    log('Cookie Name: ' + name);

    if (typeof sc !== 'undefined') {
        log('SET supercookie');
        sc.set(name, escape(expires));
    } else {
        log('SET standard cookie');
        document.cookie = name + "=" + escape(today.getTime()) +
            ((expires) ? ";expires=" + expires_date.toGMTString() : "") +
            ((path) ? ";path=" + path : "") +
            ((domain) ? ";domain=" + domain : "") +
            ((secure) ? ";secure" : "");
    }
}

function getCookie(name, expires) {
    var a_temp_cookie = '';
    var cookie_name = '';
    var cookie_value = '';
    expires = (typeof expires === "undefined") ? 3600000 : expires;

    log('Cookie Name: ' + name);

    if (typeof sc != 'undefined') {
        log('GET supercookie');
        cookie_value = sc.get(name);
    } else {
        log('GET standard cookie');
        var a_all_cookies = document.cookie.split(';');

        for (i = 0; i < a_all_cookies.length; i++) {
            a_temp_cookie = a_all_cookies[i].split('=');
            cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');
            if (cookie_name == name) {
                if (a_temp_cookie.length > 1)
                    cookie_value = unescape(a_temp_cookie[1].replace(/^\s+|\s+$/g, ''));
                break;
            }
            a_temp_cookie = null;
            cookie_name = '';
        }
    }

    log('Cookie Value: ' + cookie_value);

    if (cookie_value == 'true') {
        return cookie_value;
    } else {
        var today = new Date();
        cookie_value = parseInt(cookie_value);
        log('Time: ' + today.getTime());
        // if cookie value is greater than current time then it's an old cookie ( time + expiry ) and should be replaced with creation time.
        if (cookie_value > today.getTime()) {
            var diff = cookie_value - today.getTime();
            if (expires >= diff) {
                var new_time = today.getTime() - (expires - diff);
            } else {
                var new_time = today.getTime();
            }
            setCookie(name, new_time);
        }

        if (cookie_value + expires > today.getTime())
            return 'true';
    }
    return null;
}

function vote(ev) {
    ev.preventDefault();

    var data = jQuery('.vote-button').data('vote');

    log(data);

    var answerString = '';
    var otherText = '';

    var ck = 'PDjs_poll_' + data.id + (data.v > 0 ? '_' + data.v : '');

    log(ck);

    for (i = 0; i < document.formPoll.elements.length; i++) {
        if (document.formPoll.elements[i].type == "checkbox" || document.formPoll.elements[i].type == "radio") {
            if (document.formPoll.elements[i].checked) {
                answerString += document.formPoll.elements[i].value + ',';
            }
        }
    }
    if (document.formPoll.pz !== undefined)
        var pz = document.formPoll.pz.value;
    else
        var pz = 1;

    if (parseInt(data.o) == 1) {
        otherText = _$('PDI_OtherText').value;
    }

    if (typeof document.formPoll.tags != 'undefined')
        tags = '&tags=' + urlEncode(document.formPoll.tags.value);
    else
        tags = '';

    if (answerString.length > 0 || otherText.length > 0) {
        var vote_root = '/vote.php';
        if (window.is_poll_fm) {
            vote_root = '/vote'
        }
        var url = vote_root + '?va=' + data.at + tags + '&pt=' + data.m + '&r=' + data.b + '&p=' + data.id + '&a=' + urlEncode(answerString) + '&o=' + urlEncode(otherText) + '&t=' + data.t + '&token=' + data.n + '&pz=' + pz;
        if (data.b > 0) {
            if (getCookie(ck, data.e) == 'true') {
                if (window.is_poll_fm) {
                    url = "/" + data.id + "/results?msg=revoted"
                } else {
                    url = "/poll/" + data.id + "/?view=results&msg=revoted"
                }
            } else {
                setCookie(ck, data.e);
            }
        }
        location.href = url;
    } else {
        alert(alert_no_answer);
    }
}

function urlEncode(a) {
    return encodeURIComponent(a).replace(/\%20/g, "+").replace(/!/g, "%21").replace(/'/g, "%27").replace(/\(/g, "%28").replace(/\)/g, "%29").replace(/\*/g, "%2A").replace(/\~/g, "%7E")
}

function log(m) {
    if (typeof (_debug) !== 'undefined' && _debug)
        if (typeof (console) !== 'undefined' && console != null)
            console.log(m);
}

function answer_click(type, input) {
    var number_already_checked = 0;

    jQuery('input[name=PDI_answer]').each(function () {
        var item = jQuery(this);
        if (input.attr('id') != item.attr('id') && item.is(':checked'))
            number_already_checked++;
    });

    var other_text = '';
    if (jQuery('input[name=PDI_OtherText]').length) {
        other_text = jQuery('input[name=PDI_OtherText]').val();
        if (other_text && other_text.length > 0)
            number_already_checked++;
    }

    if (input.is(':checked'))
        number_already_checked++;

    if (number_already_checked >= type) {
        jQuery('input[name=PDI_answer]').each(function () {
            var item = jQuery(this);
            if (input.attr('id') != item.attr('id') && !item.is(':checked'))
                item.attr('disabled', 'true');
        });
        if (jQuery('input[name=PDI_OtherText]')) {
            var item = jQuery('input[name=PDI_OtherText]');
            if (input.attr('id') != item.attr('id') && item.val() == '')
                item.attr('disabled', 'true');
        }
    } else {
        jQuery('input[name=PDI_answer]').each(function () {
            var item = $(this);
            if (!item.is(':checked'))
                item.removeAttr('disabled');
        });
        if (jQuery('input[name=PDI_OtherText]'))
            jQuery('input[name=PDI_OtherText]').removeAttr('disabled');
    }
}
