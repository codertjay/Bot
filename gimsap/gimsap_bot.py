import json

collection = [
    {
        'id': 0,
        'link': 'https://gimsap.ca/collections/all/products/nora-jollof-rice',
        'name': '(Nora) Jollof Rice',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.75',
        'description': '<p>Some spice to add flavor to your Jollof rice which is a west African favorite always consisting of rice, a tomato stew and seasoning.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/nora-joolof-rice-spice_300x300.jpg?v=1650568470'
    },
    {
        'id': 1,
        'link': 'https://gimsap.ca/collections/all/products/nora-spice-for-fried-rice-25g',
        'name': '(Nora) Spice for Fried Rice 25g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.75',
        'description': 'Some spice to help bring flavor to fried rice which is rice mixed with a combination of carrots, corn and other vegetables.&nbsp;\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a6f200c0-0a7a-48a8-8371-4ee9616acd36_300x300.jpg?v=1645134573'
    },
    {
        'id': 2,
        'link': 'https://gimsap.ca/collections/all/products/3-horses-malt-bottle-24',
        'name': '3 Horses Malt Bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.50',
        'description': '<p>3 Horses&nbsp;dark malt beverage in glass bottles.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/3-horses_Bottle_Single_300x300.jpg?v=1644954940'
    },
    {
        'id': 3,
        'link': 'https://gimsap.ca/collections/all/products/3-horses-malt-24-can',
        'name': '3 Horses Malt Can',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $36.00',
        'description': '<p>3 Horses dark malt beverage</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/3-horses_can_Single_300x300.jpg?v=1644954416'
    },
    {
        'id': 4,
        'link': 'https://gimsap.ca/collections/all/products/abacha-1lb',
        'name': 'Abacha',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>African Salad. Abacha is a Nigerian staple dish made from dried and fermented cassava (gari) flour. The cassava is pounded into a paste and boiled in water, then eaten with soup or stew. Abacha is a good source of carbohydrates, protein, and fiber. It also contains some vitamin C. Abacha is a Nigerian staple dish made from dried and fermented cassava (gari) flour. The cassava is pounded into a paste and boiled in water, then eaten with soup or stew. Abacha is a good source of carbohydrates, protein, and fiber. It also contains some vitamin C.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_300x300.jpg?v=1644954747'
    },
    {
        'id': 5,
        'link': 'https://gimsap.ca/collections/all/products/aboniki-balm-25g',
        'name': 'Aboniki Balm 25g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Aboniki Balm 25g</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/AbonikiBalm_300x300.jpg?v=1644968589'
    },
    {
        'id': 6,
        'link': 'https://gimsap.ca/collections/all/products/accra-kenkey-white-corn-meal-10kg',
        'name': 'Accra Kenkey White Corn Meal 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $33.50',
        'description': '<div id="dsc-copy-section" class="dsc-preview-success">\n<p>Accra Kenkey White Corn Meal is a gluten-free cornmeal that is popular in West Africa. It is made from white corn and is an excellent source of fiber, iron, and protein. Accra Kenkey White Corn Meal is a gluten-free cornmeal that is popular in West Africa. It is made from white corn and is an excellent source of fiber, iron, and protein. This grain is easy to cook and is used in many different recipes. It can be used to make savory dishes like Akwadu, fufu, and porridge.</p>\n</div>\n<div class="dsc-success-btns"><br></div>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_09d969ab-6389-4e81-be31-b6d1008ca0e4_300x300.jpg?v=1646860846'
    },
    {
        'id': 7,
        'link': 'https://gimsap.ca/collections/all/products/accra-kenkey-white-corn-meal-2-5kg',
        'name': 'Accra Kenkey White Corn Meal 2.5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>Accra Kenkey White Corn Meal is a gluten-free cornmeal that is popular in West Africa. It is made from white corn and is an excellent source of fiber, iron, and protein. Accra Kenkey White Corn Meal is a gluten-free cornmeal that is popular in West Africa. It is made from white corn and is an excellent source of fiber, iron, and protein. This grain is easy to cook and is used in many different recipes. It can be used to make savory dishes like Akwadu, fufu, and porridge.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_f402c6ab-a27e-44c1-904f-a80d422de629_300x300.jpg?v=1646860678'
    },
    {
        'id': 8,
        'link': 'https://gimsap.ca/collections/all/products/ackees-540ml',
        'name': 'Ackees 540mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p><meta charset="utf-8"><span>This is a light, refreshing, and flavourful&nbsp;juice made from ackees. Ackees are a Caribbean fruit that is a little smaller than a lime and has a sweet, citrusy flavour. Ackees are harvested from their tree, left to ripen, and then picked and squeezed to extract the juice. This juice is light, refreshing, and slightly sweet.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f387ba28-9182-4f84-81b7-105711d3f991_300x300.jpg?v=1646857776'
    },
    {
        'id': 9,
        'link': 'https://gimsap.ca/collections/all/products/adm-wheatlets-semolina-20kg',
        'name': 'ADM (wheatlets) semolina 20kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $24.99',
        'description': '<p>ADM&nbsp;(wheatlets) semolina 20kg This is a bag of wheatlets semolina. This product is the perfect addition to your morning cereal or oatmeal. Wheatlets are a high-quality, non-GMO product. It is a good source of protein and fiber. This product can be used in baking and in other dishes.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-16at12.19.19PM_300x300.png?v=1647454830'
    },
    {
        'id': 10,
        'link': 'https://gimsap.ca/collections/all/products/adm-semolina-10lbs',
        'name': 'adm semolina 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.00',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue" style="color: #000000; font-family: \'Helvetica Neue\'; font-size: small;">adm (wheatlets) semolina 20kg.\n  This is a bag of wheatlets semolina. This product is the perfect addition to your morning cereal or oatmeal. Wheatlets are a high-quality, non-GMO product. It is a good source of protein and fiber. This product can be used in baking and in other dishes.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1ebedcea-a4de-49b5-94c8-48dd867e4a0a_300x300.jpg?v=1646861201'
    },
    {
        'id': 11,
        'link': 'https://gimsap.ca/collections/all/products/adm-semolina-6lb',
        'name': 'adm semolina 6lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue" style="color: #000000; font-family: \'Helvetica Neue\'; font-size: small;">adm (wheatlets) semolina 20kg.\n  This is a bag of wheatlets semolina. This product is the perfect addition to your morning cereal or oatmeal. Wheatlets are a high-quality, non-GMO product. It is a good source of protein and fiber. This product can be used in baking and in other dishes.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/5605_300x300.jpg?v=1646861859'
    },
    {
        'id': 12,
        'link': 'https://gimsap.ca/collections/all/products/adobe-all-purpose-seasoning-with-pepper-794g',
        'name': 'Adobe all purpose seasoning (with Pepper) 794g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>Adobe All Purpose Seasoning is a blend of the most popular herbs and spices. With a hint of pepper, this product is perfect for adding flavor to any dish. Adobe All Purpose Seasoning is an all-natural blend of herbs and spices, which can be used in anything from soups to desserts. </p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_a9136f87-2917-4f88-8c74-cc8dc52a7c9a_300x300.jpg?v=1644957917'
    },
    {
        'id': 13,
        'link': 'https://gimsap.ca/collections/all/products/adobo-all-purpose-seasoning-280g',
        'name': 'Adobo All Purpose Seasoning 280g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The Adobo All Purpose Seasoning is a mix of a variety of herbs and spices, including garlic, onion, bay leaves, cumin, salt, pepper, and paprika. These ingredients are mixed together to create a versatile and convenient seasoning that can be used on everything from rice to tacos. This seasoning is the perfect way to add flavor to any dish and is the perfect way to make any meal more flavorful.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ed2c7569-c5d3-4fea-a07a-3d8f8616b265_300x300.jpg?v=1646857781'
    },
    {
        'id': 14,
        'link': 'https://gimsap.ca/collections/all/products/africas-best-texture-shear-butter-curl',
        'name': "Africa's Best Texture Shear Butter Curl",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': "<p>Africa's Best Texture Shear Butter Curl is a hair product designed to hydrate, soften, and provide definition to curls. It can be used on damp or dry hair and leaves curls with a natural sheen. It is designed to provide superior curl definition and hydration without the use of harsh chemicals.&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1b574685-471a-4662-8097-96410ed97592_300x300.jpg?v=1646857793'
    },
    {
        'id': 15,
        'link': 'https://gimsap.ca/collections/all/products/africas-besttextures-shear-butter',
        'name': "Africa's Best Textures Shear Butter (15 oz)",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': "<p>Africa's Best Texture Shear Butter Curl is a hair product designed to hydrate, soften, and provide definition to curls. It can be used on damp or dry hair and leaves curls with a natural sheen. It is designed to provide superior curl definition and hydration without the use of harsh chemicals.&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/d1b66f92f34c4cf525afff57eb157af6_300x300.jpg?v=1644957912'
    },
    {
        'id': 16,
        'link': 'https://gimsap.ca/collections/all/products/african-choice-palm-soup-400g',
        'name': 'African Choice Palm Soup 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue">African Choice Palm Soup is a vegetable soup that is cooked with palm oil, tomatoes, onions, and peppers. It is a vegan and gluten-free soup that is both healthy and tasty. It is low in fat and cholesterol and has no added sugar. The soup can be served hot or cold. It can be eaten as a meal or as a side dish. It is perfect for the vegetarian or vegan diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/2023953_300x300.jpg?v=1650550712'
    },
    {
        'id': 17,
        'link': 'https://gimsap.ca/collections/all/products/african-choice-palm-soup-400g-palmnut-cream',
        'name': 'African Choice Palm Soup 400g palmnut cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue">African Choice Palm Soup is a vegetable soup that is cooked with palm oil, tomatoes, onions, and peppers. It is a vegan and gluten-free soup that is both healthy and tasty. It is low in fat and cholesterol and has no added sugar. The soup can be served hot or cold. It can be eaten as a meal or as a side dish. It is perfect for the vegetarian or vegan diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/2023953_b4701778-bb6b-40d8-84be-168edffb72c4_300x300.jpg?v=1650550900'
    },
    {
        'id': 18,
        'link': 'https://gimsap.ca/collections/all/products/african-choice-palm-soup-800g',
        'name': 'African Choice Palm Soup 800g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue">African Choice Palm Soup is a vegetable soup that is cooked with palm oil, tomatoes, onions, and peppers. It is a vegan and gluten-free soup that is both healthy and tasty. It is low in fat and cholesterol and has no added sugar. The soup can be served hot or cold. It can be eaten as a meal or as a side dish. It is perfect for the vegetarian or vegan diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/2023953_c197888c-40b6-480d-b3e1-7afa16ef824c_300x300.jpg?v=1650550917'
    },
    {
        'id': 19,
        'link': 'https://gimsap.ca/collections/all/products/african-choice-palm-soup-800g-palmnut-cream-conc',
        'name': 'African Choice Palm Soup 800g palmnut cream conc.',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue">African Choice Palm Soup is a vegetable soup that is cooked with palm oil, tomatoes, onions, and peppers. It is a vegan and gluten-free soup that is both healthy and tasty. It is low in fat and cholesterol and has no added sugar. The soup can be served hot or cold. It can be eaten as a meal or as a side dish. It is perfect for the vegetarian or vegan diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/2023953_7b4efc8c-a38f-4ecc-b9cb-b02252726a83_300x300.jpg?v=1650550930'
    },
    {
        'id': 20,
        'link': 'https://gimsap.ca/collections/all/products/african-essence-904g',
        'name': 'African Essence 904g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': "<p>It is made from all natural ingredients and is handmade in Africa. The mixture is made with shea butter, olive oil, coconut oil, palm oil, and aloe vera. It doesn't flake and allows you to style your hair while staying in place.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_300x300.jpg?v=1650569526'
    },
    {
        'id': 21,
        'link': 'https://gimsap.ca/collections/all/products/african-essence-weave-spray-12oz',
        'name': 'African Essence Weave Spray (12oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>African Essence Weave Spray is a lightweight leave-in spray that is made for natural hair, which is created to promote growth and to protect the hair. This product is made with all natural ingredients, which include shea butter, mango butter, grapeseed oil, and olive oil. The African Essence Weave Spray will moisturize the hair and scalp, while adding shine and strength to the hair. It is designed to be used on wet or dry hair, which will make it easier to use. African Essence Weave Spray will give you the protection you need while you are out in the sun or water.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/african-essence-6-in-1-weave-spray-12-oz-6_300x300.png?v=1644957923'
    },
    {
        'id': 22,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-braid-spray-extra-shine-12oz',
        'name': 'African Pride Braid Spray Extra Shine (12oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.50',
        'description': '<p>African Pride Braid Spray Extra Shine (12oz) is a leave-in conditioner that gives your hair that extra shine that you need. This product is a no-tears, easy-to-use spray that moisturizes and protects your hair while giving it that extra shine. African Pride Braid Spray Extra Shine (12oz) is made with all natural ingredients and is not tested on animals. This product will leave your hair feeling soft and looking beautiful.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/924e0f6e-709b-4ce8-ac3e-8133fd0d1724_1.62c8e6d292460fa33ed5ec14f343609f_300x300.jpg?v=1644957926'
    },
    {
        'id': 23,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-moist-miracle-honey-coconut-shampoo-12oz',
        'name': 'African Pride Moist Miracle Honey &amp; Coconut Shampoo (12oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>African Pride Moist Miracle Honey is a deep conditioning treatment that has been specially formulated to repair dry, damaged hair. The product contains a rich blend of oils and vitamins that penetrate the hair shaft to nourish the hair and restore its natural moisture. The treatment also contains honey to provide hydration and shea butter to provide shine. The product leaves hair feeling smooth and healthy.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/african-pride-moisture-miracle-honey-coconut-oil-shampoo-384-ml_300x300.jpg?v=1644957932'
    },
    {
        'id': 24,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-moisture-miracle-curl-defining-gel-18oz',
        'name': 'African Pride Moisture Miracle Curl Defining Gel (18oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': "<p>This curl defining gel from African Pride is a salon quality product that will give your curls the definition they need. It's formulated with shea butter, mango butter, and avocado oil to nourish and hydrate your curls. The gel has a refreshing, tropical scent that leaves your hair smelling clean and smelling good. The formula is light and not sticky, so it won't weigh your hair down.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_4f8620cb-9a57-4bc5-bf9a-06c2526e35ae_300x300.jpg?v=1644957929'
    },
    {
        'id': 25,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-no-lye-relaxer-reguler',
        'name': 'African Pride No Lye Relaxer Regular',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p>African Pride No Lye Relaxer Regular is a professional relaxer that has been specifically designed for use in African-American hair. This product can be used for both men and women and is free of lye. It is a popular choice for those who are looking for a long-lasting solution to hair breakage. This product will leave your hair soft and manageable.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cdbbf717-8b9a-47b2-9991-a3824c3c9dfc_300x300.jpg?v=1646857788'
    },
    {
        'id': 26,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-no-lye-relaxer-super',
        'name': 'African Pride No Lye Relaxer Super',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p>African Pride No Lye Relaxer Super is a hair relaxer that comes in a 16 oz. container. It is designed to be used by African-Americans to keep their hair soft and manageable. This product contains no lye, which is an ingredient that is used in most other relaxers. African Pride No Lye Relaxer Super has been used by generations of black people and has been proven to be effective.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_58f1cf67-0da3-4f34-8139-1c7cf5867d8d_300x300.jpg?v=1646857787'
    },
    {
        'id': 27,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle',
        'name': 'African Pride Olive Miracle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>A few drops of this all-natural serum, which is free of parabens, sulfates, and other harmful chemicals, will make your hair softer, shinier, and more manageable. With a rich, emollient formula that absorbs quickly into the hair, it will make your hair easier to style. Plus, it smells divine!&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8b6ad0d6-f573-4445-84c8-191ad4cdbed0_300x300.jpg?v=1646857800'
    },
    {
        'id': 28,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle-creme-anti-breakage-6oz',
        'name': 'African Pride Olive Miracle Creme Anti-Breakage (6oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>African Pride Olive Miracle Creme Anti-Breakage is a cream that will give your hair a sleek, shiny finish. This hair cream is made with natural ingredients and is designed to repair damage and make your hair feel healthier. It is also a great product for people who are looking for a way to make their hair healthier and shinier. This hair cream is made with natural ingredients, so it will be good for your hair and will not cause any allergic reactions.&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/3d5b7127-d391-4094-b967-8199ef1d5c18.879195ce4904b532aaf66c3707f08cbd_300x300.jpg?v=1644957934'
    },
    {
        'id': 29,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle-growth-oil-max-8oz',
        'name': 'African Pride Olive Miracle Growth Oil Max (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>African Pride Olive Miracle Growth Oil Max is a natural hair oil that promotes hair growth and can be used on all hair types. The product is a 100% natural blend of olive oil, olive fruit extract, olive leaf extract, and olive leaf oil. The product contains no additives or fillers. The blend of ingredients includes both vitamin E and Omega-3 fatty acids. The oil can be used on all hair types and is safe for all hair types, including color-treated hair.&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_6fa862fd-c042-47dd-b344-b7ff8885cce7_300x300.jpg?v=1644957935'
    },
    {
        'id': 30,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle-growth-sheen-spray-8oz',
        'name': 'African Pride Olive Miracle Growth Sheen Spray (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p><meta charset="utf-8"><span data-mce-fragment="1">African Pride Braid Sheen Spray instantly nourishes hair and scalp adding moisture, softness and natural shine to your braids. Use daily for stronger, healthier, shinier hair and scalp. </span></p>\n<ul>\n<li>\n<span data-mce-fragment="1">Soothes braid tightness and soreness.</span><span data-mce-fragment="1"></span>\n</li>\n<li><span data-mce-fragment="1">Softens, adds extra shine, moisturizes &amp; conditions </span></li>\n<li><span data-mce-fragment="1">Excellent for locks and twists</span></li>\n</ul>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/AP_BraidSpray_Olive__02570.1465504321_300x300.jpg?v=1644957937'
    },
    {
        'id': 31,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle-no-lyerelaxer-regular-8touch',
        'name': 'African Pride Olive Miracle No-Lye Relaxer Regular [8Touch]',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p><span color="#000000" size="2" face="Helvetica Neue" style="color: #000000; font-family: \'Helvetica Neue\'; font-size: small;">A revolutionary new relaxer that combines natural ingredients with African botanicals to deliver a no-lye, no-ammonia, no-peroxide, no-keratin, no-mineral oil, no-phenylenediamine, no-coconut oil, no-paraben, no-SLS and no-gluten solution. The olive oil in this product helps the hair retain moisture and shine. The African botanicals work to protect the hair from harsh chemicals and give it a healthy and vibrant look. The result is a hair that is strong, healthy, and full of life.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/c59e35870dab6b506e90029b961bc2db_300x300.jpg?v=1644957938'
    },
    {
        'id': 32,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-olive-miracle-relaxer-4-touch-up',
        'name': 'African Pride Olive Miracle Relaxer 4 Touch Up',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p>&nbsp;</p>\n<p><span color="#000000" size="2" face="Helvetica Neue">A revolutionary new relaxer that combines natural ingredients with African botanicals to deliver a no-lye, no-ammonia, no-peroxide, no-keratin, no-mineral oil, no-phenylenediamine, no-coconut oil, no-paraben, no-SLS and no-gluten solution. The olive oil in this product helps the hair retain moisture and shine. The African botanicals work to protect the hair from harsh chemicals and give it a healthy and vibrant look. The result is a hair that is strong, healthy, and full of life.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7d4ef50f-d3f3-4afa-809b-c2f01dd65d34_300x300.jpg?v=1646857791'
    },
    {
        'id': 33,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-sb-miracle-bouncy-curls-pudding-15oz',
        'name': 'African Pride SB Miracle Bouncy Curls Pudding (15oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>African Pride SB Miracle Bouncy Curls Pudding is a hair product that helps to give the user bouncy curls. The product is also a deep conditioner, which helps to repair and hydrate the hair. </p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/s-l640_300x300.jpg?v=1644957940'
    },
    {
        'id': 34,
        'link': 'https://gimsap.ca/collections/all/products/african-pride-sb-miracle-leave-in-conditioner-15oz',
        'name': 'African Pride SB Miracle Leave In Conditioner (15oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>African Pride SB Miracle Leave In Conditioner is a nourishing, conditioning product that is formulated to help moisturize, soften, and detangle your hair. It is also enriched with Shea Butter and Coconut Oil to help strengthen and restore the hair. This product can be used on wet or dry hair.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/c19f6a3f56b88532706eb675bd7ebdbb_300x300.jpg?v=1644957941'
    },
    {
        'id': 35,
        'link': 'https://gimsap.ca/collections/all/products/african-royale-super-gro-regular-6oz',
        'name': 'African Royale Super Gro Regular (6oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>African Royale Super Gro Regular is an African hair product that contains a blend of 14 oils and gelatin rich oils. This product prevents damage and breakage and is great for all types of hair.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_300x300.jpg?v=1644958125'
    },
    {
        'id': 36,
        'link': 'https://gimsap.ca/collections/all/products/africans-best-carrot-tea-tree-oil-therapy',
        'name': "African's Best carrot Tea Tree Oil Therapy",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': "<p>The African's Best carrot Tea Tree Oil Therapy is a scalp and hair conditioning treatment that will make your hair feel soft and smell fresh. The treatment contains tea tree oil, carrot oil, and other ingredients that will help to maintain healthy hair. It is safe for all hair types and does not contain any harmful chemicals.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_322698dc-79ca-4d34-b9b4-43f50de5b177_300x300.jpg?v=1646857792'
    },
    {
        'id': 37,
        'link': 'https://gimsap.ca/collections/all/products/africans-best-relaxer-2complete-kit-reguler',
        'name': "African's Best Relaxer 2 Complete Kit Regular",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p>Formulated with the age old properties of Extra Virgin Olive Oil, our Olive Oil Coniditoning Relaxer System helps repair, rebuild, and restore you hair, while giving it added strength, shine, and softness. Go beyond relaxing by reaching a higher level of conditioning and moisturization to experience the ultimate in healthier, softer, silkier, straighter hair. Designed for normal hair textures.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d220aba7-6e04-4218-863c-3e68437a69de_300x300.jpg?v=1646857790'
    },
    {
        'id': 38,
        'link': 'https://gimsap.ca/collections/all/products/africans-best-relaxer-2-value-pack-super',
        'name': "African's Best Relaxer 2 Value Pack Super",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': "<p>The African's Best Relaxer Complete Kit Regular is a full set of a conditioning treatment and a relaxer. The kit is designed to be used for women with medium to coarse hair that is natural or chemically treated.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_fa9a0fe6-1bf6-44a2-95d8-c2c4acbd256b_300x300.jpg?v=1650573514'
    },
    {
        'id': 39,
        'link': 'https://gimsap.ca/collections/all/products/agbo-jedijeji',
        'name': 'Agbo Jedijeji',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Can be made from multiple ingredients but is commonly gotten from scented leaves, bitter leaf, sorghum leaves and garlic. It is very popular in West Africa as a herbal medication.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/agbo-jedi-for-weight-loss_300x300.jpg?v=1646866758'
    },
    {
        'id': 40,
        'link': 'https://gimsap.ca/collections/all/products/akabanga-chilli-oil',
        'name': 'Akabanga Chilli Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>For those who love a little spice in their life, Akabanga Chilli Oil is the perfect product. Akabanga Chilli Oil is made from a blend of African bird's eye and Scotch bonnet chillies, with a slight hint of garlic. Akabanga Chilli Oil can be used in a variety of dishes, including salsas, dips, dressings, and soups.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Akabanga-chili-oil-100-ml_300x300.png?v=1644957916'
    },
    {
        'id': 41,
        'link': 'https://gimsap.ca/collections/all/products/akanwu-edible-potash-150g',
        'name': 'Akanwu (Edible Potash) 150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Akanwu is a natural African staple product. It is a type of lake salt commonly used to cook with different types of beans. It is also great for ewedu and okro soup to increase the greenness and texture of the vegetables.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1f1b7393-8413-49a0-998d-f481405d1ee6_300x300.jpg?v=1646857806'
    },
    {
        'id': 42,
        'link': 'https://gimsap.ca/collections/all/products/akpi',
        'name': 'Akpi',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': 'Food spice used to make body cream. It is&nbsp;rich in protein, oil and potassium and can make your skin smoother, silkier and firmer.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Akpi_300x300.jpg?v=1646868206'
    },
    {
        'id': 43,
        'link': 'https://gimsap.ca/collections/all/products/alabukun-10x10',
        'name': 'Alabukun (10 doses)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p><meta charset="utf-8"><span>Alabukun Powder is good for treatment, control, prevention, &amp; health improvement.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c256d854-95ad-4f3b-83e8-b5fd1224ed5b_300x300.jpg?v=1646857805'
    },
    {
        'id': 44,
        'link': 'https://gimsap.ca/collections/all/products/aligator-pepper',
        'name': 'Aligator Pepper',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Aligator peppers are one of the hottest peppers in the world. It is a habanero pepper that is so hot that it\'s name literally means "Alligator Pepper." It is also called "Carolina Reaper" or "Hottest Pepper in the World." It is rated at 1,569,300 Scoville Units, which is 10 times hotter than a jalapeno.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ca67b229-03e5-44f0-a304-e77bb7181bca_300x300.jpg?v=1646857804'
    },
    {
        'id': 45,
        'link': 'https://gimsap.ca/collections/all/products/alikay-naturals-essential-17-hair-growth-oil-8oz',
        'name': 'Alikay Naturals Essential 17 Hair Growth Oil (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $26.99',
        'description': '<p>The Alikay Naturals Essential 17 Hair Growth Oil is a nutrient-rich, deep conditioning oil made with natural ingredients. It is designed to penetrate the hair shaft and to provide nourishment and protection. It is perfect for use after shampooing and conditioning, before heat styling, or to seal in moisture.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_85a1f346-de24-4622-81f8-f55c256a75ac_300x300.jpg?v=1650574950'
    },
    {
        'id': 46,
        'link': 'https://gimsap.ca/collections/all/products/alikay-naturals-lemongrass-slay-lay-edge-gel-4oz',
        'name': 'Alikay Naturals Lemongrass Slay &amp; Lay Edge Gel (4oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': "<p>Alikay Naturals Lemongrass Slay is a light, refreshing, and all-natural spray designed to be used before and after a shave. The Lemongrass Slay's gentle formula contains organic ingredients such as Aloe Vera, Coconut Oil, and Lemon Extract, which will leave your skin feeling soft and refreshed.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/08d72f5b-80db-4601-a620-b3009ba8d2b6.0125f113e84b1dae2d943d9a8ea1bf5e_300x300.jpg?v=1645040586'
    },
    {
        'id': 47,
        'link': 'https://gimsap.ca/collections/all/products/alikay-naturals-totally-twisted-loc-butter-8oz',
        'name': 'Alikay Naturals Totally Twisted Loc Butter (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.99',
        'description': '<p>Specially formulated for natural hair, Alikay Naturals Totally Twisted Loc Butter moisturizes, conditions, and detangles hair. Made with the finest ingredients, this product is the perfect solution for hair that needs moisture and shine.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/071a4fe7-7a17-46fa-9373-3f7b81428711_1.4cb9e3c371d3f3373fe1b06cd4fc2450_300x300.jpg?v=1645040588'
    },
    {
        'id': 48,
        'link': 'https://gimsap.ca/collections/all/products/all-purpose-seasoning',
        'name': 'all purpose seasoning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>This all-purpose seasoning is perfect for any meal. It is made with salt, garlic, onion, sugar, and other spices to provide a burst of flavor to any dish. This seasoning can be used in a variety of dishes including pasta, salads, and soup. The originality of this all-purpose seasoning is what makes it so great.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ccba2fd1-a79d-4548-84ae-0c5752934f9b_300x300.jpg?v=1646857523'
    },
    {
        'id': 49,
        'link': 'https://gimsap.ca/collections/all/products/all-purpose-seeasonning-goya-with-cumin-730g',
        'name': 'All Purpose Seasonning (Goya) With Cumin  730g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>Goya All Purpose Seasoning is a blend of ground spices, garlic, onion, salt, and oregano. It can be used in any dish, including rice, pasta, soup, and sauces.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/b5027600-970f-4294-b577-1bd6f8f1686a.dcc01b292dbe0fcf1a78cf33d35d0ded_300x300.jpg?v=1645040570'
    },
    {
        'id': 50,
        'link': 'https://gimsap.ca/collections/all/products/all-purpose-soul-seasoning',
        'name': 'all purpose soul seasoning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>The true flavor of soul food has never been more accessible than with the All Purpose Soul Seasoning. The authentic blend of herbs and spices in this jar will transform any dish into a tasty, home-cooked meal. You can use it to season meats, fish, vegetables, rice, beans, and more. This seasoning is a must-have for any kitchen, and will make your dishes taste as if they were prepared by your grandmother.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6ed8e4a0-e7a4-464c-8f0b-5da165b95c26_300x300.jpg?v=1646857524'
    },
    {
        'id': 51,
        'link': 'https://gimsap.ca/collections/all/products/all-spice-ground',
        'name': 'all spice ground',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>If you love to cook, then you know that there are some spices that are indispensable in the kitchen. There are a lot of different types of spices, but one of the most popular is allspice. Allspice is a spice that is made from the dried berries of the Pimenta dioica plant. The spice has a warm, sweet taste that goes well with many dishes. The allspice berries can be used whole or ground.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_78cb1082-8cc7-4a6f-b347-11edb006107a_300x300.jpg?v=1646857525'
    },
    {
        'id': 52,
        'link': 'https://gimsap.ca/collections/all/products/alligator-pepper-2',
        'name': 'Alligator Pepper (2)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>Our Alligator&nbsp;is a pepper that is yellow in color and has a similar taste to the Jalapeno. This pepper is typically harvested in its green stage and is best used when pickled. Alligator Peppers are not hot and have a flavor that is citrusy and earthy.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_035c2f72-aea3-4999-a7ae-55bd4877e1dd_300x300.jpg?v=1646857553'
    },
    {
        'id': 53,
        'link': 'https://gimsap.ca/collections/all/products/alligator-pepper-box-of-50-pcs',
        'name': 'Alligator Pepper (Box of 50 pcs)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Alligator Pepper is a great way to spice up any dish. It has a rating of up to 2,500,000 Scoville Units. This pepper is perfect for those who enjoy spicy food.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_61ce89ff-a028-47f6-adb7-d04e7289e690_300x300.jpg?v=1646869072'
    },
    {
        'id': 54,
        'link': 'https://gimsap.ca/collections/all/products/almond-whole-lb',
        'name': 'Almond whole /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p>Almonds are a tasty, healthy snack that you can enjoy on the go. These almonds are raw and roasted in a salt and sugar blend, which gives them a sweet, salty taste. The almonds are crunchy and delicious, and they can be enjoyed as a snack or used in recipes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6f3c3800-d9ef-4d8c-9de4-f625ffd07e62_300x300.jpg?v=1646857550'
    },
    {
        'id': 55,
        'link': 'https://gimsap.ca/collections/all/products/almond-whole-10-kg',
        'name': 'Almond whole 10 Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $185.00',
        'description': '<p>Delicious and healthy almonds are a great way to satisfy your sweet tooth. They are a good source of protein, and can be used in a variety of dishes. These almonds are whole, which means they have not been peeled or chopped. Almonds are perfect for snacking, cooking, or baking.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dc5f3adf-dac5-40b7-a0b3-f2393dbbf4de_300x300.jpg?v=1646857549'
    },
    {
        'id': 56,
        'link': 'https://gimsap.ca/collections/all/products/alum',
        'name': 'Alum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Alum is a white powder made from the mineral potassium aluminum sulfate. It is a popular additive to cooking and baking. It is used as a leavening agent in breads, cakes, and other baked goods. It is also used to clarify wine and beer.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_94d3f66a-556d-4a62-bcf0-57e6b5df6035_300x300.jpg?v=1646857539'
    },
    {
        'id': 57,
        'link': 'https://gimsap.ca/collections/all/products/aluminium-moinmoin-plate-one-dozen',
        'name': 'Aluminium Moinmoin Plate (one dozen)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>There is nothing better than sitting down to a nice meal with family and friends. Moinmoin is a popular Nigerian&nbsp;dish and is often served on a clay plate. With this set of 12 aluminium plates, you can now enjoy this dish with your loved ones on a more modern, yet still culturally significant, plate.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7cbaf4b2-af09-47de-8bd3-89b5235bd0f2_300x300.jpg?v=1646857546'
    },
    {
        'id': 58,
        'link': 'https://gimsap.ca/collections/all/products/aluminium-moinmoin-plate-one-dozen-small',
        'name': 'Aluminium Moinmoin Plate (one dozen) Small',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p>There is nothing better than sitting down to a nice meal with family and friends. Moinmoin is a popular Nigerian&nbsp;dish and is often served on a clay plate. With this set of 12 aluminium plates, you can now enjoy this dish with your loved ones on a more modern, yet still culturally significant, plate.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c330596a-c67c-4241-b1c5-f1f94ad94deb_300x300.jpg?v=1646857564'
    },
    {
        'id': 59,
        'link': 'https://gimsap.ca/collections/all/products/always-super-gro',
        'name': 'Always Super Gro',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.99',
        'description': '<p>A blend of vitamin E, rosemary and jojoba which moisturizes and makes your hair soft, shiny and healthy looking.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_6541a48b-1810-4951-8547-7d237086876e_300x300.jpg?v=1645040564'
    },
    {
        'id': 60,
        'link': 'https://gimsap.ca/collections/all/products/amala-scoop-colourful',
        'name': 'Amala Scoop Colourful',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This cleverly designed, two-in-one product will save you time and space in your kitchen. The Amala Scoop Colourful is a lightweight, yet durable, silicon spatula that will not scratch non-stick surfaces. It is dishwasher safe and heat resistant up to 500 degrees Fahrenheit. It is also safe to use on all types of food, including eggs, dairy, meat, and vegetables. This convenient product is perfect for stirring, scraping, and flipping without the need for a traditional spatula.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-16at12.52.54PM_300x300.png?v=1647456805'
    },
    {
        'id': 61,
        'link': 'https://gimsap.ca/collections/all/products/amala-scoop-purple',
        'name': 'Amala Scoop Purple',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Amala&nbsp;Scooper&nbsp;is a hand-held, oval shaped device that is used for serving.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/20220309_165527_300x300.jpg?v=1646871446'
    },
    {
        'id': 62,
        'link': 'https://gimsap.ca/collections/all/products/amazing-day-cerelac',
        'name': 'Amazing Day Cerelac',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>A healthy and nutritious breakfast for children and adults alike, Cerelac is a family favorite for breakfast. Available in various flavors, Cerelac is the perfect way to start the day with a delicious meal. This cereal is fortified with vitamins and minerals, and is made with healthy grains like oats, wheat, and rice.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_d7e1842f-e9de-4b9b-961a-a0e1699b822d_300x300.jpg?v=1645040582'
    },
    {
        'id': 63,
        'link': 'https://gimsap.ca/collections/all/products/amazing-grace-chin-chin',
        'name': 'Amazing Grace Chin Chin',
        'price': 'From $7.99',
        'description': '',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-29_300x300.jpg?v=1606149786'
    },
    {
        'id': 64,
        'link': 'https://gimsap.ca/collections/all/products/ambi-black-soap-3-5oz',
        'name': 'Ambi Black Soap (3.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Ambi Black Soap is an all-natural, deep cleansing facial soap. The soap is handmade in Ghana, Africa and is made from plantain skins, palm oil, shea butter, and cocoa pods. It is formulated to exfoliate, hydrate, and protect the skin. Ambi Black Soap leaves the skin feeling clean and soft. It has a pleasant, mild fragrance.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_9eee7fb3-c8bf-472b-851c-8d3aeb7c6d61_300x300.jpg?v=1645040590'
    },
    {
        'id': 65,
        'link': 'https://gimsap.ca/collections/all/products/ambi-cocoa-butter-cleansing-bar-3-5oz',
        'name': 'Ambi Cocoa Butter Cleansing Bar (3.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Warm, soothing cocoa butter and soothing, healing almond oil gently cleanse away dirt and make-up, leaving skin clean and soft. The cleansing bar is ideal for dry, sensitive skin and can be used to remove stubborn eye make-up. An ultra-rich, ultra-gentle, triple-milled soap bar, Ambi Cocoa Butter Cleansing Bar is a favorite among women with dry, sensitive skin. Soothing cocoa butter and soothing, healing almond oil gently cleanse away dirt and make-up, leaving skin clean and soft.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/9e2fbe43-3ea1-44b6-ab90-0d2817ed4a79_3.a610f757434dc7fff5c4b0ddc0590b89_300x300.jpg?v=1645040593'
    },
    {
        'id': 66,
        'link': 'https://gimsap.ca/collections/all/products/ambi-complexion-cleansing-bar-3-5oz',
        'name': 'Ambi Complexion Cleansing Bar (3.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>The Ambi Complexion Cleansing Bar is a soap-free, non-comedogenic cleansing bar. This product is specially formulated to cleanse the skin without stripping the skin of its natural oils. The bar is made with natural ingredients and essential oils. It is recommended for normal to oily skin types. The Ambi Complexion Cleansing Bar has a creamy, rich lather that leaves the skin feeling clean and refreshed. It is recommended for normal to oily skin types.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ambi_complexion_cleansing_bar_3.5_oz_1_800x_8ef19ded-8244-4eb3-a980-bd3b8c3bce0e_300x300.jpg?v=1645040595'
    },
    {
        'id': 67,
        'link': 'https://gimsap.ca/collections/all/products/ampro-pro-finishing-sheen-11-5oz',
        'name': 'Ampro Pro Finishing Sheen (11.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': "<p>Your hair is the crowning glory of your appearance. No matter how well you dress, your hair can make or break your appearance. It's important to take care of your hair and give it the attention it deserves. Ampro Pro Finishing Sheen is a revolutionary new product that helps you do just that. Ampro Pro Finishing Sheen has a lightweight formula that is designed to provide a high-gloss shine and eliminate frizz. It is water-based and does not contain any petroleum or alcohol, which means it won't damage your hair. The formula is also rich in natural ingredients such as shea butter, aloe vera, and avocado oil. These ingredients will not only moisturize your hair, but also make it soft and silky. Ampro Pro Finishing Sheen will make your hair look like you just left the salon. It will also provide UV protection for your hair, which is important because UV rays can damage your hair and make it brittle. Ampro Pro Finishing Sheen will help you look your best without the hassle of visiting the salon.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_300x300.png?v=1650575807'
    },
    {
        'id': 68,
        'link': 'https://gimsap.ca/collections/all/products/ampro-shine-n-jam-conditioning-gel-extra-hold-16oz',
        'name': 'Ampro Shine n Jam Conditioning Gel Extra Hold (16oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.50',
        'description': '<p>Give your hair the shine and control it needs with Ampro Shine n Jam Conditioning Gel Extra Hold. This extra-hold gel provides a healthy shine and prevents frizz for up to three days. Shine n Jam is a product for all hair types, even those with curly or permed hair. This product is perfect for people who want to keep their hair in place without using harsh chemicals.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ampro-shine-n-jam-gel-16oz_1_580x_96947c4a-118a-4ba8-b560-a382778a6464_300x300.jpg?v=1645040598'
    },
    {
        'id': 69,
        'link': 'https://gimsap.ca/collections/all/products/ampro-shine-n-jam-edges-shea-butter-2-25oz-firm-hold',
        'name': 'Ampro Shine n Jam Edges Shea Butter (2.25oz) Firm Hold',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': "<p>If you're looking for a product that will help keep your edges from sticking out, this is the product for you. It's a firm hold gel that is designed to keep your edges down and out of your face. This product is made with natural ingredients that are not only good for your hair, but also good for your skin. It also smells great, and has a light, citrusy scent. It's a versatile product that you can use on your hairline, edges, and scalp.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/AMP41105_1400x1400_1207ed44-a874-4dc8-9053-cca90b98248a_300x300.jpg?v=1645040601'
    },
    {
        'id': 70,
        'link': 'https://gimsap.ca/collections/all/products/ampro-shine-n-jam-extra-hold-8oz',
        'name': 'Ampro Shine n Jam Extra Hold (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.75',
        'description': '<p>Ampo Shine n Jam Extra Hold is a wax-based hair pomade that offers a strong hold with a high shine. This pomade is perfect for creating a messy, unkempt look that is still very clean. It has a sweet, refreshing scent and a smooth, non-greasy feel.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/71F9izw9vlL._AC_SX679_300x300.jpg?v=1645040605'
    },
    {
        'id': 71,
        'link': 'https://gimsap.ca/collections/all/products/ampro-shine-n-jam-regular-hold-8oz',
        'name': 'Ampro Shine n Jam Regular Hold (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.75',
        'description': '<p>Ampro Shine n Jam Regular Hold is a hair styling gel with a light, creamy texture that is easy to work through hair and offers a firm hold that lasts all day. The product is made with natural ingredients and does not contain alcohol, parabens, or artificial colors. It leaves hair feeling soft and clean.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/107428345_max_300x300.jpg?v=1645040607'
    },
    {
        'id': 72,
        'link': 'https://gimsap.ca/collections/all/products/ampro-shine-n-jam-silk-edges-8oz',
        'name': 'Ampro Shine n Jam Silk Edges (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.50',
        'description': '<p>Ampo Shine n Jam Silk Edges is a versatile hair care product that can be used on dry or wet hair. It’s perfect for styling, defining, and smoothing hair. Ampro Shine n Jam Silk Edges is made with shea butter, olive oil, and beeswax to make hair look healthy and shiny. The product also contains apple cider vinegar, aloe vera, and panthenol to condition and strengthen hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/b7111c8f-c84d-4278-9d14-f4a852ccfe0d_1.996b9aa4ef431e64e35160be1b756613_300x300.jpg?v=1645040603'
    },
    {
        'id': 73,
        'link': 'https://gimsap.ca/collections/all/products/amstel-malta',
        'name': 'amstel malta',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $45.00',
        'description': '<p>Amstel Malta is a refreshing, light beer with a hint of fruit. Amstel Malta is a perfect beer for any occasion, and is perfect for those who enjoy a light, fruity beer. Amstel Malta is brewed in the Netherlands, and is perfect for any occasion.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/AMSTEL-MALTA-BOTTLE-33CL_300x300.jpg?v=1645040556'
    },
    {
        'id': 74,
        'link': 'https://gimsap.ca/collections/all/products/anny-sardines',
        'name': 'Anny Sardines',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.95',
        'description': "<p>If you're looking for a high-quality canned fish product, then Anny Sardines are the right choice for you. This company has been a family-owned business for over 100 years, and their sardines are all sustainably sourced. They are canned in tomato sauce and they are packed in glass jars to ensure the quality of the product. This company is committed to the best quality and they never use preservatives or MSG. They are a company that believes in sustainability and in preserving the environment.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Anny-Sardines-800x542_300x300.jpg?v=1645040567'
    },
    {
        'id': 75,
        'link': 'https://gimsap.ca/collections/all/products/apple-snail',
        'name': 'Apple Snail',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<span data-mce-fragment="1">The largest of freshwater snails, Apple Snails are found in tropical and subtropical wetlands worldwide.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/APPSNAIL-NEW-1_300x300.png?v=1650387158'
    },
    {
        'id': 76,
        'link': 'https://gimsap.ca/collections/all/products/apricots-lb',
        'name': 'Apricots /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>Our apricots are a tasty and nutritious addition to any breakfast. The sweet flavor is a perfect complement to a glass of orange juice or tea. Our apricots are available in a one pound package.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b2e58ac1-0da7-4bda-ad61-15237eddf894_300x300.jpg?v=1646857552'
    },
    {
        'id': 77,
        'link': 'https://gimsap.ca/collections/all/products/apricots-12-7-kg',
        'name': 'Apricots 12.7 Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $118.00',
        'description': '<p>Apricots are a delicious and healthy fruit. They are great for snacking, as well as adding to salads and desserts. Apricots are a good source of vitamin A, vitamin C, iron, potassium, and calcium.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ec5ce1ac-14bf-49c9-8d8f-a597a2349d91_300x300.jpg?v=1646857551'
    },
    {
        'id': 78,
        'link': 'https://gimsap.ca/collections/all/products/ariel-detergent-170g',
        'name': 'Ariel Detergent 170g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Ariel Detergent 170g is a soap powder that is formulated to provide a good clean for all types of fabrics. This product is made from biodegradable and renewable resources and is designed to be tough on dirt and stains while being gentle on clothes. Ariel Detergent 170g also comes in a powdered form that dissolves in cold water, which makes it easy to use and convenient.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_15f8c2ba-ef6b-432e-a600-38ae78cfbafe_300x300.jpg?v=1650576342'
    },
    {
        'id': 79,
        'link': 'https://gimsap.ca/collections/all/products/asepso-soap',
        'name': 'Asepso Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Asepso soap is made from natural ingredients and is biodegradable. It is handmade and hand-wrapped in cellophane. It comes in a variety of scents and colors.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_902d82ea-e840-43eb-b397-03b82cfc5fa9_300x300.jpg?v=1646857536'
    },
    {
        'id': 80,
        'link': 'https://gimsap.ca/collections/all/products/asst-hair-nail-ring-bead-x-l',
        'name': 'Asst Hair &amp; Nail Ring Bead (X.L)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.99',
        'description': '<p>The variety of hair decorator colors will allow you to customize your look and find the perfect match for your hair type.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_cd8065de-cf01-446b-832d-99c7d3cbea60_300x300.jpg?v=1645040584'
    },
    {
        'id': 81,
        'link': 'https://gimsap.ca/collections/all/products/attieke-box-cassava-couscous-300g',
        'name': 'Attieke Box Cassava Couscous 300g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $120.00',
        'description': '<p>Attieke Box Cassava Couscous is a delicious and versatile food made from the ground and boiled root of the cassava plant. This product is an excellent source of carbohydrates, protein, dietary fiber, and potassium. Attieke Box Cassava Couscous is also a good source of calcium, vitamin C, and iron. It is gluten-free and has no added salt. Attieke Box Cassava Couscous is a versatile ingredient that can be used in a variety of dishes, such as a salad, in a stew, or even in a soup. It can also be mixed with rice to make an alternative to rice and beans.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_61ea8c73-4cb4-4290-8b46-f3e416cb67c2_300x300.jpg?v=1646857543'
    },
    {
        'id': 82,
        'link': 'https://gimsap.ca/collections/all/products/attieke-cassava-couscous-300g',
        'name': 'Attieke Cassava Couscous 300g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Attieke Cassava Couscous is a quick-cooking, gluten-free, vegan-friendly, easy-to-prepare product. The couscous is made from cassava root flour, so it is high in protein and fiber. It has a low glycemic index and contains no cholesterol. Attieke Cassava Couscous is ready in five minutes and is perfect for a quick meal or side dish. It can be used in a variety of dishes, from salads to curries.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/nayama_Attieke_300x300.jpg?v=1645040555'
    },
    {
        'id': 83,
        'link': 'https://gimsap.ca/collections/all/products/attieke-couscous-500g',
        'name': 'Attieke Couscous 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p>Attieke Couscous is a delicious and healthy alternative to rice, pasta, and other grains. This grain is a staple in North African cuisine and is often used in couscous dishes. Attieke Couscous has a nice, nutty flavor and is best served with vegetables, beans, lentils, or any type of meat.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9a935bf8-5745-475b-aaa6-4e2459417790_300x300.jpg?v=1646857547'
    },
    {
        'id': 84,
        'link': 'https://gimsap.ca/collections/all/products/australian-goat-burnt-lb',
        'name': 'Australian goat burnt /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.50',
        'description': '<p>The best way to describe Australian goat burnt is to describe the taste. This type of goat meat is not as spicy as other types of goat meat. The taste is savory and complex. It is also very tender and has a sweet flavor. When cooked properly, it can have a deep, rich flavor. The best way to cook this type of goat meat is by grilling or barbecuing.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_4367c31c-c871-42fe-bd43-965dd01b64e6_300x300.jpg?v=1647370139'
    },
    {
        'id': 85,
        'link': 'https://gimsap.ca/collections/all/products/australian-goat-unburnt-lb',
        'name': 'Australian goat unburnt /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': "<p>The Aussie goat is a hearty, resilient animal that is known for its delicious meat. If you're looking for a fresh, delicious and lean protein source, this is the way to go.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_9c6dcc76-e70a-47f7-9acd-1c398fbbb20a_300x300.jpg?v=1647370195'
    },
    {
        'id': 86,
        'link': 'https://gimsap.ca/collections/all/products/ayoola-plantain-flour-2lbs',
        'name': 'Ayoola Plantain Flour (2lbs)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>This flour is the product of grinding plantains into a fine powder. It is gluten-free and provides a high amount of dietary fiber. Ayoola Plantain Flour is a nutritious and easy-to-use ingredient for a variety of recipes. The flour is also a good source of potassium and vitamin C,. Ayoola Plantain Flour is perfect for baking breads, cakes, or muffins.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ay450_300x300.jpg?v=1645040575'
    },
    {
        'id': 87,
        'link': 'https://gimsap.ca/collections/all/products/ayoola-plantain-flour-4lb',
        'name': 'Ayoola Plantain Flour 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.00',
        'description': '<p>Ayoola Plantain Flour is a gluten-free, vegan, and organic product that is perfect for those with a variety of dietary restrictions. This flour can be used in a variety of ways such as a substitute for wheat flour in baking, as a thickener for soups, and as a coating for fried foods. The flour is also packed with vitamins and minerals, so it is perfect for those looking to increase their intake of these essential nutrients.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d32d8d76-8087-45c2-917d-9d9068a555ab_300x300.jpg?v=1646857555'
    },
    {
        'id': 88,
        'link': 'https://gimsap.ca/collections/all/products/ayoola-pounded-yam',
        'name': 'Ayoola Pounded Yam',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Pounded Yam is a delicacy made from grated yam, water, and a little salt. It is a good source of carbohydrates and provides a sense of satisfaction. It is typically eaten with Nigerian staple dishes such as Jollof Rice, Moin-Moin, Egusi Soup, or Ogi.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/6151100001023-2_300x300.jpg?v=1645040573'
    },
    {
        'id': 89,
        'link': 'https://gimsap.ca/collections/all/products/b-b-firm-hold-curling-gel-6oz',
        'name': 'B&amp;B Firm Hold Curling Gel (6oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.50',
        'description': '<p><meta charset="utf-8"><span>BB® Firm Hold Curling Gel is designed for wavy to curly kinky hair. It reduces bulk and provides weightless control. BB® Firm Hold Curling Gel enhances manageability, tames frizz, defines and elongates waves and curls.</span><br></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_48c1319e-0c24-4dbc-89b1-763bfec538ce_300x300.jpg?v=1646857901'
    },
    {
        'id': 90,
        'link': 'https://gimsap.ca/collections/all/products/bs-organic-jojoba-oil',
        'name': "B's Organic Jojoba oil",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>Organic Jojoba oil is a 100% pure, unrefined, non-GMO, cold-pressed plant oil. It is high in vitamin E and antioxidants, making it a great skin moisturizer. Jojoba oil can be used for everything from hair to skin to nails. It's perfect for those with sensitive skin and for those who want to avoid using animal products.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5be1ec8d-2b9b-4af6-bb9a-d8cb8b909ab1_300x300.jpg?v=1646857534'
    },
    {
        'id': 91,
        'link': 'https://gimsap.ca/collections/all/products/baby-wool',
        'name': 'Baby wool',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Baby wool is very soft and comfortable. It can be used for a variety of things such as knitting.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f446a07e-a1c0-44e5-84e0-ef6b7a5f68dd_300x300.jpg?v=1645127996'
    },
    {
        'id': 92,
        'link': 'https://gimsap.ca/collections/all/products/bambara-beans-lb',
        'name': 'Bambara Beans /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The bambara beans, also known as the "bush bean," are a staple in West African cuisine. They are usually prepared with tomatoes, onions, and peppers. The bambara beans are a legume that is found in the West African region. They are often prepared with tomatoes, onions, and peppers.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_04f87ddb-e5e2-49d9-82b2-97a7ce35cd3e_300x300.jpg?v=1645127982'
    },
    {
        'id': 93,
        'link': 'https://gimsap.ca/collections/all/products/banga-fresh-palm-fruits-extracts-400g',
        'name': 'Banga Fresh Palm Fruits Extracts 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>The extract is created from the pure and natural fruit. It is free from cholesterol, rich in vitamin K, A and E and Magnesium.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_149d8d20-7518-4949-ad98-001f8004bd55_300x300.jpg?v=1645128022'
    },
    {
        'id': 94,
        'link': 'https://gimsap.ca/collections/all/products/banga-soup-spice',
        'name': 'Banga Soup Spice',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>A traditional Bengali recipe that is not only delicious but also nutritious. It includes onion, tomato, cumin, coriander, chili, garlic, ginger, and turmeric.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 95,
        'link': 'https://gimsap.ca/collections/all/products/banga-spice-lb',
        'name': 'Banga spice /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Banga spice is a hot, flavorful blend of red pepper, onion, garlic, salt, and other spices. It can be used in both hot and cold dishes, and is particularly popular in Caribbean cuisine.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c4ecbc74-b53a-4b2f-8c4f-2fc9b12554c0_300x300.jpg?v=1645127978'
    },
    {
        'id': 96,
        'link': 'https://gimsap.ca/collections/all/products/banku-mix-home-fresh-2-2lb-box',
        'name': 'Banku Mix (home fresh 2.2lb (box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $97.50',
        'description': '<p>Banku Mix is a mix&nbsp; that can be served with rice or as a meal in itself. The mix includes ingredients such as dried fish, ground beef, cornmeal, tomato paste, onion, and black pepper. The dish is cooked in a pot of boiling water for 15 minutes and then served with rice.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e459a132-3d4f-44f5-b62c-bdf11dee92cd_300x300.jpg?v=1645128007'
    },
    {
        'id': 97,
        'link': 'https://gimsap.ca/collections/all/products/banku-mix-home-fresh-2-2lb',
        'name': 'Banku Mix 2.2lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>It is a blend of fermented corn meal, millet, sorghum, and cassava flour. It is a staple in the diet of many West African countries. Banku Mix is a quick and easy way to enjoy this delicious dish. It can be used as a base for soup, mixed with fresh vegetables, or used as a coating for fish or meat.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7d95da56-cf45-4d20-b10c-00d98ca0de58_300x300.jpg?v=1645128008'
    },
    {
        'id': 98,
        'link': 'https://gimsap.ca/collections/all/products/banku-mix-flour-cosmas-2-2lbs',
        'name': 'Banku Mix Flour (Cosmas) 2.2lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>Banku Mix Flour is a traditional African product used to make banku, a fermented, spongy bread. This product is typically made with maize, rice, or sorghum. Banku Mix Flour is traditionally used to make this bread and is made from maize, rice, and sorghum.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_2e3ca634-c853-42e7-b112-5e115b35c354_300x300.jpg?v=1644951769'
    },
    {
        'id': 99,
        'link': 'https://gimsap.ca/collections/all/products/basa-fillet',
        'name': 'Basa fillet',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Basa fillet is a fish that is low in fat and high in protein. The Basa fillet is harvested from the Basa fish. It is a flat, white fish that is a tropical fish found in Southeast Asia.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_6dba6df3-fdd5-4b24-942e-0c35270fb014_300x300.jpg?v=1647370803'
    },
    {
        'id': 100,
        'link': 'https://gimsap.ca/collections/all/products/basa-fillet-40-lb-box',
        'name': 'Basa fillet (40 lb) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': "<p>The basa fillet is a mild white fish, which has a delicate flavor and texture. It's a great fish for those who are new to fish, or those who are just trying to add variety to their diet. Basa is also a great fish for those who want to reduce their fat intake. The box contains 40 lbs of basa fillet, which is enough to feed a family of four for a week. This fish is easy to prepare and goes well with a variety of side dishes. It's an excellent choice for an economical and healthy meal.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/SEA012_A_300x300.jpg?v=1647371910'
    },
    {
        'id': 101,
        'link': 'https://gimsap.ca/collections/all/products/basmati-rice-10lbs',
        'name': 'Basmati Rice',
        'price': 'From $17.50',
        'description': '<p>Maharani Basmati Rice is an aromatic rice with a nutty flavor and a distinctive, fluffy texture. It is a long-grain rice and is grown in the foothills of the Himalayas. Basmati Rice is perfect for pilafs, soups, and side dishes. It has a distinctive, fluffy texture and a nutty flavor. Basmati Rice is perfect for pilafs, soups, and side dishes.<span data-mce-fragment="1">&nbsp;The grains are slender and have a higher protein content than other rice varieties. Basmati Rice is typically used in Indian cuisine and is known for its distinctive flavor and aroma. Available in 10lb and 40lb bags.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Maharani_Rice_10lbs_530x_2x_d3e685cf-a278-4e2e-9f42-ebf562b5e601_300x300.jpg?v=1647375962'
    },
    {
        'id': 102,
        'link': 'https://gimsap.ca/collections/all/products/bay-leaves-whole-2-27kg',
        'name': 'Bay Leaves whole 2.27kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>They are also used in traditional dishes such as rice pilaf, rice stuffing, and chowders. Bay leaves are also used in soups and stews to give a subtle flavor. Bay leaves are the leaves of the bay laurel tree. They have a spicy, sweet flavor with a hint of citrus. The leaves are dried and crumbled before use. &nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/bay-leaves-dry-2500-56a210353df78cf772718c1f_300x300.jpg?v=1647372338'
    },
    {
        'id': 103,
        'link': 'https://gimsap.ca/collections/all/products/bay-leaves-whole-per-lb',
        'name': 'Bay Leaves whole per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The leaves are harvested when they are a deep green color and they are dried in the sun or air-dried. Bay leaves are used in many cooking recipes, especially those with heavy sauces or tomato based sauces.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/bay-leaves-dry-2500-56a210353df78cf772718c1f_e38f5c13-b80d-4748-a4ac-a2ca0e426c3c_300x300.jpg?v=1647372426'
    },
    {
        'id': 104,
        'link': 'https://gimsap.ca/collections/all/products/bean-flour-2lbs',
        'name': 'Bean Flour 2Lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p>It's the perfect alternative to regular flour, for those who have gluten sensitivities. It's a great substitute for anyone looking to make baked goods or pastries, or for anyone looking to make a healthy version of fried chicken. It's a great option for those looking to limit their sugar intake. Benefits: -Gluten-free -A healthy alternative to regular flour -Perfect for making baked goods or pastries -Great for making fried chicken</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_76bbc3d0-36ca-46e2-aec9-732c784518d5_300x300.jpg?v=1645127981'
    },
    {
        'id': 105,
        'link': 'https://gimsap.ca/collections/all/products/bean-flour-whole-2-5kg',
        'name': 'Bean Flour Whole 2.5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Bean Flour Whole is a good alternative to traditional wheat flour. This product is made from 100% organic beans and it is free of gluten, sugar, and other additives. It can be used in many recipes including making pasta, pizza crust, muffins, and more. This product is also vegan and provides protein, iron, and fiber.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c0d1109a-f5ca-4d05-b921-ac6ba47314be_300x300.jpg?v=1647372914'
    },
    {
        'id': 106,
        'link': 'https://gimsap.ca/collections/all/products/bean-flour-whole-per-lb',
        'name': 'Bean Flour Whole per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><meta charset="utf-8"><span>Bean Flour Whole is a good alternative to traditional wheat flour. This product is made from 100% organic beans and it is free of gluten, sugar, and other additives. It can be used in many recipes including making pasta, pizza crust, muffins, and more. This product is also vegan and provides protein, iron, and fiber.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d444a62f-a44c-4fbc-97ab-1f8da49520ec_300x300.jpg?v=1647372987'
    },
    {
        'id': 107,
        'link': 'https://gimsap.ca/collections/all/products/beans-flour-tasty-pot-1-kg',
        'name': 'Beans Flour (Tasty Pot) 1 Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': "<p>The thick and hearty Beans Flour (Tasty Pot) 1 Kg is a hearty blend of black beans, rice, and spices. It's a good source of protein and fiber, and can be used in a variety of dishes including Mexican rice, rice pudding, and rice balls.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b70d5112-81d8-4efd-9be3-68bb843db020_300x300.jpg?v=1645128021'
    },
    {
        'id': 108,
        'link': 'https://gimsap.ca/collections/all/products/beans-flour-1-kg-todaj',
        'name': 'Beans Flour 1 Kg (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>This product is made from selected beans and is ground to a fine flour. It is a perfect ingredient for baking and cooking. This product is gluten-free and can be used in place of wheat flour.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dde3293a-6076-4746-b0f7-e1ba17fe7d68_300x300.jpg?v=1645128024'
    },
    {
        'id': 109,
        'link': 'https://gimsap.ca/collections/all/products/beans-flour-2lb-abiola-foods',
        'name': 'Beans Flour 2lb (Abiola Foods)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>In West Africa, beans are a staple crop and one of the main sources of protein. Abiola Foods offers beans flour in 2lb bags. The beans are sourced from Nigeria and ground into a fine powder. The flour is high in protein and can be used in a variety of dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cd5ed681-d6e3-4032-900f-7508f1fba41f_300x300.jpg?v=1645128003'
    },
    {
        'id': 110,
        'link': 'https://gimsap.ca/collections/all/products/beans-flour-2lb-9kg-deluxe',
        'name': 'Beans Flour 2lb/.9kg (Deluxe)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>This flour has been specifically designed to be gluten-free and perfect for baking. This product is made from beans and is a much healthier alternative to regular flour. The beans used in this product are carefully selected to be high in protein and provide a healthy balance of carbohydrates. The product is also free of any artificial flavors, preservatives, or sweeteners.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cbcc6adc-f9ac-4e4a-a5a3-11be486becc3_300x300.jpg?v=1647374124'
    },
    {
        'id': 111,
        'link': 'https://gimsap.ca/collections/all/products/beans-flour-4lb',
        'name': 'Beans Flour 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p><meta charset="utf-8"><span>Bean Flour Whole is a good alternative to traditional wheat flour. This product is made from 100% organic beans and it is free of gluten, sugar, and other additives. It can be used in many recipes including making pasta, pizza crust, muffins, and more. This product is also vegan and provides protein, iron, and fiber.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_df41846e-6bec-42b5-886f-96006b4b6e2f_300x300.jpg?v=1647374209'
    },
    {
        'id': 112,
        'link': 'https://gimsap.ca/collections/all/products/beans-flourola-ola-1-30lbs',
        'name': 'Beans flour(ola-ola) 1.30lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>For a complete protein, these beans flour are perfect for your everyday meal. Made from finely ground beans, these beans flour are low in fat and cholesterol. A great source of protein, these beans flour will help you stay full and focused. The perfect way to cook up your beans, these beans flour are great for a side dish or even a main dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-15at2.43.42PM_300x300.png?v=1647377069'
    },
    {
        'id': 113,
        'link': 'https://gimsap.ca/collections/all/products/beans-leaf',
        'name': 'Beans Leaf',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': "<p>A tasty, healthy alternative to the morning cup of coffee, Beans Leaf is made from 100% pure, organically grown green beans. Beans Leaf has a light, smooth flavor that doesn't leave an unpleasant aftertaste. It is not too strong, but still has a powerful flavor that gets you going in the morning. The caffeine in Beans Leaf is a great way to give you a quick boost in the morning. Beans Leaf also has natural antioxidants that are beneficial for your health. Try it today and experience the benefits of a healthier lifestyle.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_754063c1-d7e3-4608-9f9c-67c62ad193b0_300x300.jpg?v=1645127986'
    },
    {
        'id': 114,
        'link': 'https://gimsap.ca/collections/all/products/beef-heart',
        'name': 'Beef Heart',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Beef heart is a cut of meat that is an excellent source of protein, iron, and other nutrients. Beef heart is usually cooked and eaten as a sandwich, served with fries, or in a salad.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_65575409-1934-4a24-aec4-a3a448ae61f1_300x300.jpg?v=1647377525'
    },
    {
        'id': 115,
        'link': 'https://gimsap.ca/collections/all/products/beef-intestine-lb',
        'name': 'Beef intestine /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>These beef intestines are cooked and sliced for an easy to use and delicious snack. The intestines are typically used in the French dish, Chitterlings, but can also be used in soups, sausages, and pates. Beef intestines are low in fat and cholesterol and high in protein.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_96930982-26ec-439c-8caf-aaa0e40dc641_300x300.jpg?v=1645127972'
    },
    {
        'id': 116,
        'link': 'https://gimsap.ca/collections/all/products/beef-kidney-lb',
        'name': 'Beef Kidney /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>The Kidney is the most flavorful part of the beef. It is great for stewing, curries, and even as a steak.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5fa4d8aa-600a-4487-9c39-1031f735818a_300x300.jpg?v=1645127992'
    },
    {
        'id': 117,
        'link': 'https://gimsap.ca/collections/all/products/beef-kidney-box',
        'name': 'Beef Kidney Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>The kidney is harvested from the steer and can be used in a variety of dishes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_32bd9937-47ba-418a-b010-8f765fc6de5c_300x300.jpg?v=1645127988'
    },
    {
        'id': 118,
        'link': 'https://gimsap.ca/collections/all/products/beef-liver-lb',
        'name': 'Beef Liver /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The beef liver is a healthy meat, which is high in protein and vitamins. It is a natural food that has been eaten for centuries. This is the perfect meal for a healthy diet. The beef liver is made up of a large number of nutrients, including iron, potassium, and vitamin B12.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_73257d5f-420a-43e9-8028-6876ed2e4b7a_300x300.jpg?v=1645127991'
    },
    {
        'id': 119,
        'link': 'https://gimsap.ca/collections/all/products/beef-lungs-lb',
        'name': 'Beef Lungs /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The first thing that comes to mind when thinking about beef lungs is the need for the offal to be cooked. The lungs are the largest organ in the body and are a great source of high-quality protein. Beef lungs are most often used in the preparation of classic dishes such as pot roast, braised short ribs, or soup.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_300x300.png?v=1647377623'
    },
    {
        'id': 120,
        'link': 'https://gimsap.ca/collections/all/products/beef-meat-lb',
        'name': 'Beef meat /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.50',
        'description': "<p>Your family deserves the best, and that's what we offer with our natural beef. Our beef is all natural, antibiotic-free, and 100% grass-fed. With all of these great benefits, your family will love it. Here's what you can expect from our beef: 100% Grass-fed 100% Natural 100% Antibiotic-free 100% Sustainable 100% Humanely Raised We take pride in our beef, and we know you'll love it too.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cc661d79-df64-4dc8-82d0-42a0ea38bdbb_300x300.jpg?v=1645127973'
    },
    {
        'id': 121,
        'link': 'https://gimsap.ca/collections/all/products/beef-shank',
        'name': 'Beef Shank',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>&nbsp;Beef shanks are taken from the front of the animal and are cut into large, round pieces. This cut of meat is a leaner cut, with less fat than other cuts. Beef shanks are perfect for braising or roasting, as they are so large and will not dry out easily.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-43_300x300.png?v=1606145528'
    },
    {
        'id': 122,
        'link': 'https://gimsap.ca/collections/all/products/beef-shank-b-less-per-lb',
        'name': 'Beef shank b/less per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': "<p>Everyday people are constantly looking for new ways to prepare the meat they buy from the grocery store. Beef shank is one of the most popular ways to prepare beef because it's so versatile. It can be used in soups, stews, and sauces, or you can simply roast it in the oven. This is an affordable cut of meat that's perfect for families who are looking to save money while still eating delicious food.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_32115fd1-afe7-4d74-bed0-8cf6277960f3_300x300.jpg?v=1645127974'
    },
    {
        'id': 123,
        'link': 'https://gimsap.ca/collections/all/products/beef-tendon-lb',
        'name': 'Beef tendon /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Ranchers use beef tendon to make beef jerky. Beef tendon is a beef byproduct, so it is a cheaper alternative to beef. Beef tendon has a chewy texture and it is usually cut into small pieces.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_20c12d0f-2429-4830-ab49-8a0a888b3a9c_300x300.jpg?v=1645127975'
    },
    {
        'id': 124,
        'link': 'https://gimsap.ca/collections/all/products/beef-tongue-lb',
        'name': 'Beef Tongue /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p>This is a great option for those who are looking for a delicious, high-quality protein that is great for grilling, braising, or simmering.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/beef-tongue_300x300.jpg?v=1647457244'
    },
    {
        'id': 125,
        'link': 'https://gimsap.ca/collections/all/products/beef-tripe-lb',
        'name': 'Beef tripe',
        'price': 'From $10.00',
        'description': '<p>This is the stomach of a cow that has been cleaned and stripped of its outer lining.&nbsp; The lining of the stomach can be boiled and eaten, or used in dishes such as pot pie, meatloaf, and more. Beef tripe is a great alternative to ground beef in recipes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/956984e67b58b55f4c0b209efaf55232_300x300.jpg?v=1647552760'
    },
    {
        'id': 126,
        'link': 'https://gimsap.ca/collections/all/products/beef-tripe-box-50lb-uncut',
        'name': 'Beef Tripe Box 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $160.00',
        'description': '<p>This product is a box of frozen cleaned beef tripe. Beef tripe is&nbsp;the edible lining of the stomach of a cow. Beef tripe is sold raw and can be cooked to create a variety of dishes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-15at3.57.25PM_300x300.png?v=1647381495'
    },
    {
        'id': 127,
        'link': 'https://gimsap.ca/collections/all/products/beef-tripe-box-60lb-uncut-cargil',
        'name': 'Beef Tripe Box 60lb Uncut (Cargil)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $180.00',
        'description': "<p>The tripe box contains a minimum of 60 pounds of beef tripe that you can use to make a variety of dishes. You can make a soup, a sauce, or even a delicious filling for your tacos. Tripe is a popular ingredient in many cuisines, including Italian, Greek, and Mexican. It's a great way to add a little variety to your diet.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-15at4.06.56PM_300x300.png?v=1647382057'
    },
    {
        'id': 128,
        'link': 'https://gimsap.ca/collections/all/products/bell-pepper-small-box',
        'name': 'Bell pepper (small) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p>This small box of bell peppers is perfect for a small dinner party or an evening in with your loved one. These peppers are flavorful and a great addition to any dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f65b8f41-fead-4ab0-97b7-062a434e2ad4_300x300.jpg?v=1645128004'
    },
    {
        'id': 129,
        'link': 'https://gimsap.ca/collections/all/products/bell-pepper-tatase-fam-pac',
        'name': 'Bell Pepper (Tatase) fam pac',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Bell Pepper (Tatase) is perfect for when you want a sweet and savory flavor.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_00ced363-24ab-4c58-bec9-c51b5d6daf65_300x300.jpg?v=1645128011'
    },
    {
        'id': 130,
        'link': 'https://gimsap.ca/collections/all/products/benedicta-oil-1lt',
        'name': 'Benedicta oil 1lt',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>Benedicta oil is a herbal oil blend for the treatment of various skin conditions. It is rich in natural oils, like olive, jojoba, almond, and evening primrose, and can be used for the prevention and treatment of a variety of skin conditions. The skin regenerating properties of the oil, combined with its anti-inflammatory and anti-aging properties, make it a great product for all skin types.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8ef051a2-aa13-4421-b0bf-a8c04623ff33_300x300.jpg?v=1645127999'
    },
    {
        'id': 131,
        'link': 'https://gimsap.ca/collections/all/products/benedicta-oil-500ml',
        'name': 'Benedicta oil 500ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Benedicta oil is a plant-based oil, made from the seed of the ben oil tree. This oil is a rich source of essential fatty acids, as well as Vitamin E. This oil can be used in a variety of ways, including cooking, moisturizing, and in skincare products.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a8386b01-62cf-4797-aa8f-daec6c547d35_300x300.jpg?v=1647461223'
    },
    {
        'id': 132,
        'link': 'https://gimsap.ca/collections/all/products/benny-17g-powdered-chicken-flavour',
        'name': 'Benny 17g Powdered Chicken Flavour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.99',
        'description': '<p>Benny 17g Powdered Chicken Flavour</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_42e179b1-bcd1-4fa5-a9fc-0b80c25bd059_300x300.jpg?v=1645128013'
    },
    {
        'id': 133,
        'link': 'https://gimsap.ca/collections/all/products/benny-17g-x-42-powdered-chicken-flavour',
        'name': 'Benny 17g x 42 Powdered Chicken Flavour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>&nbsp;This soup flavour can be added to any dish to add some additional taste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f4cd6af7-89bb-46bb-a477-3fa70d99dd41_300x300.jpg?v=1645128023'
    },
    {
        'id': 134,
        'link': 'https://gimsap.ca/collections/all/products/besugo-fish',
        'name': 'Besugo fish',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>The Besugo fish is a medium-sized fish that is usually found in shallow waters. They are typically white with a silver-grey hue and are excellent at jumping out of the water. This is a very good source of protein and is not a difficult fish to cook.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_6385c97c-8e1a-4eb3-ac5e-71ca7192dc1f_300x300.jpg?v=1647382431'
    },
    {
        'id': 135,
        'link': 'https://gimsap.ca/collections/all/products/big-mama-palmnut-cream-800g',
        'name': 'Big Mama Palmnut Cream 800g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Big Mama Palmnut Cream is extract that comes from palm fruit and it goes well with West African soups ;like Banga soup.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-16at2.07.55PM_300x300.png?v=1647461368'
    },
    {
        'id': 136,
        'link': 'https://gimsap.ca/collections/all/products/big-whole-chicken-25kg-box',
        'name': 'Big Whole Chicken 25kg box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': "<p>This 25kg box of chicken is a great way to feed a large family or group of friends. It's full of high-quality, all-natural chicken. Whether you want to roast it, fry it, or just eat it raw, this chicken is perfect for any occasion.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_431af4b0-79b8-42c1-bb2d-024c88a646cc_300x300.jpg?v=1645128121'
    },
    {
        'id': 137,
        'link': 'https://gimsap.ca/collections/all/products/big-whole-chicken-box-kg',
        'name': 'Big Whole Chicken box /kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.20',
        'description': "<p>At a glance, it's clear that this whole chicken is bigger than most. The skin is a beautiful golden brown, and the size of the bird is likely to provide a meal for a small family.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c1284f7d-6186-47c4-a825-9bb08e48e186_300x300.jpg?v=1645128117'
    },
    {
        'id': 138,
        'link': 'https://gimsap.ca/collections/all/products/bigen-black-brown-hair-color',
        'name': 'Bigen Black Brown Hair Color',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Bigen is a hair color that provides a deep, rich brown color. It is perfect for anyone looking to enhance their natural hair color. This product is ammonia-free and can be used on all hair types. It is safe for children and provides gentle conditioning for the hair.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Bigen-black-brown-hair-color-58-6g_1024x1024_fb6c3b58-5ebb-49bd-85ab-0a53573606f1_300x300.jpg?v=1647461524'
    },
    {
        'id': 139,
        'link': 'https://gimsap.ca/collections/all/products/bilolo-30x500g-bened-box',
        'name': 'Bilolo (30x500g Bened) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $165.00',
        'description': '<p><strong>Description:</strong></p>\n<p>Product: Bilolo</p>\n<p>Qty: 500g (30x) -- Box</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/bitter-leaves-bilolo-02_300x300.jpg?v=1647467629'
    },
    {
        'id': 140,
        'link': 'https://gimsap.ca/collections/all/products/bilolo-bened-500g',
        'name': 'Bilolo (Bened) 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p><strong>Description:</strong></p>\n<p>Product: Bilolo</p>\n<p>Qty: 500g</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/bitter-leaves-bilolo-02_a6737175-fc41-47d1-bdd2-e3a5bd063a6e_300x300.jpg?v=1647467680'
    },
    {
        'id': 141,
        'link': 'https://gimsap.ca/collections/all/products/biscuit-bone',
        'name': 'Biscuit Bone',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p>Biscuit Bone's texture is soft and when bitten fall into crumbs. It becomes soft and chewable when steamed for a long time or boiled.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-16at4.10.53PM_300x300.png?v=1647469469'
    },
    {
        'id': 142,
        'link': 'https://gimsap.ca/collections/all/products/bistak-natural-honey-500g',
        'name': 'Bistak Natural Honey 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.50',
        'description': '<p>The taste of this honey is pleasantly smooth and the color is a light golden yellow. The natural flavors of this honey make it a perfect choice for baking. It has a low moisture content, which makes it perfect for preserving food. Bistak Natural Honey is a 500g jar of raw, unprocessed honey. This is a great choice for those who are looking for a pure, natural product that is great for baking.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f45ac62f-7d8d-4cc2-81fe-fbe2d9eaeb8d_300x300.jpg?v=1645128165'
    },
    {
        'id': 143,
        'link': 'https://gimsap.ca/collections/all/products/bitekuteku-folon-or-tete-frozen-700g',
        'name': 'Bitekuteku (Folon or Tete) frozen 700g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Bitekuteku is a&nbsp;vegetable&nbsp;similar to spinach in taste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_908d539c-5fcc-449b-877f-9c538e75eccb_300x300.jpg?v=1645128134'
    },
    {
        'id': 144,
        'link': 'https://gimsap.ca/collections/all/products/bitter-cola-orogbo-lb',
        'name': 'Bitter Cola (Orogbo)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>The Orogbo people of Nigeria have been using this plant as a medicinal herb for centuries. The plant is indigenous to the Orogbo region and is a member of the Rubiaceae family. The plant&nbsp;can be dried and ground into a powder. Traditionally, the powder is mixed with water to make a tea that is consumed to treat stomach pains, heartburn, and indigestion. This powder can also be mixed with other herbs to make a traditional medicine. The use of this herb in Nigerian cuisine is not widespread, but some recipes call for the herb to be added to soups and stews.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_74ee0345-0f38-4c23-b5dd-357694f98b72_300x300.jpg?v=1645128145'
    },
    {
        'id': 145,
        'link': 'https://gimsap.ca/collections/all/products/bitter-yam-box',
        'name': 'Bitter Yam (box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $115.00',
        'description': '<p>Bitter Yam is a 100% natural product that can be used to promote healthy digestion. The supplement is designed to help the body break down food, absorb nutrients, and release toxins. Bitter Yam has been shown to be effective in aiding the digestion of fats, carbohydrates, and proteins. It also provides natural protection against bacteria, parasites, and viruses. This supplement is made from the dried and ground roots of the bitter yam plant. The plant grows in a tropical climate and is considered to be a valuable food crop in many parts of the world. The supplement is an excellent source of beta-carotene, vitamin C, and iron.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_71800f6b-8d10-4ed6-9c68-81818e62367f_300x300.jpg?v=1645128140'
    },
    {
        'id': 146,
        'link': 'https://gimsap.ca/collections/all/products/bitter-yam-per-pound',
        'name': 'Bitter Yam (per pound)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Bitter yams are a staple in many African and Caribbean cuisines.&nbsp; One pound of this product contains an impressive 17% of the daily value of vitamin C, a little less than 1% of the daily value of iron, and a little more than 3% of the daily value of potassium. They also contain trace amounts of vitamin A, B6, and B12. Bitter yams are easy to prepare and have a similar consistency to potatoes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_24f1d329-3b5f-4917-93ee-6edccd403cbf_300x300.jpg?v=1645128144'
    },
    {
        'id': 147,
        'link': 'https://gimsap.ca/collections/all/products/black-wild-rice-4lb',
        'name': 'Black (wild)  rice 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $44.00',
        'description': '<p><meta charset="utf-8"><span>The aroma of this rice is out of this world. It is a highly nutritious and tasty food, made with a blend of long-grain rice and black rice. The product is a mix of the health benefits of brown rice and the taste of black rice.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at1.51.46PM_fef9be9b-f15e-4ddc-b7e1-a7b4d583a8bb_300x300.png?v=1647547003'
    },
    {
        'id': 148,
        'link': 'https://gimsap.ca/collections/all/products/black-wild-rice-10kg',
        'name': 'Black (wild) rice 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $220.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">The aroma of this rice is out of this world. It is a highly nutritious and tasty food, made with a blend of long-grain rice and black rice. The product is a mix of the health benefits of brown rice and the taste of black rice.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at1.51.46PM_300x300.png?v=1647546814'
    },
    {
        'id': 149,
        'link': 'https://gimsap.ca/collections/all/products/black-pepper',
        'name': 'Black pepper',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>The sweet, spicy, and savory taste of black pepper is one of the most well-known spices in the world. This spice is made from the ground, dried berries of the plant Piper nigrum. The ground pepper is made into a fine powder and can be used in a variety of dishes, including curries, stir-fries, and sauces.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_19187258-fc31-4171-a1ef-260c12e67d3d_300x300.jpg?v=1645128131'
    },
    {
        'id': 150,
        'link': 'https://gimsap.ca/collections/all/products/black-pepper-ground',
        'name': 'black pepper ground',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': "<p>The world's most popular spice, black pepper is the perfect addition to any dish. Whether you're making a traditional beef stroganoff or a healthy, light vegan stir fry, black pepper can be used to add a spicy kick to any dish. Black pepper is also a great spice to use when preparing fried chicken or shrimp.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7a4bd034-28af-4792-9e07-6aa2d3bbbcad_300x300.jpg?v=1645128114'
    },
    {
        'id': 151,
        'link': 'https://gimsap.ca/collections/all/products/black-rice-4lbs',
        'name': 'Black rice 4lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p>You know what they say about black rice: it's like a superfood. The dark color is due to the pigment anthocyanin, which is also responsible for the deep red and purple colors in blueberries, grapes, and other fruits. This type of rice is higher in fiber, antioxidants, and protein than other types of rice.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at1.51.46PM_7b768f4f-d6b2-41b0-a47a-f9793ae5cf8c_300x300.png?v=1647546939'
    },
    {
        'id': 152,
        'link': 'https://gimsap.ca/collections/all/products/black-rice-8lb',
        'name': 'Black Rice 8lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $84.00',
        'description': '<p>The aroma of this rice is out of this world. It is a highly nutritious and tasty food, made with a blend of long-grain rice and black rice. The product is a mix of the health benefits of brown rice and the taste of black rice. The product is made in California and is GMO-free.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_259ae71c-cd1e-4316-985d-035d816895ba_300x300.jpg?v=1645128124'
    },
    {
        'id': 153,
        'link': 'https://gimsap.ca/collections/all/products/black-seed-oil-4fl-oz',
        'name': 'Black Seed Oil 4fl Oz',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Black Seed Oil is a natural remedy that is said to cure many ailments. It is said to be used to reduce inflammation, ease allergies, treat diabetes, and lower cholesterol. It is also used to help with weight loss, which is due to the high levels of Omega-3 and Omega-6. It is also said to be a natural antidepressant.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_acdb296a-db0a-46f3-b425-3d6279c1e65c_300x300.jpg?v=1645128157'
    },
    {
        'id': 154,
        'link': 'https://gimsap.ca/collections/all/products/black-soap',
        'name': 'Black Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': "<p>The soap is made with the best African Shea Butter and the purest of essential oils.&nbsp; The soap is handmade, meaning that the ingredients are combined by hand, using traditional methods. It's made with pure, natural ingredients that have been used for centuries in Africa.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_661af9d2-e446-47e8-a945-f4a5e04d5584_300x300.jpg?v=1645128132'
    },
    {
        'id': 155,
        'link': 'https://gimsap.ca/collections/all/products/black-soap-big-paper-wrapped',
        'name': 'Black Soap (Big) paper wrapped',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.50',
        'description': '<p>For people with dry skin or sensitive skin, this is the soap for you. It is made from natural ingredients that are known to moisturize and soothe the skin. This black soap is made with coconut oil, palm oil, and shea butter. These ingredients will help to keep your skin looking fresh and healthy.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b31b2602-0af1-4e81-b7e8-d23040f8a675_300x300.jpg?v=1645128154'
    },
    {
        'id': 156,
        'link': 'https://gimsap.ca/collections/all/products/black-soap-box',
        'name': 'Black Soap (Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Black soap is made with the saponified oils of plantain, cocoa pod, and palm oil. This soap is ideal for those with dry skin and is made with a base of water, palm oil, and cocoa pod.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e41884d5-b3b2-4a59-a60c-fa7d9ec19ee3_300x300.jpg?v=1645128151'
    },
    {
        'id': 157,
        'link': 'https://gimsap.ca/collections/all/products/black-soap-medium',
        'name': 'Black Soap (medium)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Black soap is a handmade soap made from palm oil, cocoa pod ash, and water. The soap is made in the old tradition of African black soap making. Black soap is made from palm oil, cocoa pod ash, and water.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0537c144-f55e-4321-b267-3bb231c92bdc_300x300.jpg?v=1645128153'
    },
    {
        'id': 158,
        'link': 'https://gimsap.ca/collections/all/products/black-turtle-beans-lb',
        'name': 'Black Turtle Beans /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>These beans are an excellent source of protein, dietary fiber, and other nutrients. They can be used in soups, salads, and a variety of other dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_321ed69d-c206-4b72-a176-c0cb957117f1_300x300.jpg?v=1645128150'
    },
    {
        'id': 159,
        'link': 'https://gimsap.ca/collections/all/products/black-turtle-beans-50lb',
        'name': 'Black Turtle Beans 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>A package of dried black turtle beans for your cooking pleasure. These beans are rich in flavor and make a delicious side dish or soup. They are a good source of protein and dietary fiber. They are also rich in iron, calcium, and potassium.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2075aa3b-7865-4d6e-892d-1601f60bc78a_300x300.jpg?v=1645128149'
    },
    {
        'id': 160,
        'link': 'https://gimsap.ca/collections/all/products/bleached-palm-oil-1l',
        'name': 'Bleached Palm Oil 1L',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Bleached Palm Oil is a common oil used in cooking. It is a versatile product that can be used for frying, as a spread, or in desserts. It is also a healthier alternative to other oils. It is low in saturated fat and is an excellent source of Vitamin E. This product is made from sustainable palm oil.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at1.41.35PM_300x300.png?v=1647546140'
    },
    {
        'id': 161,
        'link': 'https://gimsap.ca/collections/all/products/bleached-palm-oil-2l',
        'name': 'Bleached Palm Oil 2L',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Bleached Palm Oil is a common oil used in cooking. It is a versatile product that can be used for frying, as a spread, or in desserts. It is also a healthier alternative to other oils. It is low in saturated fat and is an excellent source of Vitamin E. This product is made from sustainable palm oil.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d81f3d33-02c9-49ce-9a7e-6c709e790032_300x300.jpg?v=1645128168'
    },
    {
        'id': 162,
        'link': 'https://gimsap.ca/collections/all/products/blue-band-900g',
        'name': 'Blue Band (900g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p><span>It&nbsp;is perfect for spreading on toast or making the perfect grilled cheese sandwich. This spreadable fat will give your food a boost of flavor, and make it so much easier to eat.</span></p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_75dfc7d1-aa43-4cc1-bc2e-6c40409f294a_300x300.jpg?v=1645128147'
    },
    {
        'id': 163,
        'link': 'https://gimsap.ca/collections/all/products/blue-band-900g-box',
        'name': 'Blue Band (900g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $160.00',
        'description': '<p><span>It&nbsp;is perfect for spreading on toast or making the perfect grilled cheese sandwich. This spreadable fat will give your food a boost of flavor, and make it so much easier to eat.</span></p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a3d5bcd1-37cd-443f-8046-4a567b29c40f_300x300.jpg?v=1645128146'
    },
    {
        'id': 164,
        'link': 'https://gimsap.ca/collections/all/products/blue-band-450g',
        'name': 'Blue Band 450g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p><meta charset="utf-8"><span>It&nbsp;is perfect for spreading on toast or making the perfect grilled cheese sandwich. This spreadable fat will give your food a boost of flavor, and make it so much easier to eat.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_84a18713-583f-439a-a8f8-7bdb130aac96_300x300.jpg?v=1645128141'
    },
    {
        'id': 165,
        'link': 'https://gimsap.ca/collections/all/products/blue-band-magarine',
        'name': 'Blue Band Magarine',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>It contains only natural ingredients and is cholesterol free. Magarine can be used in any recipe that calls for butter, and is perfect for spreading on toast or making the perfect grilled cheese sandwich. This spreadable fat will give your food a boost of flavor, and make it so much easier to eat.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_541a8183-6929-4a5a-a534-5cb6486d5d9e_300x300.jpg?v=1645128130'
    },
    {
        'id': 166,
        'link': 'https://gimsap.ca/collections/all/products/bobolo',
        'name': 'bobolo',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p><meta charset="utf-8">Bobolo<span>&nbsp;(a delicious cassava-based side dish that hails from Cameroon) is filling and incredibly satisfying when paired with braised fish, spicy stews, or truly anything you throw at it.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/OIP_b456e667-a38f-4357-b8df-148098714561_300x300.jpg?v=1647544261'
    },
    {
        'id': 167,
        'link': 'https://gimsap.ca/collections/all/products/bobolo-small-benedicta',
        'name': 'Bobolo small (Benedicta)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<meta charset="utf-8">Bobolo<span data-mce-fragment="1">&nbsp;(a delicious cassava-based side dish that hails from Cameroon) is filling and incredibly satisfying when paired with braised fish, spicy stews, or truly anything you throw at it.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ad4d3b1f-8ba0-43df-82bf-6280d64b77c9_300x300.jpg?v=1645128138'
    },
    {
        'id': 168,
        'link': 'https://gimsap.ca/collections/all/products/bone-in-beef',
        'name': 'Bone-in Beef',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.50',
        'description': '<p>Bold Flavor. Real Flavor. Bone-in Beef is a juicy, rich, and succulent cut of meat that is slow-roasted for hours. Each cut is packed with flavor and is an excellent addition to any meal. Bone-in Beef is perfect for grilling, slow-cooking, or even pan-searing. When you’re in the mood for something hearty and delicious, this is the cut for you.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b8100adb-619e-4805-b423-7be87478ff81_300x300.jpg?v=1645128113'
    },
    {
        'id': 169,
        'link': 'https://gimsap.ca/collections/all/products/bone-in-stockfish-bits-merex-12oz',
        'name': 'Bone-in Stockfish Bits Merex 12oz',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.50',
        'description': '<p>The product is a 12oz. bag of the dry and flaky bits of the fish. The fish is dried and flaky and is an excellent source of protein. The product is best served with a soup or a stew.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_85be2791-e992-43af-9e83-2dc03a0d42ee_300x300.jpg?v=1645128116'
    },
    {
        'id': 170,
        'link': 'https://gimsap.ca/collections/all/products/boned-stockfish-special',
        'name': 'Boned Stockfish (Special)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Boned Stockfish is a lean, firm, and delicious type of fish that is a healthy and inexpensive option for those looking to cut down on their intake of saturated fats. Boned Stockfish is a lean, firm, and delicious type of fish that is a healthy and inexpensive option for those looking to cut down on their intake of saturated fats. Boned Stockfish is available in bulk for those who want to buy in bulk, or in small packages for those who are looking for a smaller purchase.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 171,
        'link': 'https://gimsap.ca/collections/all/products/bonfi-natural-wig-shine-oil',
        'name': 'Bonfi Natural Wig Shine oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>Bonfi Natural Wig Shine oil is an organic, natural product made with pure jojoba oil and organic herbs to nourish and protect your wig. It’s lightweight and non-greasy, with a pleasant fragrance that won’t interfere with your hair. It can be used on all types of hair, including wigs, weaves, extensions, and braids.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_154027fa-aa92-46ac-8a44-eb165196466f_300x300.jpg?v=1645128129'
    },
    {
        'id': 172,
        'link': 'https://gimsap.ca/collections/all/products/bournvita-1kg',
        'name': 'Bournvita (1Kg)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.50',
        'description': '<p><meta charset="utf-8"><span>Bournvita is a nutritious drink mix, originally created in India. It is made from cocoa, wheat flour, malt extract, and sugar. Bournvita is known for its use of wheat flour and malt extract, which give it a sweet flavor. Bournvita is a good source of vitamin B12, which is often difficult to find in the diet.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_aa58d66a-d286-4816-8b69-ed49e912176a_300x300.jpg?v=1645128148'
    },
    {
        'id': 173,
        'link': 'https://gimsap.ca/collections/all/products/bournvita-1kg-box',
        'name': 'Bournvita (1Kg) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>For those looking for a delicious way to start their day, this Bournvita 1kg box is the perfect way to get started. The box includes 10 packets of the original flavor Bournvita, which is a great way to give yourself a boost of energy before you head out for the day. With just a spoonful of this Bournvita, you will be ready to tackle your day. Bournvita is made with milk and malt extract, which provides a delicious and refreshing taste. Bournvita is not only tasty, but it is also nutritious, with the added vitamins and minerals to help keep you healthy.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_66b0835c-8abc-4eaa-a1e3-f3e6b59f0c64_300x300.jpg?v=1645128167'
    },
    {
        'id': 174,
        'link': 'https://gimsap.ca/collections/all/products/bournvita-500g',
        'name': 'Bournvita 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>Bournvita is a nutritious drink mix, originally created in India. It is made from cocoa, wheat flour, malt extract, and sugar. Bournvita is known for its use of wheat flour and malt extract, which give it a sweet flavor. Bournvita is a good source of vitamin B12, which is often difficult to find in the diet.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_559cca82-40d7-4b80-810a-183cedc946d9_300x300.jpg?v=1645128133'
    },
    {
        'id': 175,
        'link': 'https://gimsap.ca/collections/all/products/box-2lb-olaola-plantain-flour-20',
        'name': 'Box 2lb Olaola Plantain Flour (20)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': '<p>Olaola Plantain Flour is a gluten-free, all-natural flour made from the finest plantains in the world. This flour is the perfect replacement for wheat flour in baking. The flour is also great for pancakes, waffles, and crepes. It is a low-glycemic index flour that will not spike your blood sugar levels. Plantains are a healthier alternative to wheat, corn, and rice flours. Olaola Plantain Flour is gluten-free, vegan, kosher, and contains no artificial ingredients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_70ecac98-9157-4086-b6c3-fc8e61862571_300x300.jpg?v=1645129893'
    },
    {
        'id': 176,
        'link': 'https://gimsap.ca/collections/all/products/box-ghana-fresh-garden-egg',
        'name': 'Box Ghana Fresh Garden Egg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>Our eggs are a simple, wholesome, and nutritious source of protein. Known for its sweet and biter taste that goes well with stew.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_eb285a5f-07f0-437c-9ecd-3f088249ea97_300x300.jpg?v=1645129885'
    },
    {
        'id': 177,
        'link': 'https://gimsap.ca/collections/all/products/box-instant-honeyed-ginger-drink',
        'name': 'Box Instant Honeyed Ginger Drink',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': '<p>Box Instant Honeyed Ginger Drink is a hot drink mix with ginger and honey. This product can be enjoyed as a warm drink on a cold day or as a cold drink on a hot day. It is a refreshing drink that will bring warmth to your soul. This drink mix can be prepared in just minutes. Simply add hot water and stir. Enjoy Box Instant Honeyed Ginger Drink for breakfast, after dinner, or as a snack. This drink mix is gluten-free, vegan, and kosher. It can be enjoyed by the whole family.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f116e832-a5d8-434d-9a7e-fa0b41a676f4_300x300.jpg?v=1645129889'
    },
    {
        'id': 178,
        'link': 'https://gimsap.ca/collections/all/products/box-iyan-ado-10lbs-x4',
        'name': 'Box Iyan Ado (10lbs x4)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $105.00',
        'description': '<p><meta charset="utf-8"><span>Pounded yam in powder form.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_46f3bbee-3cc9-42ba-95a0-c10ebecc1d1d_300x300.jpg?v=1645129896'
    },
    {
        'id': 179,
        'link': 'https://gimsap.ca/collections/all/products/box-iyan-ado-2lbs-x20',
        'name': 'Box Iyan Ado (2lbs x20)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $105.00',
        'description': '<p>Pounded yam in powder form.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7322c6bd-c31c-4e4f-9971-526853402502_300x300.jpg?v=1645129894'
    },
    {
        'id': 180,
        'link': 'https://gimsap.ca/collections/all/products/box-iyan-ado-4lbs-x10',
        'name': 'Box Iyan Ado (4lbs x10)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $105.00',
        'description': '<p>This can be&nbsp;served with a mixture of vegetables such as onions, tomatoes, and peppers.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_62fa3bd5-413c-408a-b427-3d32579a3162_300x300.jpg?v=1645129895'
    },
    {
        'id': 181,
        'link': 'https://gimsap.ca/collections/all/products/box-white-ogi-powder-500g-graceco',
        'name': 'Box White Ogi Powder 500g (Graceco',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': '<p>Ogi is a cereal grain that is processed into a powder and used as a substitute for wheat flour. It is gluten-free and has a much lower glycemic index than wheat flour. Ogi is a good source of dietary fiber, protein, vitamins, and minerals.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4b89fe4b-4414-436f-bf7b-25f505a2d413_300x300.jpg?v=1645129887'
    },
    {
        'id': 182,
        'link': 'https://gimsap.ca/collections/all/products/box-whole-cassava-leaves',
        'name': 'Box whole cassava leaves',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<p>They are a nutritious and filling food, which is traditionally used in Brazilian cuisine. The leaves are dried, boiled, and then fried to create a crunchy exterior. When cooked, the leaves are soft and tender, and can be eaten with a variety of dishes. They are gluten-free and low in calories.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0f972eb3-3cf1-49ff-a370-89a0fb428376_300x300.jpg?v=1645129865'
    },
    {
        'id': 183,
        'link': 'https://gimsap.ca/collections/all/products/br-george-honey-350ml',
        'name': 'Br. George Honey 350mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.50',
        'description': '<p>Br. George Honey is a thick, fragrant honey that is great for cooking, baking, and adding to your tea.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1acfc1bd-11b6-4951-96cd-2a527591d8a5_300x300.jpg?v=1645129911'
    },
    {
        'id': 184,
        'link': 'https://gimsap.ca/collections/all/products/br-george-honey-8x350ml-box',
        'name': 'Br. George Honey 8x350mL Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p>Enjoy this classic favorite from the honey man. George's honey is sourced from the Central Valley of California, with the help of bees. Made from pure California honey, this is a perfect addition to any family's pantry. Enjoy the rich taste of the Central Valley with a subtle sweet note that is perfect for a wide variety of dishes.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_912394a8-18ec-4d24-a601-b71af19bd0f3_300x300.jpg?v=1645129910'
    },
    {
        'id': 185,
        'link': 'https://gimsap.ca/collections/all/products/brain',
        'name': 'Brain',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 186,
        'link': 'https://gimsap.ca/collections/all/products/braziilian-wool-80g',
        'name': 'Braziilian wool 80g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>The product is a beautiful, luxurious, and heavy-weight wool yarn that comes in a gorgeous selection of colors.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2d1d2658-4924-42e8-a2f3-687441fafe18_300x300.jpg?v=1645129907'
    },
    {
        'id': 187,
        'link': 'https://gimsap.ca/collections/all/products/brazil-nut-oil',
        'name': 'Brazil Nut Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p>The nut oil is extracted from the Brazil nut, which is native to the Amazonian rainforest. The oil is rich in healthy fats, including Omega-3 and Omega-6. Brazil Nut Oil is a light-textured oil that is easily absorbed by the skin. It has a slightly nutty aroma and is a good source of Vitamin E.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b4f38094-7041-4db3-afa6-26973c34d484_300x300.jpg?v=1645129891'
    },
    {
        'id': 188,
        'link': 'https://gimsap.ca/collections/all/products/brazils-shelled-raw-box-5kg',
        'name': 'Brazils shelled raw box 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Brazils are large, oval shaped nuts with a soft, sweet and buttery taste. These Brazil nuts are shelled, and have a 5kg bag.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e18356f8-cff4-408f-9b52-e6681d632e88_300x300.jpg?v=1645129908'
    },
    {
        'id': 189,
        'link': 'https://gimsap.ca/collections/all/products/brazils-shelled-raw-per-lb',
        'name': 'Brazils shelled raw per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Brazil nuts are an excellent source of selenium, an important mineral for our immune system. Brazil nuts are also high in protein, fiber, vitamin E, and magnesium. Brazil nuts are an excellent source of selenium, an important mineral for our immune system.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_011c47b8-48a0-4267-9fa2-a36c7936977d_300x300.jpg?v=1645129909'
    },
    {
        'id': 190,
        'link': 'https://gimsap.ca/collections/all/products/bread-agege-bread',
        'name': 'Bread (Agege Bread)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': "<p>You've never had bread like this before. Our new Agege Bread is so good, you'll think you're eating the best bakery in the world. We use the best ingredients to make the perfect loaf of bread. All you have to do is get a slice of our delicious bread and you'll be hooked. You can't go wrong with our Agege Bread.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_46f3b580-558f-4d7c-8eee-7701b2bc643d_300x300.jpg?v=1645129875'
    },
    {
        'id': 191,
        'link': 'https://gimsap.ca/collections/all/products/broken-beans-4lb',
        'name': 'Broken Beans 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Broken Beans are dried, roasted beans that have been shattered into small pieces. These beans are perfect for use in soups, chili, and casseroles. Broken Beans are a gluten-free and vegan-friendly alternative to whole beans.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b38ce232-6167-4d78-80a2-47b1a1d43036_300x300.jpg?v=1645129877'
    },
    {
        'id': 192,
        'link': 'https://gimsap.ca/collections/all/products/broken-corn-4lb',
        'name': 'Broken corn 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This is a broken corn product that is a great way to mix up your dishes. The product is 4lbs and will help you get creative with your recipes. This is a great product for those who are looking for something new to try.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_377f38e5-f8a3-415d-a562-33fc7c0b94f1_300x300.jpg?v=1645129874'
    },
    {
        'id': 193,
        'link': 'https://gimsap.ca/collections/all/products/broken-yam-box',
        'name': 'Broken Yam Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<span>Our broken yams are perfect for adding to your favorite dish. They are peeled and cut into small pieces so they are easier to cook. The yams are sweet and moist with a fluffy texture. They have a light, natural brown color and have a long shelf life.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_21227a4d-54f1-417b-a0ad-76a888f135ef_300x300.jpg?v=1645129871'
    },
    {
        'id': 194,
        'link': 'https://gimsap.ca/collections/all/products/broken-yam-per-lb',
        'name': 'Broken Yam per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.00',
        'description': '<p>Our broken yams are perfect for adding to your favorite dish. They are peeled and cut into small pieces so they are easier to cook. The yams are sweet and moist with a fluffy texture. They have a light, natural brown color and have a long shelf life. The Broken Yam per lb is a delicious, sweet and moist yam that is easy to cook.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f605ed6f-fee9-4575-9bd5-f4133d04616b_300x300.jpg?v=1645129903'
    },
    {
        'id': 195,
        'link': 'https://gimsap.ca/collections/all/products/broom-large',
        'name': 'Broom (Large)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': "<p>Brooms are a necessary tool for anyone who does any type of housekeeping. They are a vital part of keeping your home clean and tidy. This broom is extra large, perfect for sweeping large areas quickly. It's made of sturdy, natural bristles that won't break easily and is double-sided for maximum cleaning power. This broom will help you keep your home clean and free of dirt and dust.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d15a462e-8c30-40a3-b279-e16acebc4bdb_300x300.jpg?v=1645129879'
    },
    {
        'id': 196,
        'link': 'https://gimsap.ca/collections/all/products/broom-small',
        'name': 'Broom (Small)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>The small broom is great for cleaning tight spaces, like under the kitchen sink.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/R_4e8ea500-14c9-4be2-9826-112dfd560983_300x300.jpg?v=1647543070'
    },
    {
        'id': 197,
        'link': 'https://gimsap.ca/collections/all/products/brown-beans',
        'name': 'Brown Beans',
        'price': 'From $13.50',
        'description': '<p>Brown (or Drum) Beans are dark brown and larger than honey beans. Our beans have been picked clean and are free from chemical preservatives. Ethically sourced.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/1553702096_3_large_1d4dd249-3d71-461b-97c8-2e534da73c77_300x300.jpg?v=1606140593'
    },
    {
        'id': 198,
        'link': 'https://gimsap.ca/collections/all/products/brown-ogi-500g-todaj',
        'name': 'Brown Ogi 500g (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><meta charset="utf-8"><span>Ogi also known as corn flour is a finely powdered white starch extracted from maize kernels. It is used to prepare Pap which is similar to Custard but has a unique sour taste.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_beedd586-0d6e-4ff2-b0f8-0a607662173a_300x300.jpg?v=1645129914'
    },
    {
        'id': 199,
        'link': 'https://gimsap.ca/collections/all/products/brown-rice-long-grain-lb',
        'name': 'Brown Rice (long grain) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.40',
        'description': '<p>There are many benefits to choosing brown rice over white rice. Brown rice is more nutritious, contains more fiber, and has a lower glycemic index. Brown rice is also lower in calories, which is perfect for those looking to lose weight. Brown rice is also a healthier option for those with diabetes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ca918140-3c09-48ec-82a5-3a5372878eba_300x300.jpg?v=1645129898'
    },
    {
        'id': 200,
        'link': 'https://gimsap.ca/collections/all/products/brown-rice-long-grain-10-kg',
        'name': 'Brown Rice (long grain) 10 Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $32.50',
        'description': '<p>Brown rice is a whole grain that is rich in protein, fiber, and vitamins. Brown rice is a good source of B vitamins, magnesium, and manganese. This rice is long grain and has a nutty flavor.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_65247e44-e58a-421e-b4e5-29fa0fc0dbaa_300x300.jpg?v=1645129904'
    },
    {
        'id': 201,
        'link': 'https://gimsap.ca/collections/all/products/browning-caramel-142-ml',
        'name': 'Browning Caramel 142 ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': "<p>A liquid-caramel sauce with a buttery, sweet flavor and a light golden color. It's made with high-quality ingredients and is an excellent addition to any dessert or coffee drink. It's also great for dipping fruit, pretzels, and even ice cream.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_416b997b-6103-4989-9e82-57046c5e51d6_300x300.jpg?v=1645129866'
    },
    {
        'id': 202,
        'link': 'https://gimsap.ca/collections/all/products/brush-rollers',
        'name': 'Brush Rollers',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>With the latest in hair technology, Brush Rollers are a necessary tool for the perfect blowout. The brush is designed to help reduce frizz and provide smoother results.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d686b1e7-04d1-4bfa-8134-eb47782c76ce_300x300.jpg?v=1645129878'
    },
    {
        'id': 203,
        'link': 'https://gimsap.ca/collections/all/products/bubble-round-xl4-pink-tone-6-pk',
        'name': 'Bubble Round XL4 Pink Tone [6/pk]',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p><meta charset="utf-8"><span>Accessories for the hair.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6a6d7c6f-ae2b-406d-9be5-156fb50204a8_300x300.jpg?v=1645129915'
    },
    {
        'id': 204,
        'link': 'https://gimsap.ca/collections/all/products/bubble-square-mix-8-pk-red-blue-white-brown',
        'name': 'Bubble Square Mix [8/pk] Red Blue White Brown',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p><meta charset="utf-8"><span>Accessories for the hair.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 205,
        'link': 'https://gimsap.ca/collections/all/products/bubble-square-sq11-l-pink-white-8-pk',
        'name': 'Bubble Square SQ11 L.Pink/White [8/pk]',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>Accessories for the hair.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dd7b24b0-0483-40b4-81b5-145a7044da4b_300x300.jpg?v=1645129917'
    },
    {
        'id': 206,
        'link': 'https://gimsap.ca/collections/all/products/bubble-square-sq15-brown-mix-8-pk',
        'name': 'Bubble Square SQ15 Brown Mix [8/pk]',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>Bubble Square SQ15 Brown Mix is a pack of 8 brown square bubble strings.&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dc38b695-bbb2-459b-963e-3364d37f0c1c_300x300.jpg?v=1645129918'
    },
    {
        'id': 207,
        'link': 'https://gimsap.ca/collections/all/products/bubble-square-sq16-crystal-pink-clear-8-pk',
        'name': 'Bubble Square SQ16 Crystal Pink Clear [8/pk]',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p><meta charset="utf-8"><span>Accessories for the hair.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_03a1e385-1392-4d7e-ae02-e2a00111d2ad_300x300.jpg?v=1645129919'
    },
    {
        'id': 208,
        'link': 'https://gimsap.ca/collections/all/products/buenas-coconut-gel-340g-24-box',
        'name': 'Buenas Coconut Gel  340g  (24/box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Buenas Coconut Gel is a coconut-based gel that can be used as a replacement for butter or oil in cooking. The product is vegan, gluten-free, and kosher. Buenas Coconut Gel is made from 100% coconut milk and can be used as a spread, a cooking oil, or as a vegan substitute for butter. The product is rich in vitamins and minerals, and is also cholesterol-free. Buenas Coconut Gel has a smooth texture and a light coconut flavor.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_58420e0c-dd08-452d-a06f-c057413e6a53_300x300.jpg?v=1645129873'
    },
    {
        'id': 209,
        'link': 'https://gimsap.ca/collections/all/products/buenas-coconut-sport-24-x-340g',
        'name': 'Buenas Coconut Sport 24 x 340g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Buenas Coconut Sport is a tasty, nutritious, and convenient way to refuel and recharge during your workout. This easy-to-digest and healthy food is a great choice for anyone who is on the go and wants to get the most out of their workout. This convenient and nutritious coconut drink mix is the perfect snack for anyone who is on the go.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4eb8e290-0cc6-4157-ae13-20e9335626ba_300x300.jpg?v=1645129872'
    },
    {
        'id': 210,
        'link': 'https://gimsap.ca/collections/all/products/buffalo-chicken-seasoning',
        'name': 'buffalo chicken seasoning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>A hearty, hot, and spicy buffalo chicken seasoning. Great for flavoring chicken, potatoes, macaroni, and more. Made with all natural ingredients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b5953318-da5e-48fd-b34a-bf1be48ab551_300x300.jpg?v=1645129956'
    },
    {
        'id': 211,
        'link': 'https://gimsap.ca/collections/all/products/bulacan-coconut-gel-in-syrup-340g-24-box',
        'name': 'Bulacan Coconut Gel in Syrup 340g  (24/box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Bulacan Coconut Gel in Syrup 340g (24/box) is a product that can be used as a substitute for dairy cream in desserts, ice cream, and other recipes. It has a rich and creamy taste and is derived from fresh coconut milk.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b0a8c839-fa24-4a78-9964-342b20e2549d_300x300.jpg?v=1645129961'
    },
    {
        'id': 212,
        'link': 'https://gimsap.ca/collections/all/products/bulgur-wheat-coarse-10-kg',
        'name': 'Bulgur Wheat coarse 10 kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<p>Bulgur wheat is a grain that is often found in Middle Eastern cuisine. Bulgur wheat is made from wheat kernels that have been boiled, dried, and cracked. The wheat is then parboiled with hot water and sun-dried. Bulgur wheat is an excellent substitute for rice and pasta, and can be used in a variety of dishes. Bulgur wheat is also a great source of fiber, protein, and other essential nutrients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Tropical_Sun_Bulgur_Wheat_500g_Packet_1200x1200_d64d66f3-9672-4474-bb3d-4b81455d26eb_300x300.jpg?v=1647541879'
    },
    {
        'id': 213,
        'link': 'https://gimsap.ca/collections/all/products/bulgur-wheat-coarse-per-lb',
        'name': 'Bulgur Wheat coarse per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.50',
        'description': '<p>Bulgur wheat is a whole grain that is often used in Middle Eastern dishes. Bulgur wheat is the dried, crushed form of wheat that has been parboiled and dried. Bulgur wheat is a great substitute for rice or couscous, as it is high in fiber and low in calories. Bulgur wheat is also a good source of magnesium, zinc, and iron.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_57b7fd4a-327d-4c12-854b-b04dc1eda46d_300x300.jpg?v=1645129963'
    },
    {
        'id': 214,
        'link': 'https://gimsap.ca/collections/all/products/bunge-5lb',
        'name': 'Bunge 5lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': "<p>Premium Quality, Roasted, Shelled, Unsalted Pistachios Bunge 5lb. Premium Quality, Roasted, Shelled, Unsalted Pistachios are grown in California. Bunge's pistachios are roasted in their shells, then peeled to ensure the best quality. They are shelled and then unsalted. The product is available in a 5lb. bag.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b277fb1f-d917-4740-8608-ab68506de663_300x300.jpg?v=1645129966'
    },
    {
        'id': 215,
        'link': 'https://gimsap.ca/collections/all/products/bunge-corn-meal-50lb',
        'name': 'Bunge Corn Meal 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': "<p>If you're looking for a dependable product to cook up all your favorite dishes, then you'll want to try our Bunge Corn Meal. Made from 100% whole grain corn, this all-purpose flour is perfect for cooking up traditional favorites like cornbread, muffins, and more. We carry it in 50lb bags for a great value and it's USDA certified for quality.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_45201b78-2e5e-4d71-b86d-93c0edb918a0_300x300.jpg?v=1645129962'
    },
    {
        'id': 216,
        'link': 'https://gimsap.ca/collections/all/products/burger-peanut-snack-50g',
        'name': 'Burger Peanut Snack (50g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.50',
        'description': '<p>The perfect protein-packed peanut snack for any time of day, Burger Peanut Snack is made with delicious, wholesome ingredients. This snack is gluten-free, soy-free, and contains no trans fats. With the perfect balance of peanuts and spices, this peanut snack is sure to be a crowd pleaser.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b3234432-f7c6-48da-9db8-54354abf4cd3_300x300.jpg?v=1645129965'
    },
    {
        'id': 217,
        'link': 'https://gimsap.ca/collections/all/products/burger-peanut-snack-box-144x50g',
        'name': 'Burger Peanut Snack Box (144x50g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Burger Peanut Snack Box is a product that has been designed to be a convenient and delicious snack. This product is perfect for those who are looking for a satisfying meal that is both filling and affordable. The Burger Peanut Snack Box is available in a variety of flavors, including; Original, Sweet Chili, and Teriyaki. The snack box is also high in protein and contains less than five grams of sugar. This product is gluten-free, kosher, and has no added MSG. The ingredients are also free of trans fats and high in fiber. With this snack box, you can enjoy a tasty and healthy meal on the go.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2c1cf374-0e61-4798-bc75-dc7ffb1f02ad_300x300.jpg?v=1645129969'
    },
    {
        'id': 218,
        'link': 'https://gimsap.ca/collections/all/products/farm-goat-burnt-lb',
        'name': 'Burnt Farm Goat Meat',
        'price': 'From $15.00',
        'description': '<p>Mouthwatering&nbsp;goat meat with burnt skin.&nbsp;Cut into ready to cook chunks.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/goat-meat-skin-frozen_300x300.jpg?v=1646868908'
    },
    {
        'id': 219,
        'link': 'https://gimsap.ca/collections/all/products/butter-mint',
        'name': 'Butter Mint',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': "<p>If you love the flavor of buttery popcorn, but you're looking for a more refreshing, minty twist, then you need to try Butter Mint. With a buttery and buttery taste, this is a light and refreshing way to enjoy the classic flavors of popcorn. If you're looking for a fresh and unique popcorn experience, then Butter Mint is the perfect snack for you.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4d968170-4a4b-49bb-ab5d-e387fda6f470_300x300.jpg?v=1645129964'
    },
    {
        'id': 220,
        'link': 'https://gimsap.ca/collections/all/products/butter-mint-box-26x',
        'name': 'Butter Mint Box (26x)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>We all know that sometimes it can be hard to find the perfect gift for a loved one. Why not try Butter Mint Boxes? This is a pack of 26 boxes of individually wrapped Butter Mints. They are great for giving to friends, family, coworkers, and more.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a7e7966e-1cc7-4dc3-8a5b-3574c95f1dc2_300x300.jpg?v=1645129967'
    },
    {
        'id': 221,
        'link': 'https://gimsap.ca/collections/all/products/cabin-biscuit',
        'name': 'Cabin Biscuit',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': "<p>The smell of fresh baked biscuits fills the air in the morning and reminds you of simpler times. These days, we all have our own breakfast habits, but there's still a time and place for a classic morning meal. Bring the comfort of home to your morning routine with Cabin Biscuit.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8a51a08b-5d49-4a1c-94b1-3c83e81b5956_300x300.jpg?v=1645133466'
    },
    {
        'id': 222,
        'link': 'https://gimsap.ca/collections/all/products/calamansi-juice',
        'name': 'Calamansi juice',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $28.03',
        'description': '<p>Calamansi juice is a citrus fruit juice with a tart and tangy flavor. Calamansi juice is a perfect drink for the morning or any time of day. This drink is a great way to get your daily dose of vitamin C and has no added sugar. Calamansi juice is also a healthy substitute for soda. Calamansi juice is available in four delicious flavors: lime, orange, grapefruit, and cherry.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fd9c90a2-3387-4b3e-8b88-e2e05849ae8c_300x300.jpg?v=1645133468'
    },
    {
        'id': 223,
        'link': 'https://gimsap.ca/collections/all/products/callaloo-in-brine',
        'name': 'callaloo in brine',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>&nbsp;This delicious Caribbean dish is now available in a new way! Introducing callaloo in brine. Callaloo in brine is the perfect meal for your next barbecue. The flavor of this dish is reminiscent of the islands. The rich flavor of the callaloo will delight your taste buds. You will find that this dish is perfect for any occasion.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4bb1dfdd-ea8f-4b58-994b-b592e9f49a24_300x300.jpg?v=1645133469'
    },
    {
        'id': 224,
        'link': 'https://gimsap.ca/collections/all/products/calrose-rice-nupak-2kg',
        'name': 'Calrose Rice Nupak 2kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This product is a bag of Calrose Rice. It is 2kg, which is a large bag. It is also made from the most common type of rice in the United States. Calrose Rice is grown in California and it is a medium grain rice. It is brown in color, which is the color that most people associate with rice. Calrose Rice is a very popular type of rice and it is often used in many dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3c94f2ca-4c8e-463f-8a18-193a94124553_300x300.jpg?v=1645133470'
    },
    {
        'id': 225,
        'link': 'https://gimsap.ca/collections/all/products/calve-mayonnaise-450g-x12',
        'name': 'Calve Mayonnaise 450g x12',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Calve Mayonnaise is a rich, creamy mayonnaise that is a perfect accompaniment to sandwiches, burgers, salads, or any other dishes that need a flavorful, creamy sauce. It is made with the finest ingredients including a blend of virgin oils and is gluten-free.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d88526f3-d460-4a90-955f-0b41b4233166_300x300.jpg?v=1645133471'
    },
    {
        'id': 226,
        'link': 'https://gimsap.ca/collections/all/products/cameroon-pepper',
        'name': 'cameroon pepper',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Cameroon pepper is a type of African pepper. It is a very hot pepper with a fruity flavor. It has a bright red color and can be used in dishes to add a spicy, fruity flavor. It is often used in recipes that call for black pepper, such as chili and other dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_da947b9b-9999-4e99-b638-9132ab115921_300x300.jpg?v=1645133472'
    },
    {
        'id': 227,
        'link': 'https://gimsap.ca/collections/all/products/cameroon-pepper-medium-bowl',
        'name': 'Cameroon Pepper Medium Bowl',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': "<p>Cameroon Pepper Medium Bowl This Cameroon Pepper Medium Bowl is a piece of functional art for the kitchen. Made from stainless steel, this bowl is designed to withstand years of use and even a dishwasher. The bowl has a high-polish finish that will resist scratches and other wear and tear, so you can keep it looking like new for years to come. It's perfect for serving up a side of your favorite chili, or for storing small items like screws and nails. T</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 228,
        'link': 'https://gimsap.ca/collections/all/products/canada-dry-710ml',
        'name': 'Canada Dry 710ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.10',
        'description': '<p>Canada Dry is the perfect drink for any occasion. From summer BBQs to family gatherings, Canada Dry is always a crowd pleaser. It is a refreshingly light and refreshing drink with a distinctive taste that has been around for over 130 years.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d0defdc5-40c2-4ce3-b258-d6bc11f3bb15_300x300.jpg?v=1645133474'
    },
    {
        'id': 229,
        'link': 'https://gimsap.ca/collections/all/products/canton-noodles',
        'name': 'canton noodles',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.60',
        'description': '<p>Canton noodles are made from wheat flour, vegetable oil, salt, sugar, yeast, and eggs. They are traditionally served with a bowl of soup.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_df87ef83-399b-470f-b49e-232297e8d474_300x300.jpg?v=1645133475'
    },
    {
        'id': 230,
        'link': 'https://gimsap.ca/collections/all/products/cantu-argan-oil',
        'name': 'Cantu argan Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Cantu Argan Oil is a light weight and natural oil that penetrates the hair shaft to help restore and protect hair. The oil has a light and pleasant scent. The argan oil is rich in omega-6 fatty acids, linoleic acid, antioxidants, vitamin E, and phytosterols. Cantu Argan Oil can be used on wet or dry hair. Apply to the scalp and hair, then gently work the product through the hair.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c1752fdd-aef3-4f5a-bd7b-6adec83be919_300x300.jpg?v=1645133476'
    },
    {
        'id': 231,
        'link': 'https://gimsap.ca/collections/all/products/cantu-argan-oil-leave-in-conditioning-repair-cream-16oz',
        'name': 'Cantu Argan Oil Leave In Conditioning Repair Cream (16oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.50',
        'description': '<p>Cantu Argan Oil Leave In Conditioning Repair Cream is a moisturizing cream that is designed to be used on the hair to help repair dry and damaged hair. It has a creamy texture that is designed to provide the hair with hydration. It is recommended for use on hair that has been damaged by heat styling or hair treatments. It has a light and non-greasy feel that leaves the hair feeling smooth and soft.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bf15e785-e7ad-42d3-856e-8bc1cd28c196_300x300.jpg?v=1645133477'
    },
    {
        'id': 232,
        'link': 'https://gimsap.ca/collections/all/products/cantu-care-for-kids-curling-cream',
        'name': 'Cantu Care For Kids Curling Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Cantu Care For Kids Curling Cream is a cream that is designed to help make kids’ hair curl. The cream is designed to help get kids’ hair to hold the curl and to make it last longer. The cream is made with the best ingredients and is designed to be lightweight and moisturizing. The cream is designed to be easily washable and to not leave residue in the hair. The product is also designed to not have a greasy feel.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6005a135-1fcd-4b75-ba57-0a5bd1a59838_300x300.jpg?v=1645133478'
    },
    {
        'id': 233,
        'link': 'https://gimsap.ca/collections/all/products/cantu-coconut-oil-shine-hold-237ml',
        'name': 'Cantu Coconut oil shine &amp; hold 237ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.50',
        'description': '<p>Cantu Coconut oil shine is a moisturizing hair care product that will provide your hair with a glossy, healthy look. It is enriched with coconut oil, an ingredient that provides your hair with an instant shine. The product is made with natural ingredients and has a fragrance that will be pleasant to most people. Cantu Coconut oil shine is suitable for all hair types and is easy to use. Simply apply the product to your hair and let it sit for a few minutes before rinsing it out.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c2608684-0ad4-4bad-bc9a-3fb171cb194b_300x300.jpg?v=1645133479'
    },
    {
        'id': 234,
        'link': 'https://gimsap.ca/collections/all/products/cantu-coil-calm',
        'name': 'Cantu Coil Calm',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Cantu Coil Calm is a deep conditioning treatment for your hair. It contains shea butter, which helps your hair become soft and shiny. It also contains castor oil, which helps your hair grow longer and thicker. The cream is free of sulfates, which will not strip your hair of its natural oils. It is safe for color-treated hair.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5af6f265-87b7-4371-981d-1eafb344ac52_300x300.jpg?v=1645133480'
    },
    {
        'id': 235,
        'link': 'https://gimsap.ca/collections/all/products/cantu-grow-strong-173g',
        'name': 'Cantu Grow  Strong 173g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>The Cantu Grow Strong collection is specifically designed to grow strong, healthy hair. The Cantu Grow Strong Conditioner is a product that restores, moisturizes, and strengthens your hair. It is a deep conditioner that you can use every day. It is safe for color treated hair and has a sweet almond scent. It is recommended for daily use on natural or chemically treated hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_be3a9c35-60ae-482f-a3c9-ba6f1fc63aef_300x300.jpg?v=1645133481'
    },
    {
        'id': 236,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter',
        'name': 'Cantu Shea Butter',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>Cantu Shea Butter is a hair care product that moisturizes and nourishes the hair. It is made with a blend of shea butter, coconut oil, and vitamin E. The product is designed to be used as a deep conditioner, moisturizer, and styling aid. Cantu Shea Butter is designed to moisturize and nourish the hair.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b3deca68-d7c6-44b7-a3ba-21e86e76f66c_300x300.jpg?v=1645133482'
    },
    {
        'id': 237,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-beard-oil',
        'name': 'Cantu Shea Butter Beard Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>It's no secret that a man's beard is the focal point of his masculinity. And while the appearance of a beard can be subjective, one thing is certain: a healthy beard needs the right kind of attention. A daily grooming routine with a high-quality beard oil is the perfect way to keep a beard looking and feeling its best. Cantu Shea Butter Beard Oil is made with pure, organic ingredients and a proprietary blend of shea butter, argan oil, and other essential oils. The oil penetrates deep into the hair follicles to help strengthen and moisturize the beard, which results in less breakage and healthier-looking facial hair. Cantu Shea Butter Beard Oil can also be used as a leave-in conditioner for softer, shinier hair.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6ca9a972-ce41-454a-9266-e62387994665_300x300.jpg?v=1645133483'
    },
    {
        'id': 238,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-daily-oil-moisturizer-13oz',
        'name': 'Cantu Shea Butter Daily Oil Moisturizer (13oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>The Cantu Shea Butter Daily Oil Moisturizer is a daily moisturizer for all hair types. It contains shea butter, which is a natural moisturizer, to help prevent dryness and protect hair from breakage. It also contains sunflower seed oil, avocado oil, and coconut oil, which help provide nutrients to the hair and scalp. The moisturizer is also fortified with vitamins A, C, and E, which are all antioxidants that help fight against free radicals. The moisturizer is available in two scents: original and lavender. This moisturizer will provide your hair with the nutrients it needs to grow healthy and strong.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_37b54bd0-1cc0-4e41-b2a6-0c0cfb8096ba_300x300.jpg?v=1645133484'
    },
    {
        'id': 239,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-leave-in-conditioningrepair-cream-16oz',
        'name': 'Cantu Shea Butter Leave in ConditioningRepair Cream (16oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>Cantu Shea Butter Leave in Conditioning Repair Cream is a leave-in conditioning cream that repairs dry, damaged hair and restores shine. This formula contains an exclusive blend of shea butter, coconut oil, and panthenol to provide a complete, deep conditioning treatment. Cantu Shea Butter Leave in Conditioning Repair Cream can be used as a daily conditioner or weekly deep conditioning treatment. It can be used on wet or dry hair and will not weigh hair down.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_82818544-5dee-4054-9a8f-25d4f67a7985_300x300.jpg?v=1645133485'
    },
    {
        'id': 240,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-moisturizing-cream-shampoo-13-5oz',
        'name': 'Cantu Shea Butter Moisturizing Cream Shampoo (13.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>The Cantu Shea Butter Moisturizing Cream Shampoo is a deep cleansing, moisturizing shampoo. This product has been formulated with an array of ingredients to provide an intensive, deep cleanse. These ingredients include a mixture of natural extracts, coconut oil, shea butter, and other ingredients to help create a healthy scalp and reduce breakage. This product is vegan and cruelty-free.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_da5fdbbb-a46a-4375-965c-62abd2b77bec_300x300.jpg?v=1645133486'
    },
    {
        'id': 241,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-natural-wave-whip-curing-mousse-8-4oz',
        'name': 'Cantu Shea Butter Natural Wave Whip Curing Mousse (8.4oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>A natural wave whip mousse that cures to a soft, touchable hold and controls frizz, Cantu Shea Butter Natural Wave Whip Curing Mousse provides natural looking definition and style. With a touch of Shea Butter, our Natural Wave Whip Curing Mousse is a must-have for every curly girl.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9bd838f7-58d6-48d7-b6a1-71ad94a3363e_300x300.jpg?v=1645133487'
    },
    {
        'id': 242,
        'link': 'https://gimsap.ca/collections/all/products/cantu-shea-butter-oil-sheen-deep-conditioning-spray-10oz',
        'name': 'Cantu Shea Butter Oil Sheen Deep Conditioning Spray (10oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': "<p>This is a deep conditioning spray that is perfect for adding moisture to the hair and scalp. It is formulated with organic shea butter and almond oil, which work to repair and restore the hair's elasticity. The oil-free formula is safe for color-treated hair and leaves the hair feeling soft and manageable. This product is ideal for all hair types, including dry, damaged, and color-treated hair.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ed4c2531-41a4-49f0-b004-efc85e4c2944_300x300.jpg?v=1645133488'
    },
    {
        'id': 243,
        'link': 'https://gimsap.ca/collections/all/products/cantu-super-shine-hair',
        'name': 'Cantu Super Shine Hair',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>The Cantu Super Shine Hair product is a product that is designed to add extra shine to dull, dry hair. It does this by adding moisturizers and proteins to the hair. The product is used by applying it to the hair and then styling as usual. The product is designed to be used on all hair types.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0daa5b11-06b3-4e38-aa07-c09955dd7a56_300x300.jpg?v=1645133489'
    },
    {
        'id': 244,
        'link': 'https://gimsap.ca/collections/all/products/care-free-curl',
        'name': 'Care Free Curl',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>Hair is your crowning glory. You wear it long, wear it short, dye it blonde, dye it red, or wear it black. Whatever you do, you want to make sure that your hair is always beautiful and manageable. However, when you wake up in the morning, your hair is a mess. No matter how many times you brush it, it just won't cooperate. That's where Care Free Curl comes in. Care Free Curl is a new and innovative product that will change the way you care for your hair. It comes in a package of ten pre-moistened pads that are individually wrapped and sealed. All you have to do is wet the pad with water and apply it to your hair. The pads are perfect for any hair type, and will make your hair look fresh and beautiful in just seconds. They're easy to use, they're inexpensive, and they're perfect for anyone who has a busy lifestyle. Care Free Curl is the perfect product for any woman who wants to make her hair look beautiful and manageable, but doesn't have the time to spend on it.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_afffde29-cb41-442b-b976-cd7627534350_300x300.jpg?v=1645133490'
    },
    {
        'id': 245,
        'link': 'https://gimsap.ca/collections/all/products/caro-light-cream',
        'name': 'Caro Light Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $29.99',
        'description': '<p>Caro Light Cream is a light moisturizer that is also perfect for use in the morning. The cream absorbs quickly into the skin and leaves a soft, silky feel. It has a non-greasy formula that is perfect for sensitive skin. It is fragrance-free and is ideal for all skin types.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b4735662-9be4-428c-bc4f-d727e33f8b32_300x300.jpg?v=1645133491'
    },
    {
        'id': 246,
        'link': 'https://gimsap.ca/collections/all/products/caro-white-corps',
        'name': 'Caro White Corps',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $29.99',
        'description': '<p>Caro White Corps, a luxury bath and body company, is committed to providing luxurious, high-quality products for women of all ages. The company offers a range of bath and body products that are 100% natural and safe for all skin types.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_85d848d6-21b0-4bd2-b159-b51a02c18174_300x300.jpg?v=1645133510'
    },
    {
        'id': 247,
        'link': 'https://gimsap.ca/collections/all/products/caro-white-lightening-oil-50ml',
        'name': 'Caro White Lightening Oil 50mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>Caro White Lightening Oil is a potent, deep-penetrating oil that is designed to fight hyperpigmentation and help reduce the appearance of dark spots. This oil will help you achieve a fairer, more even skin tone by helping to lighten dark spots and areas of discoloration. The oil is formulated with a potent blend of natural ingredients, including turmeric, orange peel, lemon peel, and papaya extract. The blend is designed to increase the skin's natural production of melanin and help reduce the appearance of dark spots. Caro White Lightening Oil is vegan, cruelty-free, and paraben-free.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a171b6b7-6e6f-47f1-ad9f-6769c6203209_300x300.jpg?v=1645133512'
    },
    {
        'id': 248,
        'link': 'https://gimsap.ca/collections/all/products/caro-white-lotion',
        'name': 'Caro White Lotion',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $29.99',
        'description': "<p>Caro White Lotion is a skin care product that was developed by a dermatologist to restore the skin's natural tone and texture. This product is specially formulated to brighten and even out skin tone, while reducing the appearance of dark spots and age spots.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5e12317d-d903-46da-9416-19220177237b_300x300.jpg?v=1645133513'
    },
    {
        'id': 249,
        'link': 'https://gimsap.ca/collections/all/products/caro-white-oil',
        'name': 'Caro white oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Caro White Oil is a natural beauty oil that is extracted from olive oil and coconut oil. This white oil is a mixture of moisturizing ingredients that are perfect for dry skin and can be used to moisturize hair. The product is 100% natural and is not tested on animals.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_67ff436a-80bd-46ee-9ada-b312a596a7c7_300x300.jpg?v=1645133514'
    },
    {
        'id': 250,
        'link': 'https://gimsap.ca/collections/all/products/caro-white-soap',
        'name': 'Caro White Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>If you are looking for a soap that can clean your skin while providing a delicate scent, then Caro White Soap is the perfect choice. This soap is a premium soap that is made with a luxurious formula that provides the user with a silky, clean feeling. This soap also has a light, refreshing scent that is perfect for everyday use. The soap is perfect for the person who is looking for a soap that is gentle on the skin and leaves them feeling refreshed.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7f8a3d6e-5124-4e4a-a479-d481d455f5a9_300x300.jpg?v=1645133515'
    },
    {
        'id': 251,
        'link': 'https://gimsap.ca/collections/all/products/carotino-cooking-oil-1-1l-35-2-oz',
        'name': 'Carotino Cooking Oil 1.1L (35.2 oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Carotino Cooking Oil is the healthier alternative to other cooking oils because it is made from pure and natural ingredients, such as palm fruit, coconut, and rice bran. The oil is then cold-pressed and filtered to remove any impurities, leaving behind a tasteless, odorless, and colorless cooking oil. It is also 100% natural and 100% cholesterol-free. This oil is also great for frying and searing, as it has a high smoke point.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f6e2308c-7ae5-42b1-98e6-036c312e0f20_300x300.jpg?v=1645133493'
    },
    {
        'id': 252,
        'link': 'https://gimsap.ca/collections/all/products/carotino-cooking-oil-1-1l-35-2-oz-box',
        'name': 'Carotino Cooking Oil 1.1L (35.2 oz) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $235.00',
        'description': '<p>For those who are looking for a great way to prepare their favorite dishes, Carotino Cooking Oil is the perfect product. With its natural blend of olive and canola oils, Carotino Cooking Oil is ideal for frying, sautéing, grilling, and baking. Carotino Cooking Oil is free of trans fats and cholesterol, and has a neutral taste and aroma. It is also non-GMO and gluten-free. With Carotino Cooking Oil, there is no need to worry about frying foods in unhealthy oils.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fed0d681-29d0-488b-9913-a17e058d567b_300x300.jpg?v=1645133494'
    },
    {
        'id': 253,
        'link': 'https://gimsap.ca/collections/all/products/carotino-cooking-oil-3-3l',
        'name': 'Carotino Cooking Oil 3.3L',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $39.99',
        'description': '<p>Carotino Cooking Oil is a premium quality cooking oil made from sunflower seeds. The 3.3L container is a convenient size for many families, with a 2-year shelf life. The cooking oil is perfect for frying, sautéing, and deep frying, and it can be used for cooking both sweet and savory dishes. The cooking oil is a perfect choice for those looking for a high-quality cooking oil with a long shelf life.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2c2d7dc7-bca7-4c9a-a1bb-0a0b43b782fc_300x300.jpg?v=1645133495'
    },
    {
        'id': 254,
        'link': 'https://gimsap.ca/collections/all/products/carotino-cooking-oil-550-mil',
        'name': 'Carotino Cooking Oil 550 mil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Carotino Cooking Oil 550 mil Carotino Cooking Oil is the ultimate olive oil alternative. Unlike olive oil, Carotino Cooking Oil is a vegan and paleo-friendly cooking oil. It is free of any animal byproducts and is low in saturated fat. Carotino Cooking Oil is an excellent alternative to animal fats, such as butter, lard, and tallow. It is cholesterol-free and has a light, pleasant taste. The cooking oil is also certified Kosher. Carotino Cooking Oil is made from a combination of cold-pressed oils from the finest fruit and vegetable sources.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b0419ef1-3adb-4814-8528-787c3d5e9133_300x300.jpg?v=1645133496'
    },
    {
        'id': 255,
        'link': 'https://gimsap.ca/collections/all/products/carotone-brightening-cream-330ml',
        'name': 'Carotone 3 in 1 Brightening Cream 330mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.99',
        'description': '<p>Carotone Brightening Cream is a creamy, rich formula that lightens skin and moisturizes. It’s formulated with peptides, antioxidants, and botanical extracts to hydrate, smooth, and brighten the skin. It is paraben-free and hypoallergenic.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d11f3cd8-6a81-47e9-84b8-0899fcbe92a9_300x300.jpg?v=1645133498'
    },
    {
        'id': 256,
        'link': 'https://gimsap.ca/collections/all/products/carotone-b-s-c-maxi-effect-30ml',
        'name': 'Carotone Black Spot Corrector (B.S.C.) Maxi Effect 30mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p>Carotone Black Spot Corrector (B.S.C.) Maxi Effect&nbsp; is a new formula that is supposed to help boost collagen production and firm skin. It helps reduce the appearance of dark spots caused by acnes, blemishes and hyperpigmentation.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/CCAROTOR-1_300x300.jpg?v=1647972436'
    },
    {
        'id': 257,
        'link': 'https://gimsap.ca/collections/all/products/carotone-brightening-oil-3-in-1',
        'name': 'Carotone Brightening oil (3 in 1)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Carotone Brightening Oil is a 3-in-1 formula that brightens skin, protects against UV rays, and moisturizes. This product is the perfect way to brighten up your skin and give it a healthy glow. The formula is made with shea butter, grape seed oil, vitamin E, and pure jojoba oil. These ingredients combine to provide a rich and nourishing oil that soothes and protects the skin. This product is cruelty-free and free of any animal byproducts.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_27d2be40-fdb8-4340-899a-85833b890ce2_300x300.jpg?v=1645133499'
    },
    {
        'id': 258,
        'link': 'https://gimsap.ca/collections/all/products/carotone-cream',
        'name': 'Carotone Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Carotone Cream is a topical, hypoallergenic product that contains ingredients that promote skin health and reduce the appearance of age spots. The cream can be used on any area of the body and is specially formulated to treat hyperpigmentation. Carotone.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8a0c9acb-510c-4a6a-99a7-d858457ad7a5_300x300.jpg?v=1645133502'
    },
    {
        'id': 259,
        'link': 'https://gimsap.ca/collections/all/products/carrot-oil-hair-lotion',
        'name': 'Carrot Oil Hair Lotion',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Carrot Oil Hair Lotion is a product that provides intense hydration and restores hair’s natural shine. It is made with 100% natural ingredients and is safe for color-treated hair. This product does not contain harsh chemicals, alcohol, or sulfates, and is free of artificial colors. It is vegan and cruelty-free. Carrot Oil Hair Lotion is perfect for any hair type, and is especially beneficial for dry, damaged, or chemically-treated hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e61043a3-40a9-497d-8826-3c16d1be71cb_300x300.jpg?v=1645133516'
    },
    {
        'id': 260,
        'link': 'https://gimsap.ca/collections/all/products/cashew-bottle-small',
        'name': 'Cashew Bottle small',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p><meta charset="utf-8"><span data-mce-fragment="1">Cashews are a crunchy, delicious snack that can be enjoyed as is or used in many recipes. They are also a healthy snack, as they are high in monounsaturated fats and contain no cholesterol.</span><br></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f685655c-cfb6-4262-a99d-9023f3d60270_300x300.jpg?v=1645133518'
    },
    {
        'id': 261,
        'link': 'https://gimsap.ca/collections/all/products/cashews-whole-roasted-unsalted-lb',
        'name': 'Cashews whole roasted unsalted /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p><span>Cashews are a crunchy, delicious snack that can be enjoyed as is or used in many recipes. These cashews are unsalted. They are also a healthy snack, as they are high in monounsaturated fats and contain no cholesterol.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3015f3e4-6cc4-466e-ad71-33ff31307874_300x300.jpg?v=1645133521'
    },
    {
        'id': 262,
        'link': 'https://gimsap.ca/collections/all/products/cashews-whole-roasted-unsalted-12-kg',
        'name': 'Cashews whole roasted unsalted 12 Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $300.00',
        'description': '<p>Cashews are a crunchy, delicious snack that can be enjoyed as is or used in many recipes. These cashews are unsalted. They are also a healthy snack, as they are high in monounsaturated fats and contain no cholesterol.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_edf946b9-c7e9-4a11-9282-fede06201795_300x300.jpg?v=1645133519'
    },
    {
        'id': 263,
        'link': 'https://gimsap.ca/collections/all/products/cashews-whole-roasted-unsalted-25lb',
        'name': 'Cashews whole roasted unsalted 25lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $300.00',
        'description': '<p><span>Cashews are a crunchy, delicious snack that can be enjoyed as is or used in many recipes. These cashews are unsalted. They are also a healthy snack, as they are high in monounsaturated fats and contain no cholesterol.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fa805fe5-9e9f-4c29-826d-a2dd384ae251_300x300.jpg?v=1645133520'
    },
    {
        'id': 264,
        'link': 'https://gimsap.ca/collections/all/products/cassava-flour-lafun-kabeya',
        'name': 'Cassava Flour Lafun (Kabeya)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_74660eee-2685-476a-afae-a0707e1d601d_300x300.jpg?v=1645133523'
    },
    {
        'id': 265,
        'link': 'https://gimsap.ca/collections/all/products/cassava-flour-lafun-20lbs-todaj',
        'name': 'cassava flour lafun 20lbs (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $40.00',
        'description': '<p><span>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_832cceb0-6f6b-4bdc-8c7b-4b662ec3db15_300x300.jpg?v=1645133522'
    },
    {
        'id': 266,
        'link': 'https://gimsap.ca/collections/all/products/cassava-foufou-delice-1kg',
        'name': 'Cassava Foufou (delice) 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b349b59c-5d38-490a-b0d7-adc59cf85bff_300x300.jpg?v=1645133525'
    },
    {
        'id': 267,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-10lbs',
        'name': 'cassava fufu 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p><meta charset="utf-8"><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ec8c9dca-3896-4d9f-ab7c-0bfcf18f941a_300x300.jpg?v=1645133526'
    },
    {
        'id': 268,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-110-lbs',
        'name': 'Cassava fufu 110 lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $200.00',
        'description': '<p><meta charset="utf-8"><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f0696b36-587d-4d86-8246-a9f395974af9_300x300.jpg?v=1645133527'
    },
    {
        'id': 269,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-1kgx12-delice',
        'name': 'Cassava Fufu 1kgx12 (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><meta charset="utf-8"><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_20972c53-a5b3-4ffd-b33a-e65e78fae67b_300x300.jpg?v=1645133528'
    },
    {
        'id': 270,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-3kgx5-delice',
        'name': 'Cassava Fufu 3kgx5 (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><meta charset="utf-8"><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1cc369e6-e6d8-4ba9-bc5f-29c3d3621b4a_300x300.jpg?v=1645133529'
    },
    {
        'id': 271,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-5lbs',
        'name': 'cassava fufu 5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p><meta charset="utf-8"><span>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0611799a-de81-44d6-8195-a15928ffd3c9_300x300.jpg?v=1645133530'
    },
    {
        'id': 272,
        'link': 'https://gimsap.ca/collections/all/products/cassava-fufu-flour-4lbs-de-chosen',
        'name': 'cassava fufu flour 4lbs (De Chosen)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Cassava fufu flour is made from cassava roots that are dried and then ground into a fine powder. It is used in various types of traditional African cuisine. The flavor is best described as earthy and slightly sweet. It is most often used to make fufu, a thick paste made from boiling the flour in water or milk. It can also be used to make other types of traditional African dishes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e39c8b16-0a4e-47ae-bdb6-2b037dc2d8b7_300x300.jpg?v=1645133531'
    },
    {
        'id': 273,
        'link': 'https://gimsap.ca/collections/all/products/cassava-lafun-10lbs',
        'name': 'cassava lafun 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p><span>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ce5145a1-11af-4076-b8e0-6980b5eed27c_300x300.jpg?v=1645133532'
    },
    {
        'id': 274,
        'link': 'https://gimsap.ca/collections/all/products/cassava-lafun-110lbs',
        'name': 'Cassava lafun 110lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $180.00',
        'description': '<p><span>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f07c4b3d-c429-4c7e-acab-1f90c6644437_300x300.jpg?v=1645133534'
    },
    {
        'id': 275,
        'link': 'https://gimsap.ca/collections/all/products/cassava-lafun-4-5lbs',
        'name': 'Cassava Lafun 4.5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ca84a698-f040-4036-86c6-73a0e91ddb42_300x300.jpg?v=1645133535'
    },
    {
        'id': 276,
        'link': 'https://gimsap.ca/collections/all/products/cassava-lafun-5lbs',
        'name': 'cassava lafun 5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p><span>Cassava Flour Lafun (Kabeya) is a traditional African delicacy. It is made from grated cassava roots that are boiled, ground, and then made into a thick dough. The dough is then flattened and fried to create a delicacy that is popular in the West African country of Ghana.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_1bb62e37-c074-4729-8112-cd08a4e2f4f8_300x300.jpg?v=1650595008'
    },
    {
        'id': 277,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-1kg-bened-box',
        'name': 'Cassava Leaves 1Kg (Bened) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $95.50',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_300x300.jpg?v=1650595123'
    },
    {
        'id': 278,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-1kgbened-piece',
        'name': 'Cassava leaves 1kg(Bened) piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8a4b59b9-3c51-4846-92c2-ac88eac91202_300x300.jpg?v=1650595153'
    },
    {
        'id': 279,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-1kgkabeya-box',
        'name': 'Cassava leaves 1kg(kabeya) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $115.00',
        'description': '<p><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b13f18f9-84b7-434d-8e23-338aab528dff_300x300.jpg?v=1650595171'
    },
    {
        'id': 280,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-1kgkabeya-piece',
        'name': 'Cassava leaves 1kg(kabeya) piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_e69972ef-baaa-4da2-9883-45df3206bdea_300x300.jpg?v=1650595235'
    },
    {
        'id': 281,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-22x700g-box',
        'name': 'Cassava Leaves 22x700g Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $95.00',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c65a855d-1b23-43a1-8065-22b28e88b0ce_300x300.jpg?v=1645133545'
    },
    {
        'id': 282,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-500gpondu',
        'name': 'Cassava leaves 500g(pondu)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_021e2049-c081-416f-9d8f-97053c27d729_300x300.jpg?v=1650596094'
    },
    {
        'id': 283,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-500gpondu-piece',
        'name': 'Cassava leaves 500g(Pondu) piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p><meta charset="utf-8"><span data-mce-fragment="1">Cassava leaves</span><span data-mce-fragment="1">&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span><br></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_39ded964-3203-4798-934b-7f12c89c5239_300x300.jpg?v=1650596231'
    },
    {
        'id': 284,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-700g-pc',
        'name': 'Cassava Leaves 700g pc',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_45d191f0-392d-4bee-b650-bf26f533e63a_300x300.jpg?v=1650596250'
    },
    {
        'id': 285,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-800g-bened-box',
        'name': 'Cassava Leaves 800g (Bened) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $105.00',
        'description': '<p><meta charset="utf-8"><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_ad0ada00-7ab6-4d20-b005-03706d305cb7_300x300.jpg?v=1650596277'
    },
    {
        'id': 286,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-800g-bened-piece',
        'name': 'Cassava Leaves 800g (Bened) piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_6bd54236-caa6-4fae-a89e-7eb8366cbc43_300x300.jpg?v=1650596416'
    },
    {
        'id': 287,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-ing-bened-1-3kg-box',
        'name': 'Cassava Leaves Ing (Bened) 1.3kg Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $120.00',
        'description': '<p><span>Cassava leaves&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9d7a9ace-9a06-4508-af57-7cfabce5c2b3_300x300.jpg?v=1650596462'
    },
    {
        'id': 288,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leaves-ing-bened-1-3kg-piece',
        'name': 'Cassava Leaves Ing (Bened) 1.3kg piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.75',
        'description': '<p><span>Cassava leaves</span><span>&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_fa8f25e8-86b5-43eb-8f3b-582cabf5e022_300x300.jpg?v=1650596546'
    },
    {
        'id': 289,
        'link': 'https://gimsap.ca/collections/all/products/cassava-leavesamelia',
        'name': 'Cassava leaves(amelia)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Cassava leaves&nbsp;are a common leafy green found in most tropical countries. The leaves are often used in dishes like salads, soups, and stir-fries. The leaves are harvested from the cassava plant and are a good source of calcium, iron, and vitamin C.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_726280db-0e78-4748-8480-648b99a1de69_300x300.jpg?v=1650596636'
    },
    {
        'id': 290,
        'link': 'https://gimsap.ca/collections/all/products/cassava-powder',
        'name': 'Cassava Powder',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Cassava is a root vegetable that is typically found in Africa, Central America, and South America. It is a carbohydrate-rich food that is consumed by many people in these regions. It is also a source of dietary fiber, protein, and calcium. Cassava Powder is a powder that is made from dried cassava roots. It is often used as a substitute for wheat flour in baking.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_ddae7882-6c06-49e5-86c4-202d858e7b64_300x300.jpg?v=1650596713'
    },
    {
        'id': 291,
        'link': 'https://gimsap.ca/collections/all/products/castor-oil',
        'name': 'Castor Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Castor Oil is a thick, amber-colored oil extracted from the castor bean. Castor Oil is a good choice for those who want to grow their hair, as it can stimulate hair growth and reduce hair loss. Castor Oil can also be used to soothe irritated skin and to help heal scars.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8bf01221-e13b-497c-8932-c12dd8009b09_300x300.jpg?v=1645133555'
    },
    {
        'id': 292,
        'link': 'https://gimsap.ca/collections/all/products/caterpillar',
        'name': 'Caterpillar',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 293,
        'link': 'https://gimsap.ca/collections/all/products/caterpiller-bowl',
        'name': 'Caterpiller (bowl)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Caterpiller in a bowl</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 294,
        'link': 'https://gimsap.ca/collections/all/products/catfish-800-1200-per-lb',
        'name': 'Catfish (800-1200)  per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': '<p>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_57032632-e381-4172-b208-4a8eeb292a8e_300x300.jpg?v=1650596856'
    },
    {
        'id': 295,
        'link': 'https://gimsap.ca/collections/all/products/catfish-800-1200-13-2-lb-box-cut',
        'name': 'Catfish (800-1200) 13.2 lb box cut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $52.50',
        'description': '<p><meta charset="utf-8"><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9083bb6f-1291-44f5-967e-5dd500bcb289_300x300.jpg?v=1650596888'
    },
    {
        'id': 296,
        'link': 'https://gimsap.ca/collections/all/products/catfish-800-1200-13-2-lb-box-uncut',
        'name': 'Catfish (800-1200) 13.2 lb box uncut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $48.50',
        'description': '<p><meta charset="utf-8"><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_f5eb2136-ab64-47fc-879b-6eb139c7d7ff_300x300.jpg?v=1650596901'
    },
    {
        'id': 297,
        'link': 'https://gimsap.ca/collections/all/products/catfish-cut-frozen-box-550-750g',
        'name': 'Catfish Cut Frozen Box 550-750g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p>The Catfish Cut Frozen Box is a frozen product that is of a high quality. It is high in protein and has a long shelf life. The product is available in a variety of sizes and weights, so the customer can purchase what they need.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_5fd633e0-13b3-4756-b9a0-34e822c34fcb_300x300.jpg?v=1650596913'
    },
    {
        'id': 298,
        'link': 'https://gimsap.ca/collections/all/products/catfish-dried-sam-per-lb',
        'name': 'Catfish Dried (Sam) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.50',
        'description': '<p><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_01bf50c1-5784-4d8f-bbcc-b58058f07904_300x300.jpg?v=1650597012'
    },
    {
        'id': 299,
        'link': 'https://gimsap.ca/collections/all/products/catfish-dried-per-lb',
        'name': 'Catfish Dried per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.99',
        'description': '<p><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_31de7ee1-3729-40b0-9307-c4f963b2e823_300x300.jpg?v=1650597043'
    },
    {
        'id': 300,
        'link': 'https://gimsap.ca/collections/all/products/catfish-frozen-lb',
        'name': 'Catfish Frozen /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': '<p><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_76f5f3e6-a821-4e97-ab07-2ff5649a2727_300x300.jpg?v=1645133567'
    },
    {
        'id': 301,
        'link': 'https://gimsap.ca/collections/all/products/catfish-frozen-box-550-750g',
        'name': 'Catfish Frozen Box 550-750g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $55.00',
        'description': '<p>Catfish Frozen Box 550-750g Catfish is a mild, white fish that is low in fat and high in protein. This product comes in a 550-750g box, and is best when fried, grilled, or baked.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0281ee5c-4a7f-45e6-861e-c933c024c021_300x300.jpg?v=1650597173'
    },
    {
        'id': 302,
        'link': 'https://gimsap.ca/collections/all/products/catfish-headless-aa-1',
        'name': 'Catfish headless AA-1',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $90.00',
        'description': '<p><span>Catfish is known for its delicious white meat. Catfish has a white meat that is a good source of protein. Catfish is also a good source of omega-3 fatty acids, vitamin D, and selenium. Catfish is a great source of lean protein and a healthy meal option.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_ab92ead4-09e0-4e3a-9b20-9986c244ec68_300x300.jpg?v=1650597288'
    },
    {
        'id': 303,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-honey-wheat-w-milk-12x1kg',
        'name': 'Cerelac (honey &amp; wheat w/ milk) 12x1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $28.00',
        'description': '<p>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e1646329-b14e-4b72-ada7-db39b9d6a11f_300x300.jpg?v=1645133588'
    },
    {
        'id': 304,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-honey-wheat-w-milk-1kg',
        'name': 'Cerelac (honey &amp; wheat w/ milk) 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_50e4c5d8-2690-450b-86cb-28b2a66a6c82_300x300.jpg?v=1645133589'
    },
    {
        'id': 305,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-maize-with-milk-12x400g',
        'name': 'Cerelac (Maize with milk) 12x400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_c3f75f8c-c293-49ed-a48c-b7bdd63e343c_300x300.jpg?v=1650597469'
    },
    {
        'id': 306,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-maize-with-milk-400g',
        'name': 'Cerelac (Maize with milk) 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9c0f3cd4-76ce-421d-a4ac-143aed0b184e_300x300.jpg?v=1650597490'
    },
    {
        'id': 307,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-wheat-w-milk-400g',
        'name': 'Cerelac (Wheat w/ Milk) 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_41b6b483-f631-48c7-9f95-840e13789342_300x300.jpg?v=1645133597'
    },
    {
        'id': 308,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-honey-wheat-w-milk-400g',
        'name': 'Cerelac Honey &amp; Wheat w/ Milk 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_864f8974-c3eb-410a-b672-014a708300a0_300x300.jpg?v=1645133590'
    },
    {
        'id': 309,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-maize-w-milk-1kg',
        'name': 'Cerelac Maize w/ Milk 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9904ad08-8dea-4b5f-b520-22b5ac2c2dc5_300x300.jpg?v=1650597553'
    },
    {
        'id': 310,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-maize-w-milk-6x1kg-box-nigeria',
        'name': 'Cerelac Maize w/ Milk 6x1kg Box (Nigeria)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2a973026-cd92-4dc0-b9b5-2ceea6a42a26_300x300.jpg?v=1650597576'
    },
    {
        'id': 311,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-mixed-fruits-wheat-w-milk-1kg',
        'name': 'Cerelac Mixed Fruits &amp; Wheat w/ Milk 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2dc4c59d-c78f-41f6-959f-f1ae0f66be22_300x300.jpg?v=1645133595'
    },
    {
        'id': 312,
        'link': 'https://gimsap.ca/collections/all/products/cerelac-wheat-w-milk-1kg',
        'name': 'Cerelac Wheat w/ Milk 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.00',
        'description': '<p><span>Cerelac is a cereal product made of oats, wheat, barley, rice, maize, sugar, skimmed milk powder, palm oil, vitamins and minerals. It is a nutritious breakfast for infants and toddlers and can be mixed with fruit and milk. Cerelac is a convenient option for busy parents and caregivers who want to provide their children with a healthy start to the day.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_44b64d15-836d-439f-a6d7-9d272014c17f_300x300.jpg?v=1645133596'
    },
    {
        'id': 313,
        'link': 'https://gimsap.ca/collections/all/products/chai-seed-white-5kg',
        'name': 'Chai Seed white 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $70.00',
        'description': '<p>Chai Seed white is a product that is intended to be mixed with water to create a chai drink. The product is made from organic chai seeds and comes in a 5kg bag.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_3aef2815-fc7f-4ca5-8ae9-5137cac5dace_300x300.jpg?v=1650597682'
    },
    {
        'id': 314,
        'link': 'https://gimsap.ca/collections/all/products/chalk',
        'name': 'Chalk',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>A type of clay that many consume as medicine.&nbsp;&nbsp;Is also used to make facial masks and soaps.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f6cb5dbf-07d2-4dd6-97ab-b9d9b510ed20_300x300.jpg?v=1650597860'
    },
    {
        'id': 315,
        'link': 'https://gimsap.ca/collections/all/products/chalk-clay-shere-0-5lb',
        'name': 'Chalk (clay shere) 0.5lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p><span>A type of clay that many consume as medicine.&nbsp;</span><span>&nbsp;Is also used to make facial masks and soaps.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_4922a611-8726-4dfc-85bf-23486d72cc44_300x300.jpg?v=1650598187'
    },
    {
        'id': 316,
        'link': 'https://gimsap.ca/collections/all/products/chalk-clay-shere-1lb',
        'name': 'Chalk (clay shere) 1lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<span data-mce-fragment="1">A type of clay that many consume as medicine.&nbsp;</span><span data-mce-fragment="1">&nbsp;Is also used to make facial masks and soaps.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_942042ae-ab45-4a43-8ef0-d9650bc9a1c8_300x300.jpg?v=1650598199'
    },
    {
        'id': 317,
        'link': 'https://gimsap.ca/collections/all/products/chalk-clay-shere-box',
        'name': 'Chalk (clay shere) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $250.00',
        'description': '<span data-mce-fragment="1">A type of clay that many consume as medicine.&nbsp;</span><span data-mce-fragment="1">&nbsp;Is also used to make facial masks and soaps.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_245a57e9-bcbe-4db2-bf0c-f5987d540337_300x300.jpg?v=1650598224'
    },
    {
        'id': 318,
        'link': 'https://gimsap.ca/collections/all/products/checkers-custard-powder-2kg',
        'name': 'Checkers Custard Powder 2kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Checkers Custard Powder is versatile and can be used in any recipe that calls for custard. It can be used to make traditional puddings, flans, creams, and cakes. It is a great way to add a hint of creaminess to your desserts without having to make it from scratch.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_438f8dd1-8d94-417e-ad39-2cb0d4ce2e06_300x300.jpg?v=1650598326'
    },
    {
        'id': 319,
        'link': 'https://gimsap.ca/collections/all/products/checkers-custard-powder-400g',
        'name': 'Checkers Custard Powder 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Checkers Custard Powder is versatile and can be used in any recipe that calls for custard. It can be used to make traditional puddings, flans, creams, and cakes. It is a great way to add a hint of creaminess to your desserts without having to make it from scratch.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_35d08e71-4b0d-413b-8323-30d36cbe4895_300x300.jpg?v=1650598382'
    },
    {
        'id': 320,
        'link': 'https://gimsap.ca/collections/all/products/chewing-stick',
        'name': 'Chewing Stick',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Chewing sticks are pieces of plant stem, typically found in Africa, that are chewed on in order to help clean teeth and freshen breath. These natural pieces of plant stem are typically long and have been traditionally used by Africans for hundreds of years.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a2d12308-497f-409c-8c52-3cb6da465fb1_300x300.jpg?v=1645133605'
    },
    {
        'id': 321,
        'link': 'https://gimsap.ca/collections/all/products/chia-seed-black-per-lb',
        'name': 'Chia Seed  Black per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p><span>The Chia Seed is a seed grown in South America that is full of Omega-3 fatty acids, protein, and fiber. This seed is perfect for those looking to improve their health and nutrition. It can be used in a variety of dishes and drinks, making it a great addition to any diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b9535cc2-7bcc-4072-87b4-f75da318f991_300x300.jpg?v=1650598557'
    },
    {
        'id': 322,
        'link': 'https://gimsap.ca/collections/all/products/chia-seed-5kg-code-1675',
        'name': 'Chia Seed 5kg Code 1675',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>The Chia Seed is a seed grown in South America that is full of Omega-3 fatty acids, protein, and fiber. This seed is perfect for those looking to improve their health and nutrition. It can be used in a variety of dishes and drinks, making it a great addition to any diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0681714c-a894-4d03-ba98-657a23a47b1f_300x300.jpg?v=1650598653'
    },
    {
        'id': 323,
        'link': 'https://gimsap.ca/collections/all/products/chia-seed-black-5kg',
        'name': 'Chia Seed Black 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $50.00',
        'description': '<p>Chia Seed Black 5kg is a great addition to any diet. This package contains 5kg of Chia Seed which can be used in a variety of ways. The Chia Seed is a seed grown in South America that is full of Omega-3 fatty acids, protein, and fiber. This seed is perfect for those looking to improve their health and nutrition. It can be used in a variety of dishes and drinks, making it a great addition to any diet.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_26129d57-e87a-4cda-94ad-c812bbdf6b30_300x300.jpg?v=1650598518'
    },
    {
        'id': 324,
        'link': 'https://gimsap.ca/collections/all/products/chia-seed-white-code-1676-5kg',
        'name': 'Chia Seed White Code 1676  5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $52.00',
        'description': '<p><span>The Chia Seed is a seed grown in South America that is full of Omega-3 fatty acids, protein, and fiber. This seed is perfect for those looking to improve their health and nutrition. It can be used in a variety of dishes and drinks, making it a great addition to any diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_8cd801c4-1eb3-4f10-b0ac-582bdd9ef28f_300x300.jpg?v=1650598716'
    },
    {
        'id': 325,
        'link': 'https://gimsap.ca/collections/all/products/chia-seed-white-code-1676-per-lb',
        'name': 'Chia Seed White Code 1676  per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p><span>The Chia Seed is a seed grown in South America that is full of Omega-3 fatty acids, protein, and fiber. This seed is perfect for those looking to improve their health and nutrition. It can be used in a variety of dishes and drinks, making it a great addition to any diet.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_3cadf7c4-2453-421d-8404-60f4c739f544_300x300.jpg?v=1650598734'
    },
    {
        'id': 326,
        'link': 'https://gimsap.ca/collections/all/products/chicharon',
        'name': 'chicharon',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.70',
        'description': '<p>Chicharon is a type of pork rind that is fried in oil and seasoned with salt. The word chicharon is Spanish for "crackling" or "crackling of fat." The chicharon is crispy and crunchy, making it a great option for any type of meal. It can be eaten alone as a snack or used as a topping for other dishes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8abc3588-f1cb-4820-82a4-66b26ecda947_300x300.jpg?v=1650598846'
    },
    {
        'id': 327,
        'link': 'https://gimsap.ca/collections/all/products/chicken-breast',
        'name': 'Chicken Breast',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $55.00',
        'description': '<p>The underside of a chicken. There are many ways to cook delicious chicken breasts, from baking to even air frying.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0b3b90c5-5d42-4508-b8d0-6008c17df8dd_300x300.jpg?v=1650599094'
    },
    {
        'id': 328,
        'link': 'https://gimsap.ca/collections/all/products/chicken-drumstick-5kg',
        'name': 'Chicken Drumstick 10lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.50',
        'description': "<p>Soft Chicken Drumsticks. If you are looking for a flavorful and juicy chicken, the chicken drumstick is the perfect choice. With a price that won't break the bank, these drumsticks are perfect for any home chef. Cooked to perfection, this chicken is always juicy and full of flavor.&nbsp;With easy to follow recipes, it is sure to satisfy your taste buds.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_25550a08-bb3d-4d83-a546-762f25f71747_300x300.jpg?v=1645133615'
    },
    {
        'id': 329,
        'link': 'https://gimsap.ca/collections/all/products/chicken-drumstick-maple-leaf-19-29kg',
        'name': 'Chicken Drumstick 18kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': '<p><span data-mce-fragment="1">Soft Chicken Drumstick. Tired of fighting with your kids over who gets the drumstick? Well, this bulk pack of chicken drumsticks is perfect for you! The package&nbsp;will provide enough food for your family to enjoy. This bulk pack is a great buy for your family and will provide a great source of protein and nutrients.&nbsp;</span>Maple Leaf Foods is a Canadian company that specializes in poultry and meat products. Maple Leaf Foods has been a family-owned company since its founding in 1931.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ChickenDrum_300x300.jpg?v=1647369098'
    },
    {
        'id': 330,
        'link': 'https://gimsap.ca/collections/all/products/chicken-gizzard-lb',
        'name': 'Chicken Gizzard',
        'price': 'From $5.00',
        'description': '<p>A popular street food in many countries, chicken gizzards are a delicacy that should not be missed. Sold by the pound, chicken gizzards are one of the cheapest cuts of meat and are perfect for those on a budget. Though some people are not fond of the taste, chicken gizzards are easy to cook and make a tasty, protein-rich addition to any meal. Chicken gizzards are rich in nutrients, including protein, iron, and zinc.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4c9e3302-ded4-4f7f-8b38-38cd93400b1c_300x300.jpg?v=1645133621'
    },
    {
        'id': 331,
        'link': 'https://gimsap.ca/collections/all/products/chicken-gizzard-10kg-box',
        'name': 'Chicken Gizzards 40lb Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $125.00',
        'description': "<p>If you're looking for a low-fat, high-protein option for your next meal, then look no further than this&nbsp;40lb box of chicken gizzards. They're a tasty and nutritious alternative to chicken breast and will give you the energy you need to power through your day.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d3b43226-3eb0-4eed-a169-f6c4dfd75311_300x300.jpg?v=1645133618'
    },
    {
        'id': 332,
        'link': 'https://gimsap.ca/collections/all/products/chicken-leg-n-backsmall-chicken-10kg',
        'name': 'chicken leg n back(small chicken) 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $33.00',
        'description': '<p>This package contains a small chicken that weighs 10kg. This 10kg package of chicken legs and back is perfect for meal prep.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_1903f2f4-4cc4-4ea5-834e-8196e07e5e8d_300x300.jpg?v=1650599197'
    },
    {
        'id': 333,
        'link': 'https://gimsap.ca/collections/all/products/chicken-leg-n-back-attached-soft-per-lb',
        'name': 'chicken leg n back-attached (soft) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.00',
        'description': "<p>Bite-sized and juicy, these tender chicken legs are perfect for entertaining or as a quick snack. The back is attached for easy handling and because it's so tasty! These tender chicken legs are perfect for entertaining or as a quick snack.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d2e049f4-c3a5-468a-872d-dd59f0468fe5_300x300.jpg?v=1650599285'
    },
    {
        'id': 334,
        'link': 'https://gimsap.ca/collections/all/products/chicken-wings-superior-10kg',
        'name': 'Chicken Wings 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $45.00',
        'description': '<p><span data-mce-fragment="1">What could be better than a pack of 10kg of crispy, crunchy, delicious chicken wings? These are the perfect dish for a party, game day, or anytime you\'re looking for a hearty meal. They\'re great for snacks too!&nbsp;</span>Season these wings with a sweet and spicy sauce, that will make any night a night to remember.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7cb7f911-f1c4-4672-9476-535a022d62c4_300x300.jpg?v=1645133626'
    },
    {
        'id': 335,
        'link': 'https://gimsap.ca/collections/all/products/chin-chin-amazing-grace-big',
        'name': 'Chin-chin (Amazing Grace) - Big',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': "<p>A common snack in West Africa that's bite sized, crunchy and delicious.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b603907a-eb54-4108-a8d2-3e9081065192_300x300.jpg?v=1650599388'
    },
    {
        'id': 336,
        'link': 'https://gimsap.ca/collections/all/products/chin-chin-amazing-grace-small-regular',
        'name': 'Chin-chin (Amazing Grace) -Small Regular',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<span data-mce-fragment="1">A common snack in West Africa that\'s bite sized, crunchy and delicious.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_64fb0b70-a0a5-453d-a11e-5777b33b21c4_300x300.jpg?v=1650601265'
    },
    {
        'id': 337,
        'link': 'https://gimsap.ca/collections/all/products/chin-chin-amazing-grace-spicy',
        'name': 'Chin-Chin (Amazing Grace) Spicy',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<span data-mce-fragment="1">A common snack in West Africa that\'s bite sized, crunchy and delicious.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9b6ec00e-d375-44f8-9e1b-1aa8d8f47604_300x300.jpg?v=1645133630'
    },
    {
        'id': 338,
        'link': 'https://gimsap.ca/collections/all/products/china-lilly-soya-sauce-483ml',
        'name': 'China Lilly Soya Sauce 483mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>China Lilly Soya Sauce is a high quality soy sauce made in China. It is made from carefully selected soybeans, wheat, salt, and water. This soy sauce is great for stir-frying and marinating, and is low in sodium.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_30ff22fc-245b-45e2-a2b7-5073e98d741a_300x300.jpg?v=1650601375'
    },
    {
        'id': 339,
        'link': 'https://gimsap.ca/collections/all/products/chinchin-apexol-plastic',
        'name': 'Chinchin (Apexol) plastic',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<span data-mce-fragment="1">A common snack in West Africa that\'s bite sized, crunchy and delicious.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_73c28861-789f-4be1-a7e6-234f9b762b4c_300x300.jpg?v=1644953476'
    },
    {
        'id': 340,
        'link': 'https://gimsap.ca/collections/all/products/chinchin-bottle',
        'name': 'Chinchin Bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<span data-mce-fragment="1">A common snack in West Africa that\'s bite sized, crunchy and delicious.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_179672d7-a51e-411d-82ce-dc09c24955a3_300x300.jpg?v=1650601519'
    },
    {
        'id': 341,
        'link': 'https://gimsap.ca/collections/all/products/chinchin-snack-alive-250g',
        'name': 'Chinchin Snack Alive 250g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.50',
        'description': '<span data-mce-fragment="1">A common snack in West Africa that\'s bite sized, crunchy and delicious.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a74ed152-c88c-476e-80de-d18cda3e8a7e_300x300.jpg?v=1650601689'
    },
    {
        'id': 342,
        'link': 'https://gimsap.ca/collections/all/products/choco-milo',
        'name': 'Choco Milo',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>Choco Milo is a chocolate milk drink made with milk, cocoa, and honey. It is a delicious, nutritious drink that is a favorite among children and adults alike.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_53770203-e44a-41eb-8185-2960454e6511_300x300.jpg?v=1650601802'
    },
    {
        'id': 343,
        'link': 'https://gimsap.ca/collections/all/products/chocolate',
        'name': 'chocolate',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>This rich, smooth, and sweet chocolate is made with only the finest ingredients. It is rich in flavor and smooth in texture. This is the perfect treat for any occasion.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_474a3988-7ef7-44e6-8172-876a84f476cf_300x300.jpg?v=1645133634'
    },
    {
        'id': 344,
        'link': 'https://gimsap.ca/collections/all/products/chopseuy-mix',
        'name': 'Chopseuy mix',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $33.36',
        'description': '<p>Chopseuy mix is a product designed to make the perfect chopped seuy for soup. Chopseuy mix is made with the highest quality ingredients and is easy to use. The mixture is comprised of a combination of seuy, chopped carrots, chopped celery, chopped onion, and chopped cabbage. The mixture is great for making soups with or without broth.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_a86857db-4cb5-4888-b02c-95609177d2d1_300x300.jpg?v=1650601893'
    },
    {
        'id': 345,
        'link': 'https://gimsap.ca/collections/all/products/chuck-short-ribs',
        'name': 'Chuck short ribs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Chuck short ribs are a tough cut of meat, but once cooked low and slow, they will become soft and tender. They are best served with potatoes, carrots, and onions. These short ribs are a favorite for families with large appetites.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_8717d4ae-7a34-4426-a860-9d9935ec0669_300x300.jpg?v=1650601948'
    },
    {
        'id': 346,
        'link': 'https://gimsap.ca/collections/all/products/cinamon-stick',
        'name': 'Cinamon Stick',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': "<p>The product is a cinamon stick that has a slight cinamon flavor to it. It's best used in a dish that needs a little bit of cinamon flavor. It can be used in soups, meat dishes, and desserts.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_63376707-b128-4313-ae11-f0d033ad8969_300x300.jpg?v=1645133638'
    },
    {
        'id': 347,
        'link': 'https://gimsap.ca/collections/all/products/cinnamon-leaf',
        'name': 'Cinnamon Leaf',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>Cinnamon Leaf is a small, reddish-brown leaf that is used as a spice in many recipes. Cinnamon Leaf has a distinctive flavor that is both sweet and spicy. The leaf is a popular addition to chai tea, but can also be used in baking, desserts, and savory dishes. Cinnamon Leaf is used in many recipes for a variety of dishes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bb812c4f-a048-46b4-b828-fc35c30275aa_300x300.jpg?v=1645133639'
    },
    {
        'id': 348,
        'link': 'https://gimsap.ca/collections/all/products/citronell-lemon-grass-bened-25x300g-box',
        'name': 'Citronell (lemon grass Bened 25x300g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $137.00',
        'description': '<p>Citronell is a natural insect repellent. This is an eco-friendly and safe way to keep away insects. It is great for use in your home, car, and office. This product is also great for use in the outdoors. It is environmentally friendly and has a pleasant lemon scent.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3234adb7-583f-430f-afb3-39c811f524b8_300x300.jpg?v=1650602080'
    },
    {
        'id': 349,
        'link': 'https://gimsap.ca/collections/all/products/citronell-lemon-grass-bened-300g',
        'name': 'Citronell (lemon grass Bened) 300g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Citronell is a natural insect repellent. This is an eco-friendly and safe way to keep away insects. It is great for use in your home, car, and office. This product is also great for use in the outdoors. It is environmentally friendly and has a pleasant lemon scent.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b316ff38-5f46-4c8c-8a34-ca9b996909dc_300x300.jpg?v=1650602137'
    },
    {
        'id': 350,
        'link': 'https://gimsap.ca/collections/all/products/clairissim-serum',
        'name': 'Clairissim serum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.99',
        'description': "<p>Clairissim serum is the newest and most advanced skin care product on the market. It contains all natural ingredients that are clinically proven to reduce wrinkles and age spots. The formula has been designed to promote a healthy, youthful appearance by making the skin more elastic and reducing the appearance of fine lines. Clairissim serum is designed to work with your skin's natural repair process, making it more efficient and effective. This product is perfect for people who want to make a noticeable difference in their skin without resorting to drastic measures.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_ecd723bd-5899-4942-b70d-5cfc83de3792_300x300.jpg?v=1650602216'
    },
    {
        'id': 351,
        'link': 'https://gimsap.ca/collections/all/products/clairissime',
        'name': 'Clairissime',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.99',
        'description': "<p><span>It contains all natural ingredients that are clinically proven to reduce wrinkles and age spots. The formula has been designed to promote a healthy, youthful appearance by making the skin more elastic and reducing the appearance of fine lines. Is designed to work with your skin's natural repair process, making it more efficient and effective. This product is perfect for people who want to make a noticeable difference in their skin without resorting to drastic measures.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_3e0e89b8-69bb-41a2-85cd-8059b44b1686_300x300.jpg?v=1650602366'
    },
    {
        'id': 352,
        'link': 'https://gimsap.ca/collections/all/products/clairissime-glycerine',
        'name': 'CLAIRISSIME GLYCERINE',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Clairissime Glycerine is a clear, viscous liquid that is 100% vegetable-based. It is odorless and tasteless, making it perfect for use in any recipe. This product can be used in food products such as puddings, icings, chocolate, candy, and other desserts. It can also be used in products such as toothpaste, mouthwash, and hand lotion.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_28fdc462-ecc9-4eeb-903d-78c6a07588f7_300x300.jpg?v=1645133643'
    },
    {
        'id': 353,
        'link': 'https://gimsap.ca/collections/all/products/clairissime-sweet-almond-oil',
        'name': 'Clairissime Sweet Almond oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.99',
        'description': '<p>This is a luxurious, natural, and healthy moisturizer. The oil is derived from the sweet almond nut and is often used in many recipes. The oil has a light and sweet scent that is not overpowering. The oil is also suitable for sensitive skin.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_936b8c42-33f5-495e-89e7-fc6e060aac59_300x300.jpg?v=1645133644'
    },
    {
        'id': 354,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-complexion-soap',
        'name': 'Clear Essence Complexion Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>Clear Essence Complexion Soap is an all-natural, organic skin care product made with high quality ingredients. This soap is formulated to cleanse the skin and remove impurities, leaving it feeling soft and smooth. This soap is vegan, cruelty-free, and suitable for all skin types. It is also 100% organic, made with pure coconut oil, organic olive oil, organic soybean oil, organic jojoba oil, organic lavender oil, and organic aloe vera.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_389d49a3-edf8-447d-b7d2-f2c2ce859d5b_300x300.jpg?v=1645133647'
    },
    {
        'id': 355,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-complexion-soap-150g',
        'name': 'Clear Essence Complexion Soap 150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Clear Essence Complexion Soap is an all-natural, organic skin care product made with high quality ingredients. This soap is formulated to cleanse the skin and remove impurities, leaving it feeling soft and smooth. This soap is vegan, cruelty-free, and suitable for all skin types. It is also 100% organic, made with pure coconut oil, organic olive oil, organic soybean oil, organic jojoba oil, organic lavender oil, and organic aloe vera.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_864a293e-7cf1-44a9-90ee-357f9a13d6c6_300x300.jpg?v=1645133648'
    },
    {
        'id': 356,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-exclusive-medicated-fade-cream',
        'name': 'Clear Essence Exclusive Medicated Fade Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Our exclusive medicated fade cream is specially formulated to eliminate those spots and freckles in just two weeks. The cream is made with the highest quality ingredients, including vitamin E, Kojic acid, and green tea extract. The vitamins and green tea extract work to fade away those spots, while the Kojic acid prevents new spots from forming. All of these ingredients work together to create a powerful fade cream that is gentle on your skin. The product is made with an anti-inflammatory and anti-aging formula, so you will notice your skin feeling firmer and smoother. Clear Essence’s exclusive medicated fade cream is a skin care product designed to eliminate freckles and dark spots on the skin.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4476137e-fb9d-4c24-80fe-e7fd303e810f_300x300.jpg?v=1645133649'
    },
    {
        'id': 357,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-maxi-tone',
        'name': 'clear essence maxi tone',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Clear Essence Maxi Tone is a product that helps to remove dark spots and other skin discolorations. This formula helps to eliminate the appearance of dark spots, acne scars, and other skin discolorations. The product contains only natural ingredients and is a safe alternative to traditional skin lightening products.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a313ee04-e729-4147-a743-3220d0ec3209_300x300.jpg?v=1645133650'
    },
    {
        'id': 358,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-maxi-tone-skin-milk-227g',
        'name': 'Clear Essence Maxi-Tone SKin Milk 227g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Clear Essence Maxi-Tone Skin Milk is a light, creamy, and emollient skin milk that is infused with natural collagen and essential nutrients. This product is formulated to provide hydration and help reduce the appearance of fine lines and wrinkles. It is ideal for all skin types and provides long-lasting hydration to the skin. Clear Essence Maxi-Tone Skin Milk is a light, creamy, and emollient skin milk that is infused with natural collagen and essential nutrients. This product contains a unique blend of peptides, natural collagen, hyaluronic acid, Vitamin E, Vitamin C, Vitamin A, and shea butter to help soften and nourish the skin.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_54df3f80-e761-40d0-a56e-14bc7093b0e6_300x300.jpg?v=1645133651'
    },
    {
        'id': 359,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-medicated-cleansing-bar-soap',
        'name': 'Clear Essence Medicated Cleansing Bar Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>The Clear Essence Medicated Cleansing Bar Soap is a soap that is gentle enough for daily use. It is specially formulated to be mild enough for those with sensitive skin, but also powerful enough to remove dirt and oil. The soap is also medicated with Aloe Vera and Tea Tree Oil to cleanse and refresh the skin. This soap is made in the USA and contains no artificial colors or fragrance.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c2350f31-c96d-4313-b57a-e73ff1c7a140_300x300.jpg?v=1645133657'
    },
    {
        'id': 360,
        'link': 'https://gimsap.ca/collections/all/products/clear-essence-skin-lightening-serum',
        'name': 'Clear Essence Skin Lightening Serum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>A great way to lighten skin tone, Clear Essence Skin Lightening Serum can be used on all skin types. With Vitamin C, this product is a great addition to your daily routine. The product works to remove dark spots and discoloration from the skin, so that you can enjoy a healthy, clear complexion. Clear Essence Skin Lightening Serum is the perfect way to give your skin a fresh start.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a4666440-7ee8-4a71-8b1d-2c050bf4b9ba_300x300.jpg?v=1645133658'
    },
    {
        'id': 361,
        'link': 'https://gimsap.ca/collections/all/products/close-up-toothpaste-naija-140g',
        'name': 'Close-up Toothpaste Naija (140g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>It is not just toothpaste. It is a beautiful and protective product that will help you get your teeth to their best. It is specially formulated to help you achieve that sparkling white smile. It is easy to use and will keep your teeth clean and healthy. It also removes tartar and stains, giving you that beautiful smile.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_627fc6ce-e91e-4448-aaa6-76270962a65f_300x300.jpg?v=1650602931'
    },
    {
        'id': 362,
        'link': 'https://gimsap.ca/collections/all/products/cloves',
        'name': 'CLOVES',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Cloves are the dried, unopened flower buds of a tropical evergreen tree. The cloves are harvested by hand, dried in the sun, and then they are sorted by size and quality. Cloves are used in baking, desserts, and drinks. They are also used to make perfume and as a natural home fragrance.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6a389d7e-fd33-4d7f-a6d8-03292a8fc9ba_300x300.jpg?v=1645133660'
    },
    {
        'id': 363,
        'link': 'https://gimsap.ca/collections/all/products/cocacola-coke',
        'name': 'Cocacola Coke',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.10',
        'description': '<p>Coca-Cola is a sugar-sweetened, caffeinated soft drink.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_d45533e5-79c4-4275-a382-0f2670b9cbe8_300x300.jpg?v=1650603055'
    },
    {
        'id': 364,
        'link': 'https://gimsap.ca/collections/all/products/cock-soup-mix-43g',
        'name': 'Cock Soup Mix 43g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.30',
        'description': '<p>Cock Soup Mix is a mixture of ingredients to create a soup that is both hearty and flavorful. The mix includes mushrooms, garlic, onions, and ginger, as well as dried shrimp, dried scallops, and dried scallions. The soup can be cooked with either water or stock. This mix is perfect for a cold winter day.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_addb5d80-4463-4f5d-ac52-b9d77a02d6c4_300x300.jpg?v=1645133662'
    },
    {
        'id': 365,
        'link': 'https://gimsap.ca/collections/all/products/cocoa-butter',
        'name': 'Cocoa Butter',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': 'Comes from the processing of cocoa beans and is not only used for cooking but also skin and hair.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d7cc6e7d-eb58-4071-936b-a2efbab1c310_300x300.jpg?v=1645133663'
    },
    {
        'id': 366,
        'link': 'https://gimsap.ca/collections/all/products/coconut-creamed',
        'name': 'coconut creamed',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.00',
        'description': 'A type of thick cream made from coconut milk. Not only adds rich texture and flavor to deserts but also goes well in smoothies, dips and sauces,\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e3911eba-0746-43e9-9079-c6e19040892a_300x300.jpg?v=1650603800'
    },
    {
        'id': 367,
        'link': 'https://gimsap.ca/collections/all/products/coconut-flakes-unsweetened-25-lb',
        'name': 'Coconut Flakes (unsweetened)  25 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $100.00',
        'description': 'A light snack that can add a delicious crunch, texture flavor to any dessert.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3423f3c3-0ddc-41d5-bfdd-57c105a3ed10_300x300.jpg?v=1650603897'
    },
    {
        'id': 368,
        'link': 'https://gimsap.ca/collections/all/products/coconut-flakes-unsweetened-lb',
        'name': 'Coconut Flakes (unsweetened) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.35',
        'description': 'A light snack that can add a delicious crunch, texture flavor to any dessert.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_60efbbfb-d91d-4b0f-9f0d-7cc5bbb3cd4f_300x300.jpg?v=1650604402'
    },
    {
        'id': 369,
        'link': 'https://gimsap.ca/collections/all/products/coconut-milk-400ml-aroy-d',
        'name': 'Coconut Milk 400mL Aroy-D',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': 'A great alternative to cow milk that contains several vitamins and minerals.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a2f49686-1724-4a68-9cfa-940d7fe03ad5_300x300.jpg?v=1645133668'
    },
    {
        'id': 370,
        'link': 'https://gimsap.ca/collections/all/products/cocoyam',
        'name': 'cocoyam',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': 'A tropical root and vegetable crop. Can be roasted, fried or boiled. Can be used to make flour or sliced and fried to make chips.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_dee461fd-acb4-4f24-a26c-03b5a0d04631_300x300.jpg?v=1650604665'
    },
    {
        'id': 371,
        'link': 'https://gimsap.ca/collections/all/products/cocoyam-box',
        'name': 'Cocoyam Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $100.00',
        'description': '<p>&nbsp;</p>\n<p><span>A tropical root and vegetable crop. Can be roasted, fried or boiled. Can be used to make flour or sliced and fried to make chips.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_d216d6cb-facf-4e48-ba18-701eace22fd3_300x300.jpg?v=1650604941'
    },
    {
        'id': 372,
        'link': 'https://gimsap.ca/collections/all/products/cocoyam-powder-100g-best-bargain',
        'name': 'Cocoyam Powder 100g Best Bargain',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': 'Made from cocoyam root. Contains magnesium, iron, zinc and copper.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_52390481-b995-4186-aea8-69988a054fd2_300x300.jpg?v=1650605051'
    },
    {
        'id': 373,
        'link': 'https://gimsap.ca/collections/all/products/coke',
        'name': 'Coke',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>&nbsp;</p>\n<p>Coca-Cola is a sugar-sweetened, caffeinated soft drink.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7e862c75-7f92-4ec2-8dee-2cf8c3849ce3_300x300.jpg?v=1645133674'
    },
    {
        'id': 374,
        'link': 'https://gimsap.ca/collections/all/products/comb',
        'name': 'Comb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': 'A strip of plastic with narrow teeth the untangle or style hair.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_14be6034-9f89-4705-98a7-a3e0d40a8e70_300x300.jpg?v=1645133675'
    },
    {
        'id': 375,
        'link': 'https://gimsap.ca/collections/all/products/control-wig-spray-355ml',
        'name': 'Control Wig Spray 355ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': 'A 3 in 1 hair products made to help wigs and braids stay in place and look natural.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_5c4e2aef-d1dd-4a32-a1ae-94a3cb04a0a4_300x300.jpg?v=1650605339'
    },
    {
        'id': 376,
        'link': 'https://gimsap.ca/collections/all/products/cooking-oat-4-lb',
        'name': 'Cooking Oat 4 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': 'Rolled outs that have been coarsely chopped. Nutritious and delicious all at once.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1ebfcab8-8e36-433f-b901-bd6a46662e77_300x300.jpg?v=1650605577'
    },
    {
        'id': 377,
        'link': 'https://gimsap.ca/collections/all/products/cooking-pot',
        'name': 'cooking pot',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': 'Can be used to cook multiple things such as soup, stew and so much more.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_edb833d7-c9f4-4bc8-89b0-dc5548cb8b89_300x300.jpg?v=1645133678'
    },
    {
        'id': 378,
        'link': 'https://gimsap.ca/collections/all/products/cooking-pot-large',
        'name': 'Cooking Pot Large',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $120.00',
        'description': '<p>&nbsp;</p>\n<p><span>Can be used to cook multiple things such as soup, stew and so much more.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ca1fb4b5-aa13-4175-8230-4373678dc4e1_300x300.jpg?v=1645133679'
    },
    {
        'id': 379,
        'link': 'https://gimsap.ca/collections/all/products/coriander-powder',
        'name': 'Coriander Powder',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': 'Made from freshly grounded coriander seeds. Contain many nutrients such as vitamin A, vitamin C, folic acid and Riboflavin.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_07b67c5b-f44c-4556-848f-b992fa399077_300x300.jpg?v=1645133680'
    },
    {
        'id': 380,
        'link': 'https://gimsap.ca/collections/all/products/coriandre-mix-spices',
        'name': 'Coriandre Mix spices',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': 'Made from freshly grounded coriander seeds. Contain many nutrients such as vitamin A, vitamin C, folic acid and Riboflavin.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b78617c6-d3d4-4787-9bf5-f74fb69d3616_300x300.jpg?v=1645133681'
    },
    {
        'id': 381,
        'link': 'https://gimsap.ca/collections/all/products/corn-beef-exeter',
        'name': 'Corn Beef Exeter',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': 'Tasty with low sodium and fat.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_25213b32-1b76-4190-bb24-217ef7952407_300x300.jpg?v=1645133682'
    },
    {
        'id': 382,
        'link': 'https://gimsap.ca/collections/all/products/corn-beef-exeter-box',
        'name': 'Corn Beef Exeter Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $175.00',
        'description': 'Tasty with low sodium and fat.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_35ce13ea-473e-463e-9a48-f598346268c3_300x300.jpg?v=1645133684'
    },
    {
        'id': 383,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-agricor-50lb',
        'name': 'Corn Flour (Agricor) 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': 'Made from grounded cornmeal. Light, soft and great for baking and cooking.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f82ebccc-7e6c-457b-b89c-2ac9f5b62d65_300x300.jpg?v=1645133685'
    },
    {
        'id': 384,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-white-10kg',
        'name': 'Corn Flour White 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_da67a949-840a-45e4-b421-fd6f75be2645_300x300.jpg?v=1650642922'
    },
    {
        'id': 385,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-white-20kg',
        'name': 'Corn Flour White 20kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $45.00',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fbc7a01e-1c1f-490c-88da-5352b8af5912_300x300.jpg?v=1650642972'
    },
    {
        'id': 386,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-white-per-lb',
        'name': 'Corn Flour White per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_42359246-c3e3-4333-866e-0a635d8f6309_300x300.jpg?v=1645133688'
    },
    {
        'id': 387,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-yellow-10-kg',
        'name': 'Corn Flour Yellow (10 kg)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $27.00',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b16b41bd-2032-415e-8a03-f594165e9236_300x300.jpg?v=1650643014'
    },
    {
        'id': 388,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-yellow-lb',
        'name': 'Corn Flour Yellow /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.30',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_80fb76ad-1837-4c77-954a-057de98801e3_300x300.jpg?v=1650643050'
    },
    {
        'id': 389,
        'link': 'https://gimsap.ca/collections/all/products/corn-flour-yellow-22-68-kg',
        'name': 'Corn Flour Yellow 22.68 kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $50.00',
        'description': '<p>&nbsp;</p>\n<p><span>Made from grounded cornmeal. Light, soft and great for baking and cooking.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_910f2f04-3283-4e04-a115-6c3c184a7cec_300x300.jpg?v=1650643066'
    },
    {
        'id': 390,
        'link': 'https://gimsap.ca/collections/all/products/corn-grit-10lbs',
        'name': 'corn grit 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': 'Can typically be made from boiled dried hominy or from ground cornmeal.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_287bb162-cd13-44d2-8c99-36483d68dabf_300x300.jpg?v=1650643086'
    },
    {
        'id': 391,
        'link': 'https://gimsap.ca/collections/all/products/corn-grit-4lbs',
        'name': 'corn grit 4lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>&nbsp;</p>\n<p><span>Can typically be made from boiled dried hominy or from ground cornmeal.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8c92d3dd-ce5f-4239-a433-7562f7638207_300x300.jpg?v=1645133693'
    },
    {
        'id': 392,
        'link': 'https://gimsap.ca/collections/all/products/corn-grits-hominy-white-50-lb',
        'name': 'Corn Grits (Hominy) White 50 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>&nbsp;</p>\n<p><span>Can typically be made from boiled dried hominy or from ground cornmeal.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_1b61650a-4ee7-4b20-b8e3-4f71aa72d63f_300x300.jpg?v=1650643448'
    },
    {
        'id': 393,
        'link': 'https://gimsap.ca/collections/all/products/corn-husks',
        'name': 'corn husks',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': 'The peel of a corn.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ce5f1091-b0f1-4cd3-8bd5-f7bda4841eed_300x300.jpg?v=1650643499'
    },
    {
        'id': 394,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-white-lb',
        'name': 'Corn Kernels White /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': 'Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b7e3d969-d97e-4be1-8498-aba760358f65_300x300.jpg?v=1650643782'
    },
    {
        'id': 395,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-white-10kg',
        'name': 'Corn Kernels White 10Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': '<p>&nbsp;</p>\n<p><span>Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5e945889-3090-4c5c-992f-1f4d38bada4a_300x300.jpg?v=1650644159'
    },
    {
        'id': 396,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-white-50lb',
        'name': 'Corn Kernels White 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $47.00',
        'description': '<p>&nbsp;</p>\n<p><span>Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_372bb478-3b96-4fb0-aa4e-e9ac70f1336d_300x300.jpg?v=1650644179'
    },
    {
        'id': 397,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-yellow-lb',
        'name': 'Corn Kernels Yellow /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': '<p>&nbsp;</p>\n<p><span>Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_021525ac-e65d-4f62-bef5-725d94709a5c_300x300.jpg?v=1650644314'
    },
    {
        'id': 398,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-yellow-10kg',
        'name': 'Corn Kernels Yellow 10Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>&nbsp;</p>\n<p><span>Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_786b750b-acac-4ac0-9f37-67ead8b8ead8_300x300.jpg?v=1650644332'
    },
    {
        'id': 399,
        'link': 'https://gimsap.ca/collections/all/products/corn-kernels-yellow-50lb',
        'name': 'Corn Kernels Yellow 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $47.00',
        'description': '<p><span>Corn kernels have a sweet and crispy consistency when ripe and very rich in vitamin C.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f2ef1e2c-4cc2-4483-b2e8-5279ee81fae2_300x300.jpg?v=1650644349'
    },
    {
        'id': 400,
        'link': 'https://gimsap.ca/collections/all/products/corn-leaf',
        'name': 'Corn Leaf',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': 'A tall grass plant packed with vitamin K and potassium.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_300x300.png?v=1650644488'
    },
    {
        'id': 401,
        'link': 'https://gimsap.ca/collections/all/products/corn-meal-agricor-50lb',
        'name': 'Corn Meal (Agricor) 50lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': 'Made from whole dried corn kernel with a gritty texture.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c522c3ab-f0fd-4d49-901d-167dde8337e8_300x300.jpg?v=1645133707'
    },
    {
        'id': 402,
        'link': 'https://gimsap.ca/collections/all/products/cornickboy-bawang',
        'name': 'cornick(boy bawang)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>A delicious and crispy snack that tastes like fresh corn kernels.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_01d2eb67-b70a-4ab5-bdae-9a8a16c84ba2_300x300.jpg?v=1645133697'
    },
    {
        'id': 403,
        'link': 'https://gimsap.ca/collections/all/products/cottage-fresh-black-soap-aloe-vera',
        'name': 'Cottage Fresh Black Soap (Aloe Vera)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.50',
        'description': "A skin product that's fit for all and has no side effects. Contains oils like, she butter, cocoa butter, and palm oil.\n<p>&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/IMG_3804_small_7d585a2e-6566-4967-8628-56ffc84638c4_300x300.webp?v=1650648266'
    },
    {
        'id': 404,
        'link': 'https://gimsap.ca/collections/all/products/cottage-fresh-black-soap-avocado',
        'name': 'Cottage Fresh Black Soap (Avocado)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.50',
        'description': "<p>&nbsp;</p>\n<p><span>A skin product that's fit for all and has no side effects. Contains oils like, she butter, cocoa butter, and palm oil.</span></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/IMG_3804_small_4e04f0fc-93ea-4816-a93f-4c1d4b2df67b_300x300.webp?v=1650648438'
    },
    {
        'id': 405,
        'link': 'https://gimsap.ca/collections/all/products/cottage-fresh-black-soap-lemon',
        'name': 'Cottage Fresh Black Soap (Lemon)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.50',
        'description': "<p>&nbsp;</p>\n<p><span>A skin product that's fit for all and has no side effects. Contains oils like, she butter, cocoa butter, and palm oil.</span></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/IMG_3804_small_e77697d1-e413-40d5-9a8d-c07561679d32_300x300.webp?v=1650648474'
    },
    {
        'id': 406,
        'link': 'https://gimsap.ca/collections/all/products/couscous',
        'name': 'Couscous',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': 'A type of pasta that originates from Northern Africa.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_399db792-73b0-49c9-9365-79f13b7317f0_300x300.jpg?v=1650648605'
    },
    {
        'id': 407,
        'link': 'https://gimsap.ca/collections/all/products/couscous-box',
        'name': 'Couscous box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $120.00',
        'description': '<p><span>A type of pasta that originates from Northern Africa.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_50d14625-035c-44b5-880c-64990953b28b_300x300.jpg?v=1645133712'
    },
    {
        'id': 408,
        'link': 'https://gimsap.ca/collections/all/products/cowfoot-yyc-cut',
        'name': 'Cowfoot (YYC) Cut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': 'A great source of protein.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cc9bd280-7980-4f76-ba8f-db8c67923c5f_300x300.jpg?v=1650648692'
    },
    {
        'id': 409,
        'link': 'https://gimsap.ca/collections/all/products/cowfoot-yyc-uncut',
        'name': 'Cowfoot (YYC) Uncut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': '<p>&nbsp;</p>\n<p><span>A great source of protein.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ee8a5d34-6097-4c7a-a5de-73cff72868b3_300x300.jpg?v=1650648813'
    },
    {
        'id': 410,
        'link': 'https://gimsap.ca/collections/all/products/cowfoot-burnt',
        'name': 'Cowfoot Burnt',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>&nbsp;</p>\n<p><span>A great source of protein.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_d551364b-0bb7-4d4d-9a0f-2a919d64122b_300x300.jpg?v=1650648854'
    },
    {
        'id': 411,
        'link': 'https://gimsap.ca/collections/all/products/cowfoot-per-lb',
        'name': 'Cowfoot per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>&nbsp;</p>\n<p><span>A great source of protein.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_88969672-db54-4854-bdba-5786c586c7de_300x300.jpg?v=1645133714'
    },
    {
        'id': 412,
        'link': 'https://gimsap.ca/collections/all/products/cowskin-burnt-long-ones-cut',
        'name': 'Cowskin burnt long ones (cut)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p><span data-mce-fragment="1">The Cowskin burnt long ones are a type of animal skin that is still intact with hair. The cow skin is burned for a long time to remove the hair.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_3f28e996-3be3-42fa-8a58-d1d20a9aa201_300x300.jpg?v=1650648961'
    },
    {
        'id': 413,
        'link': 'https://gimsap.ca/collections/all/products/cowskin-burnt-long-ones-uncut',
        'name': 'Cowskin burnt long ones (uncut)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>The Cowskin burnt long ones are a type of animal skin that is still intact with hair. The cow skin is burned for a long time to remove the hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_7bb1135b-a262-4f32-8af1-bdfbcf8c76b6_300x300.jpg?v=1650649068'
    },
    {
        'id': 414,
        'link': 'https://gimsap.ca/collections/all/products/cowskin-burnt-nigerian',
        'name': 'Cowskin burnt Nigerian',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<span data-mce-fragment="1">The Cowskin burnt long ones are a type of animal skin that is still intact with hair. The cow skin is burned for a long time to remove the hair.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_e1982a68-daf5-4a7f-a3c7-1c249acc0a05_300x300.jpg?v=1650649098'
    },
    {
        'id': 415,
        'link': 'https://gimsap.ca/collections/all/products/cowskin-burnt-toronto',
        'name': 'Cowskin burnt Toronto',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p><span>The Cowskin burnt long ones are a type of animal skin that is still intact with hair. The cow skin is burned for a long time to remove the hair.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_17d18e9a-b35a-4172-a32f-8c7e6714b76f_300x300.jpg?v=1650649129'
    },
    {
        'id': 416,
        'link': 'https://gimsap.ca/collections/all/products/cowskin-unburnt-lb',
        'name': 'Cowskin unburnt /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<span data-mce-fragment="1">The Cowskin burnt long ones are a type of animal skin that is still intact with hair. The cow skin is burned for a long time to remove the hair.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_206dbcb8-9df0-4e18-8e1f-82b81043acda_300x300.jpg?v=1650649149'
    },
    {
        'id': 417,
        'link': 'https://gimsap.ca/collections/all/products/cray-fish-by-sam',
        'name': 'Cray Fish (by Sam)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0be04359-be9f-41a8-a23e-1455ed8be95d_300x300.jpg?v=1650649344'
    },
    {
        'id': 418,
        'link': 'https://gimsap.ca/collections/all/products/cray-fish-grinded-by-motherland',
        'name': 'Cray fish (grinded) by Motherland',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_88e43f36-4a9d-4192-af6e-190265432207_300x300.jpg?v=1650649406'
    },
    {
        'id': 419,
        'link': 'https://gimsap.ca/collections/all/products/cray-fish-sultan',
        'name': 'Cray fish (Sultan)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>It is a freshwater crayfish that is usually found in Northern Africa, Western Asia, and Southern Europe. The Sultan Crayfish is typically found in streams, rivers, and lakes. The Sultan Crayfish is typically cooked with a variety of spices.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_898c5052-6c31-4805-b962-81f268f34a9d_300x300.jpg?v=1650649561'
    },
    {
        'id': 420,
        'link': 'https://gimsap.ca/collections/all/products/crayfish-100g',
        'name': 'Crayfish 100g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_03527987-66f0-423e-b6e7-eb02eecb506b_300x300.jpg?v=1645133723'
    },
    {
        'id': 421,
        'link': 'https://gimsap.ca/collections/all/products/crayfish-1lb',
        'name': 'Crayfish 1lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6233965d-0864-4db2-a7b8-bcc35bc1dab9_300x300.jpg?v=1650649669'
    },
    {
        'id': 422,
        'link': 'https://gimsap.ca/collections/all/products/credit-card-fee',
        'name': 'Credit Card Fee',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>For the business owner who wants to reduce their monthly credit card processing fees, this card is the perfect solution. It provides a merchant account and card reader with no monthly fees, a $0.00 per transaction fee, and $0.00 for transactions under $10.00. For transactions over $10.00, the card charges a low rate of 2.5%.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c7e7f5f5-753a-415b-a1bb-a379afca69e5_300x300.jpg?v=1645133728'
    },
    {
        'id': 423,
        'link': 'https://gimsap.ca/collections/all/products/creme-of-nature-argan-oil-intensive-cond-treatment-20oz',
        'name': 'Creme of Nature Argan Oil Intensive Cond. Treatment (20oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.50',
        'description': '<p>The Creme of Nature Argan Oil Intensive Conditioning Treatment is a deep conditioning treatment that restores the natural moisture and sheen of your hair. This product is a leave-in conditioner that contains Moroccan Argan Oil and moisturizing shea butter. It is made to repair damaged hair and restore the health of your hair. This product also has a scent that is reminiscent of the ocean.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_de08ac58-81e9-4901-9c74-c4f0b265df19_300x300.jpg?v=1645133729'
    },
    {
        'id': 424,
        'link': 'https://gimsap.ca/collections/all/products/creme-of-nature-argan-oil-leave-in-conditioner-8-45oz',
        'name': 'Creme of Nature Argan Oil Leave In Conditioner (8.45oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.50',
        'description': '<p>Creme of Nature Argan Oil Leave In Conditioner is a leave-in conditioner that is enriched with the powerful benefits of Argan Oil. It is a lightweight formula that provides your hair with the moisture it needs without weighing it down. With this product, you can avoid dryness and frizz. This product is designed to help maintain a healthy, natural look. It also protects your hair from heat damage. It is made with a pH balanced formula that is safe for color treated hair.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_466f21c1-9a34-401a-ba13-bd57f377655f_300x300.jpg?v=1645133730'
    },
    {
        'id': 425,
        'link': 'https://gimsap.ca/collections/all/products/creme-of-nature-argan-oil-sheen-spray-11-25oz',
        'name': 'Creme of Nature Argan Oil Sheen Spray (11.25oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Creme of Nature Argan Oil Sheen Spray is a light-weight, water-based product that helps to provide shine and luster to the hair. It provides a protective layer to shield hair from environmental damage, and has a pleasant scent. The spray can be used on wet or dry hair. The spray does not contain any alcohol or artificial colors, and is made with natural ingredients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f35fdd25-568e-4b99-8b04-89f79bd95c3f_300x300.jpg?v=1645133731'
    },
    {
        'id': 426,
        'link': 'https://gimsap.ca/collections/all/products/creme-of-nature-detangling-conditioning-shampoo-sunflower-32oz',
        'name': 'Creme of Nature Detangling Conditioning Shampoo [Sunflower] (32oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>This product is a shampoo with a unique formula that includes Sunflower Seed Extract and Soy Protein to help promote hair growth and strengthen hair follicles. This is a moisturizing formula that will not strip the hair of its natural oils, and will leave your hair soft and shiny. The Creme of Nature Detangling Conditioning Shampoo [Sunflower] is a moisturizing shampoo that will not strip the hair of its natural oils.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_40fc40c1-3285-4a33-97c0-6ccd0aead83d_300x300.jpg?v=1645133732'
    },
    {
        'id': 427,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-with-head-10kg',
        'name': 'Croaker Fish (with head) 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e7d17cda-92fd-4b87-ab72-ad82f196676b_300x300.jpg?v=1645133741'
    },
    {
        'id': 428,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-10kg',
        'name': 'Croaker Fish 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_84d382d6-7112-41a9-b3cb-810e43cfca07_300x300.jpg?v=1645133734'
    },
    {
        'id': 429,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-20kg-box',
        'name': 'Croaker Fish 25lb Box Headless',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $240.00',
        'description': '<p>Croaker Fish&nbsp;is the perfect solution for your needs. It is a fresh and sustainable fish that is high in protein and a great source of Omega-3. With a great taste and easy to prepare, this Croaker Fish box is perfect for any occasion.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7051409a-c243-4e3a-b03e-44d8d7cd9ec2_300x300.jpg?v=1645133734'
    },
    {
        'id': 430,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-40lb-box',
        'name': 'Croaker Fish 40lb box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $215.00',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_24809f2b-5803-4b87-a645-dcb719a143bc_300x300.jpg?v=1650650040'
    },
    {
        'id': 431,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-40lb-box-cut',
        'name': 'Croaker Fish 40lb box Cut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $225.00',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2595e70d-f082-4e09-9c40-9a9aec34c9f3_300x300.jpg?v=1650650072'
    },
    {
        'id': 432,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-per-pound-cut-lb',
        'name': 'Croaker Fish per pound  cut (lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_17be9ce8-7712-48dd-8464-6c40c37269df_300x300.jpg?v=1650650095'
    },
    {
        'id': 433,
        'link': 'https://gimsap.ca/collections/all/products/croaker-fish-per-pound-uncut-lb',
        'name': 'Croaker Fish per pound uncut (lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>A delicious deep-sea fish, this fish is a rich source of Omega-3 fatty acids and a great alternative to red meat. Its flesh is white and has a firm texture. The croaker fish can be used in many different dishes, from sushi to croquettes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_936e9361-2db5-4e0e-b93c-b4ebb8afb9ef_300x300.jpg?v=1650650115'
    },
    {
        'id': 434,
        'link': 'https://gimsap.ca/collections/all/products/crochet-wig-cap',
        'name': 'Crochet  wig Cap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Crochet wig caps are made of high quality cotton. They are breathable and easy to care for. These caps are great for wearing over your natural hair to protect it from sun damage, while keeping your style intact. This wig cap can be worn under a hat, as a ponytail holder, or as a headband. They come in many different colors, so you can find one that matches your hair color.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_42f286d4-8ab0-4c56-81f8-db1a201f3b2b_300x300.jpg?v=1645133742'
    },
    {
        'id': 435,
        'link': 'https://gimsap.ca/collections/all/products/crusader-soap',
        'name': 'Crusader Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>The Crusader Soap is a handcrafted soap made from a proprietary blend of vegetable oils, pure essential oils, and natural butters. This soap is gentle on the skin and is enriched with Vitamin E and other natural antioxidants. It is available in four scents: lavender, eucalyptus, sage, and peppermint.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_58c4784f-07ec-48f6-a778-caa5542328f4_300x300.jpg?v=1645133744'
    },
    {
        'id': 436,
        'link': 'https://gimsap.ca/collections/all/products/curry-powder',
        'name': 'Curry Powder',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p><span>Curry Powder is a mixture of ground spices that can be used to flavor a variety of dishes. This is a high quality product that is vegan and gluten-free.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d26627fa-2b17-47bf-8046-e0d8efd3d6ae_300x300.jpg?v=1645133745'
    },
    {
        'id': 437,
        'link': 'https://gimsap.ca/collections/all/products/curry-powder-1kg',
        'name': 'Curry Powder 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Curry Powder is a mixture of ground spices that can be used to flavor a variety of dishes. This is a high quality product that is vegan and gluten-free.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_acd8df74-d9c9-4493-9119-2bbb62c1f646_300x300.jpg?v=1645133746'
    },
    {
        'id': 438,
        'link': 'https://gimsap.ca/collections/all/products/curry-powder-25kg-bag',
        'name': 'Curry powder 25kg bag',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $200.00',
        'description': '<p><span>Curry Powder is a mixture of ground spices that can be used to flavor a variety of dishes. This is a high quality product that is vegan and gluten-free.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fc3d2067-3ab9-4f2f-a626-b6140760b422_300x300.jpg?v=1650650379'
    },
    {
        'id': 439,
        'link': 'https://gimsap.ca/collections/all/products/curry-powder-packed-1-lb',
        'name': 'Curry powder packed (1 lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p><span>Curry Powder is a mixture of ground spices that can be used to flavor a variety of dishes. This is a high quality product that is vegan and gluten-free.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_adc775d4-d171-4f62-9f0e-1d4a983f1018_300x300.jpg?v=1645133748'
    },
    {
        'id': 440,
        'link': 'https://gimsap.ca/collections/all/products/cut-big-whole-chicken-25kg-box',
        'name': 'Cut Big Whole Chicken 25kg box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $100.00',
        'description': "<p>It's whole chicken that has been cut into individual pieces. You can easily cook this chicken for a whole week and have a different meal every night. The pieces are easy to handle and are already skinned and seasoned, so all you have to do is add your favorite spices and get cooking.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a8607f5c-ef4a-4588-bbac-1e76b7988d6c_300x300.jpg?v=1645133750'
    },
    {
        'id': 441,
        'link': 'https://gimsap.ca/collections/all/products/10lb-cut-whole-hard-chicken-bag',
        'name': 'Cut Whole Hard Chicken Bag',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.50',
        'description': '<p><meta charset="utf-8"><span>Sunrise Mature Fowl. Lip smacking, finger licking, taste bud tingling, hand clapping, best tasting chicken ever! This Whole Hard Chicken is perfect for those that love a good chicken sandwich. The chicken is cut in order to be easy to prepare. This is a great way to feed a large family, or for those that want to get ahead of the game and stock up for the future.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at3.40.51PM_300x300.png?v=1647553337'
    },
    {
        'id': 442,
        'link': 'https://gimsap.ca/collections/all/products/cutting-charge',
        'name': 'Cutting charge',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 443,
        'link': 'https://gimsap.ca/collections/all/products/dagaa-1kg-small-fish',
        'name': 'Dagaa 1kg (Small Fish)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p>This is a food product that can be eaten raw or cooked. The Dagaa 1kg (Small Fish) is a type of saltwater fish that is found in coastal waters of West Africa. The Dagaa 1kg (Small Fish) is used in various dishes and is often served with a tomato sauce. The Dagaa 1kg (Small Fish) can be eaten whole or the fish can be deboned.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6a050c2e-3218-40ec-ad47-81014f25292e_300x300.jpg?v=1645133752'
    },
    {
        'id': 444,
        'link': 'https://gimsap.ca/collections/all/products/damato-hair-cream',
        'name': 'Damato Hair Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The Damato Hair Cream is a multi-purpose product that is made for all hair types. It has a conditioning and hydrating effect on the hair and it leaves the hair with a healthy shine. It is formulated with organic ingredients, making it ideal for sensitive skin. The Damato Hair Cream can be used on wet or dry hair and it does not leave a greasy residue. It also contains no sulfates, so it is gentle on the hair. The Damato Hair Cream is vegan and cruelty-free.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_af548a34-75e8-4a5e-970a-8ae0049f6a11_300x300.jpg?v=1645133753'
    },
    {
        'id': 445,
        'link': 'https://gimsap.ca/collections/all/products/damatol-110g',
        'name': 'Damatol 110g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p><span>The Damato Hair Cream is a multi-purpose product that is made for all hair types. It has a conditioning and hydrating effect on the hair and it leaves the hair with a healthy shine. It is formulated with organic ingredients, making it ideal for sensitive skin. The Damato Hair Cream can be used on wet or dry hair and it does not leave a greasy residue. It also contains no sulfates, so it is gentle on the hair. The Damato Hair Cream is vegan and cruelty-free.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1618e8dc-490b-4ba2-aac9-ee09351d0892_300x300.jpg?v=1645133754'
    },
    {
        'id': 446,
        'link': 'https://gimsap.ca/collections/all/products/damatol-hair-cream-55g-x72-box',
        'name': 'Damatol Hair Cream (55g x72) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>The Damato Hair Cream is a multi-purpose product that is made for all hair types. It has a conditioning and hydrating effect on the hair and it leaves the hair with a healthy shine. It is formulated with organic ingredients, making it ideal for sensitive skin. The Damato Hair Cream can be used on wet or dry hair and it does not leave a greasy residue. It also contains no sulfates, so it is gentle on the hair. The Damato Hair Cream is vegan and cruelty-free.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8b3c42c0-5d92-4d4d-bdd2-a18ab49a5983_300x300.jpg?v=1645133756'
    },
    {
        'id': 447,
        'link': 'https://gimsap.ca/collections/all/products/damatol-hair-cream-55g',
        'name': 'Damatol Hair Cream (55g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.50',
        'description': '<p><span>The Damato Hair Cream is a multi-purpose product that is made for all hair types. It has a conditioning and hydrating effect on the hair and it leaves the hair with a healthy shine. It is formulated with organic ingredients, making it ideal for sensitive skin. The Damato Hair Cream can be used on wet or dry hair and it does not leave a greasy residue. It also contains no sulfates, so it is gentle on the hair. The Damato Hair Cream is vegan and cruelty-free.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_38cf06a2-0238-4440-acad-187915760250_300x300.jpg?v=1645133755'
    },
    {
        'id': 448,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-fade-resist',
        'name': 'Dark &amp; Lovely Fade Resist',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Permanent hair dye that leaves your hair shiny and protected.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2c19d91a-46e0-4e68-a7d9-45ae4cd4a4c2_300x300.jpg?v=1650651091'
    },
    {
        'id': 449,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-fade-resist-372',
        'name': 'Dark &amp; Lovely Fade Resist 372',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p><span>Permanent hair dye that leaves your hair shiny and protected.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0ca15753-81d5-4d1f-bb12-4250cb903a29_300x300.jpg?v=1650651163'
    },
    {
        'id': 450,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-for-all-hair',
        'name': 'Dark &amp; Lovely For All Hair',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p><span>Permanent hair dye that leaves your hair shiny and protected.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_1403b0af-8cfc-4425-a998-06ed55b0f486_300x300.jpg?v=1650651205'
    },
    {
        'id': 451,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-hair-color-kit-luminous-blonde',
        'name': 'Dark &amp; Lovely Hair Color Kit Luminous Blonde',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.50',
        'description': '<p><span>Permanent hair dye that leaves your hair shiny and protected.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/81jMe5cAsqL._AC_SS130_300x300.jpg?v=1650652239'
    },
    {
        'id': 452,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-reguler',
        'name': 'Dark &amp; lovely Reguler',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>Made with shea butter, jojoba and avocado oils which helps preserve hair shine, strength, softness and moisture.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/DLSUPER_CLAVIS_TRIPLENOURISH_REGULAR_FRONT_1000X1000_8e5311a9-6cef-42ed-b92a-8548371e3ed7_300x300.jpg?v=1650651591'
    },
    {
        'id': 453,
        'link': 'https://gimsap.ca/collections/all/products/dark-lovely-super',
        'name': 'Dark &amp; Lovely Super',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/files/GIMSAP_Approved_Logo_2_540x.png?v=1606137685'
    },
    {
        'id': 454,
        'link': 'https://gimsap.ca/collections/all/products/dark-and-lovely-leave-in-treatment',
        'name': 'Dark and Lovely (Leave in Treatment)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>This product is a leave-in treatment that provides a moisturizing, nourishing, and refreshing feel to the hair. It can be used as a heat protectant, which will help maintain the integrity of the hair. It is a very versatile product that can be used on any hair type. It can be used to seal split ends, soften, and detangle hair. It is a very popular product among many people.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_71f4e065-e82b-490f-a0f4-2ec867edb622_300x300.jpg?v=1645133758'
    },
    {
        'id': 455,
        'link': 'https://gimsap.ca/collections/all/products/dark-and-lovely-detangler',
        'name': 'DARK and LOVELY DETANGLER',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Dark and Lovely Detangler is a product for those who love their hair to be silky and smooth. It is a blend of Argan Oil, Lavender, and Shea Butter, which help to eliminate tangles and leaves hair smelling nice. This product is perfect for people who love the feeling of soft, manageable hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_81da06b8-d784-418d-9e28-9597bb4f07ca_300x300.jpg?v=1645133757'
    },
    {
        'id': 456,
        'link': 'https://gimsap.ca/collections/all/products/dark-and-lovely-no-mistake',
        'name': 'Dark And Lovely No Mistake',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>For a natural look, try Dark And Lovely No Mistake. This product comes in an array of colors, from subtle to bold. It provides a natural look with a rich, deep color that lasts. This product can be used for both hair and skin.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_610361cf-e56a-417d-a392-40ca4772c3d7_300x300.jpg?v=1645133759'
    },
    {
        'id': 457,
        'link': 'https://gimsap.ca/collections/all/products/dawa-dawa',
        'name': 'Dawa Dawa',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Made out of fermented locust beans with a sticky texture. Contains vitamin C, phosphorous and potassium.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3e6ffb87-00df-4dcb-8660-909a9dca36d5_300x300.jpg?v=1645133767'
    },
    {
        'id': 458,
        'link': 'https://gimsap.ca/collections/all/products/dawa-dawa-5pcs-flat',
        'name': 'Dawa Dawa (5pcs) Flat',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.75',
        'description': '<p><span>Made out of fermented locust beans with a sticky texture. Contains vitamin C, phosphorous and potassium.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2121ac1c-6c96-4c80-8d64-d5c7f18f6c1a_300x300.jpg?v=1650652494'
    },
    {
        'id': 459,
        'link': 'https://gimsap.ca/collections/all/products/dax-bees-wax',
        'name': 'Dax Bees Wax',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Dax Bees Wax is a natural, pure and unfiltered beeswax. It is derived from the honeycomb, where it is collected from the honeycomb cells, dried and cleaned. The Dax Bees Wax is a pure white, odorless, soft and pliable. It is an excellent base for lip balms, skin care products, and many other applications.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_25c136ce-8611-4e93-8be6-a1fcfed7cd4b_300x300.jpg?v=1645133769'
    },
    {
        'id': 460,
        'link': 'https://gimsap.ca/collections/all/products/dax-curling-wax',
        'name': 'Dax Curling Wax',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Dax Curling Wax is a brand of professional salon grade hair care products for both men and women. Dax Curling Wax has been designed to provide a strong hold and brilliant shine to all hair types. The wax contains natural beeswax, lanolin, and vitamin E to ensure a healthy, shiny finish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d27534b8-330c-4a33-9213-fda9b31e1ebe_300x300.jpg?v=1645133770'
    },
    {
        'id': 461,
        'link': 'https://gimsap.ca/collections/all/products/dax-indian-hemp-14oz',
        'name': 'DAX Indian Hemp (14oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': "<p>DAX Indian Hemp is a high-quality, all-natural soap that will leave your skin feeling silky smooth. This soap is made with organic oils and natural herbs, so it's gentle on your skin and the environment.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8916557c-a02a-4ab4-9520-0bdadb7eeb46_300x300.jpg?v=1645133771'
    },
    {
        'id': 462,
        'link': 'https://gimsap.ca/collections/all/products/dax-kocatah-dry-scalp-relief',
        'name': 'Dax Kocatah Dry Scalp Relief',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Dax Kocatah Dry Scalp Relief is a product that is meant to soothe and relieve the dry scalp. The dry scalp relief has a formula that is made up of natural ingredients that are safe for the scalp. The product also has a nice, fresh scent. The Dax Kocatah Dry Scalp Relief can be used as a hair conditioner or as a leave-in conditioner. The product is also dermatologist-tested and is recommended for people with sensitive skin.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_18940706-811b-4577-94cc-aef74a2136ac_300x300.jpg?v=1645133772'
    },
    {
        'id': 463,
        'link': 'https://gimsap.ca/collections/all/products/dax-pomade-14oz',
        'name': 'DAX Pomade (14oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>DAX Pomade is a water-based pomade made from natural ingredients. This product can be used to style hair and can also be used as a skin moisturizer. The water-based formula is perfect for a variety of hair types, including curly, frizzy, and straight. The pomade will hold all day without feeling heavy or greasy. It is made from natural ingredients including avocado oil, coconut oil, jojoba oil, beeswax, and shea butter. DAX Pomade has a subtle vanilla and citrus scent.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7866c38b-fcfc-4c2d-9dc1-685a97cd03c5_300x300.jpg?v=1645133773'
    },
    {
        'id': 464,
        'link': 'https://gimsap.ca/collections/all/products/de-chosen-ground-achi',
        'name': 'De Chosen Ground Achi',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>De Chosen Ground Achi is a new coffee company that is based in Austin, Texas. They offer high-quality coffee beans and coffee blends. They also offer coffee beans that are sourced from different regions around the world. This includes Central America, South America, Africa, Asia, and Europe. Their blends include Colombian, Colombian Decaf, Ethiopian, Ethiopian Decaf, French Roast, and French Roast Decaf.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_98460279-7b0d-4a23-924f-4100f2dae925_300x300.jpg?v=1645133775'
    },
    {
        'id': 465,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-210g',
        'name': 'De Rica 210g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_34f44131-92aa-4c50-b518-4d709ec0ebf6_300x300.jpg?v=1645133779'
    },
    {
        'id': 466,
        'link': 'https://gimsap.ca/collections/all/products/derica-2200g',
        'name': 'De rica 2200g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.00',
        'description': '<p data-mce-fragment="1">De Rica is a&nbsp;concentrated tomato paste.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_159a596c-afb6-4760-a135-19a93f9a70b2_300x300.jpg?v=1645133780'
    },
    {
        'id': 467,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-24x210g-box',
        'name': 'De Rica 24x210g (Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_a5db3855-d067-4462-bf37-cf0a60435b08_300x300.jpg?v=1650652781'
    },
    {
        'id': 468,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-24x400g-box',
        'name': 'De Rica 24x400g (Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_87379f77-a682-471a-9526-c5b10d163f15_300x300.jpg?v=1650652799'
    },
    {
        'id': 469,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-400g',
        'name': 'De Rica 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a49189d2-7e70-4017-bc71-7dbfc7b9cc44_300x300.jpg?v=1645133783'
    },
    {
        'id': 470,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-70g',
        'name': 'de rica 70g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cf674ffa-f98c-43a8-b948-7004c92d86d3_300x300.jpg?v=1645133784'
    },
    {
        'id': 471,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-70g-sachet',
        'name': 'De rica 70g sachet',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b6af626a-9013-42f8-b00e-3d088aace328_300x300.jpg?v=1645133785'
    },
    {
        'id': 472,
        'link': 'https://gimsap.ca/collections/all/products/de-rica-850g',
        'name': 'De Rica 850g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>De Rica is a&nbsp;concentrated tomato paste.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c2048621-47f7-482e-95c9-1b9cd0c812f1_300x300.jpg?v=1645133787'
    },
    {
        'id': 473,
        'link': 'https://gimsap.ca/collections/all/products/delta-soap',
        'name': 'Delta Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>The scent of the clean, crisp, and fresh-smelling soap is reminiscent of the feeling of a cool ocean breeze. The soap is made with the natural ingredient, olive oil, which leaves your skin feeling smooth and moisturized.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d8fc549f-7c5d-469c-9fd0-9bfe284901d9_300x300.jpg?v=1645133777'
    },
    {
        'id': 474,
        'link': 'https://gimsap.ca/collections/all/products/demert-wig-weave-spray',
        'name': 'DeMert Wig &amp; Weave Spray',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Can be used on natural and synthetic hair, prevents color fading and dies quickly.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9d6f9d86-508b-4de9-bb96-f1811beaa3db_300x300.jpg?v=1650653280'
    },
    {
        'id': 475,
        'link': 'https://gimsap.ca/collections/all/products/dermovate-cream-25g',
        'name': 'Dermovate Cream 25g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<p>Dermovate Cream is a prescription medication for the treatment of eczema. Dermovate Cream should be applied once or twice a day to the affected area and rubbed in gently.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9c2489d8-a552-4ec2-9bf8-008e2899dfe9_300x300.jpg?v=1650653351'
    },
    {
        'id': 476,
        'link': 'https://gimsap.ca/collections/all/products/dettol-250ml',
        'name': 'Dettol 250ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world. Dettol 250ml is the perfect size for home use.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_5d094919-a43f-4135-8a26-100058dd113f_300x300.jpg?v=1650653496'
    },
    {
        'id': 477,
        'link': 'https://gimsap.ca/collections/all/products/dettol-75ml-liquid-bottle',
        'name': 'Dettol 75mL Liquid Bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/8870588317726_1280x_6f627793-6c4d-4182-82fb-dae3c038282e_300x300.webp?v=1650653634'
    },
    {
        'id': 478,
        'link': 'https://gimsap.ca/collections/all/products/dettol-anti-bacteria-bar-soap',
        'name': 'Dettol Anti Bacteria Bar Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Dettol Anti-Bacteria Bar Soap provides a gentle, yet powerful clean that fights bacteria. This soap is great for a variety of skin types, including sensitive skin. It is also a great choice for children, and comes in a refreshing scent. The soap is enriched with emollients and conditioners that provide deep hydration and protection. It leaves skin feeling clean and fresh.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_80037a56-f32b-42fe-ad41-aaa6799b900b_300x300.jpg?v=1645133792'
    },
    {
        'id': 479,
        'link': 'https://gimsap.ca/collections/all/products/dettol-anti-bacteria-bar-soap-3-pcs',
        'name': 'Dettol Anti Bacteria Bar Soap (3 pcs)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Dettol Anti-Bacteria Bar Soap provides a gentle, yet powerful clean that fights bacteria. This soap is great for a variety of skin types, including sensitive skin. It is also a great choice for children, and comes in a refreshing scent. The soap is enriched with emollients and conditioners that provide deep hydration and protection. It leaves skin feeling clean and fresh.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_1d3d0f36-fd0f-41ae-ba3e-69862e6b5314_300x300.jpg?v=1650653738'
    },
    {
        'id': 480,
        'link': 'https://gimsap.ca/collections/all/products/dettol-liquid-1-litre',
        'name': 'Dettol Liquid 1 Litre',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_e1a6a288-ee07-44fc-a821-c5a1946328bc_300x300.jpg?v=1650653794'
    },
    {
        'id': 481,
        'link': 'https://gimsap.ca/collections/all/products/dettol-liquid-1-litre-box',
        'name': 'Dettol Liquid 1 Litre Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b00d6a16-d898-4d76-a0ae-c5e922b49e56_300x300.jpg?v=1650653819'
    },
    {
        'id': 482,
        'link': 'https://gimsap.ca/collections/all/products/dettol-liquid-500ml',
        'name': 'Dettol Liquid 500ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9b0952de-5ae6-4375-800b-64120b74596a_300x300.jpg?v=1650653847'
    },
    {
        'id': 483,
        'link': 'https://gimsap.ca/collections/all/products/dettol-liquid-550ml',
        'name': 'Dettol Liquid 550ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_046298ed-e7f7-4178-a565-9a44f8f43e93_300x300.jpg?v=1650653886'
    },
    {
        'id': 484,
        'link': 'https://gimsap.ca/collections/all/products/digestive',
        'name': 'digestives',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p><span>The chocolate-covered digestive biscuits are a great way to end a meal and satisfy any chocolate cravings.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_26c82316-0052-464a-9b88-0b37bbabc791_300x300.jpg?v=1645133800'
    },
    {
        'id': 485,
        'link': 'https://gimsap.ca/collections/all/products/digestifs-box-20x400g',
        'name': 'Digestives Box 20x400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This box of Digestives contains 20 individual packets of 400g of chocolate-covered digestive biscuits. The Digestives Box is perfect for a party of any size, and is a great addition to any candy buffet. The chocolate-covered digestive biscuits are a great way to end a meal and satisfy any chocolate cravings.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a8424630-0e90-4afc-9dc1-d0e50299106a_300x300.jpg?v=1645133799'
    },
    {
        'id': 486,
        'link': 'https://gimsap.ca/collections/all/products/djama-djama-bened-22x700g-box',
        'name': 'Djama Djama (Bened 22x700g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': "<p>Djama Djama is a delicious and authentic Moroccan stew made with lamb, chickpeas, and a blend of fragrant spices. This dish is also a great choice for dinner parties, potlucks, and other social gatherings. Djama Djama is an excellent dish to serve with warm bread, couscous, or rice. Djama Djama is also gluten-free and can be made vegan by substituting vegetable broth for the water. It's also a great choice for a dinner party because it can be made in advance and refrigerated until you're ready to serve it.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2229dcaa-2b61-4d82-87ea-e40c25d66ab6_300x300.jpg?v=1650654180'
    },
    {
        'id': 487,
        'link': 'https://gimsap.ca/collections/all/products/djama-djama-bened-700g',
        'name': 'Djama Djama (Bened) 700g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': "<p>Djama Djama is a delicious and authentic Moroccan stew made with lamb, chickpeas, and a blend of fragrant spices. This dish is also a great choice for dinner parties, potlucks, and other social gatherings. Djama Djama is an excellent dish to serve with warm bread, couscous, or rice. Djama Djama is also gluten-free and can be made vegan by substituting vegetable broth for the water. It's also a great choice for a dinner party because it can be made in advance and refrigerated until you're ready to serve it.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_e3a0f91a-8f69-43ee-8aea-f2fd60b3520b_300x300.jpg?v=1650654288'
    },
    {
        'id': 488,
        'link': 'https://gimsap.ca/collections/all/products/djassan-akpi',
        'name': 'Djassan/Akpi',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Djassan/Akpi is not only used for cooking because it is rich in protein, potassium and fat but it is also good for the skin and face.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f7da0f2b-d126-4b1c-ad12-12d3d7bafa93_300x300.jpg?v=1645133803'
    },
    {
        'id': 489,
        'link': 'https://gimsap.ca/collections/all/products/donkwa',
        'name': 'Donkwa',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': "<p>A savory snack that's made from cornmeal and peanuts.</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_90958de5-19b7-40dd-8f69-931daa534c02_300x300.jpg?v=1650654755'
    },
    {
        'id': 490,
        'link': 'https://gimsap.ca/collections/all/products/donkwa-apexol',
        'name': 'Donkwa (Apexol)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p><span>A savory snack that's made from cornmeal and peanuts.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cfd13334-3a76-4d46-9c70-a157274621dc_300x300.jpg?v=1650654769'
    },
    {
        'id': 491,
        'link': 'https://gimsap.ca/collections/all/products/donkwa-powder-lb',
        'name': 'Donkwa Powder /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p><span>A savory snack that's made from cornmeal and peanuts in powder form.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_17b96e83-639f-434e-93dc-3ef14e045ff9_300x300.jpg?v=1650654877'
    },
    {
        'id': 492,
        'link': 'https://gimsap.ca/collections/all/products/donkwa-rolled-cookie-lb',
        'name': 'Donkwa Rolled + Cookie /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p><span>A savory snack that's made from cornmeal and peanuts.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4773eaef-eb4a-4e92-be19-5c28028ac0e0_300x300.jpg?v=1650656672'
    },
    {
        'id': 493,
        'link': 'https://gimsap.ca/collections/all/products/doo-gro-triple-strength-growth-detangler',
        'name': 'Doo Gro (Triple Strength Growth Detangler)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.99',
        'description': '<p>Doo Gro is a hair detangler that contains vitamin E and jojoba oil to strengthen hair. The triple strength formula works to provide a gentle yet effective detangling treatment for dry, brittle hair. The detangler also provides protection against breakage, heat styling, and UV rays.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_28e5c5f6-507d-42a8-92a3-295c7a81733e_300x300.jpg?v=1650656741'
    },
    {
        'id': 494,
        'link': 'https://gimsap.ca/collections/all/products/doo-gro-oil',
        'name': 'Doo gro oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Doo gro oil is a brand of beauty oil that is formulated to provide deep moisturizing and conditioning to the skin. It is made with 100% natural ingredients, and is safe for all skin types. Doo gro oil is also a great way to fight acne, since it is made with essential oils that have natural anti-inflammatory properties.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f6b887cb-324c-48ae-bfe0-5afa943951fa_300x300.jpg?v=1645133808'
    },
    {
        'id': 495,
        'link': 'https://gimsap.ca/collections/all/products/dr-johnsons-500ml-antiseptic-disinfectant-dettol',
        'name': "Dr. Johnson's 500mL Antiseptic Disinfectant (Dettol)",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p><span>Dettol is a leading brand of antiseptic liquid. It kills germs on the skin and in the air. It has been trusted for over 80 years by millions of people around the world.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_f634ee6e-96d9-4c03-8755-442d01a98afe_300x300.jpg?v=1650656888'
    },
    {
        'id': 496,
        'link': 'https://gimsap.ca/collections/all/products/dream-kids-anti-breakage-detangling-oil-moisturizer-8oz',
        'name': 'Dream Kids Anti-Breakage Detangling Oil Moisturizer (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>Dream Kids Anti-Breakage Detangling Oil Moisturizer is a new product from Dream Kids. It is a product that is specially formulated for children to help prevent breakage and dryness in their hair. The product contains three key ingredients, jojoba oil, argan oil, and olive oil. The oil is then mixed with Vitamin E, Shea Butter, and Aloe Vera to create a moisturizing oil that will help to keep hair looking healthy and hydrated.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_71b025e4-c427-4b50-8740-e2a5a6322515_300x300.jpg?v=1645133810'
    },
    {
        'id': 497,
        'link': 'https://gimsap.ca/collections/all/products/dream-kids-detangler-miracle',
        'name': 'Dream Kids Detangler Miracle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Dream Kids Detangler Miracle is a perfect product for kids who are getting ready for school. It’s a detangler that will make your child’s hair easier to comb through. This product is non-greasy and smells like vanilla. It is also safe for children, so there is no need to worry about it getting in their eyes. Dream Kids Detangler Miracle is perfect for kids who have long hair, curly hair, or wavy hair.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c4a3b83c-4c23-4133-930a-7f80df624954_300x300.jpg?v=1645133812'
    },
    {
        'id': 498,
        'link': 'https://gimsap.ca/collections/all/products/dream-kids-olive-miracle',
        'name': 'Dream Kids Olive Miracle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': "<p>Dream Kids Olive Miracle is a natural, healing lotion that contains olive oil, vitamin E, and pure honey. The olive oil in the lotion provides deep moisturizing, while the vitamin E and honey work to soothe and heal. Dream Kids Olive Miracle is made with a non-GMO and vegan formula, and it is 100% natural. This lotion is ideal for children of all ages, and it is safe to use on sensitive skin. Dream Kids Olive Miracle has a light, natural scent, and it can be used on a child's face, hands, or any other part of the body.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_47203564-9616-4989-be8e-82b2e6c898ba_300x300.jpg?v=1645133814'
    },
    {
        'id': 499,
        'link': 'https://gimsap.ca/collections/all/products/deam-kids-relaxer-1-application',
        'name': 'Dream Kids Relaxer 1 Application',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Dream Kids Relaxer 1 Application is a product designed for children to make them feel more comfortable when using relaxer products. This product comes in a box with instructions for use on adults as well.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4f0a897b-255b-410c-ac5a-1425e96ee103_300x300.jpg?v=1645133774'
    },
    {
        'id': 500,
        'link': 'https://gimsap.ca/collections/all/products/dream-kids-soothing-moisturizing-braid-spray-12oz',
        'name': 'Dream Kids Soothing Moisturizing Braid Spray (12oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>Dream Kids Soothing Moisturizing Braid Spray is a braid spray that is designed to be used to prevent hair breakage and ease discomfort of dry, itchy scalp. The spray has a refreshing and relaxing lavender scent that provides relief from dry scalp. The spray is made from natural ingredients, including aloe vera, chamomile, rosemary, lavender, and grapefruit. It is perfect for kids who are too young to apply lotion to their scalp.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b3208473-b6ca-408f-bd4b-23c717ab465f_300x300.jpg?v=1645133816'
    },
    {
        'id': 501,
        'link': 'https://gimsap.ca/collections/all/products/dreamkids-childrens-relaxer',
        'name': "DreamKids Children''s Relaxer",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': "<p>DreamKids Children's Relaxer is a hair relaxer for children. It is a gentle and easy to use formula that is formulated to make the hair easier to comb and less likely to tangle. It also eliminates the frizz and fly away that children often experience. The conditioner is formulated with natural oils that moisturize the hair and prevent breakage. DreamKids Children's Relaxer is gentle enough for children as young as two years old.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a67bbbbc-2146-4a2c-a4d0-4d551bb1436a_300x300.jpg?v=1645133811'
    },
    {
        'id': 502,
        'link': 'https://gimsap.ca/collections/all/products/dreamkids-relaxer',
        'name': 'DreamKids Relaxer',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': "<p>DreamKids Relaxer is a hair relaxer specifically designed for children's hair. It is formulated with ingredients that are gentle on the hair and scalp, while still delivering the desired results. The product is designed to be applied to the hair without the need for rinsing. DreamKids Relaxer will leave your child's hair looking healthier and smoother, while also providing protection against damage. The product is also designed to not leave a strong smell in your child's hair.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_63f73b49-3d8a-4fc7-915f-16436f10c2c8_300x300.jpg?v=1645133814'
    },
    {
        'id': 503,
        'link': 'https://gimsap.ca/collections/all/products/dried-bitter-leaf-lb',
        'name': 'Dried Bitter Leaf',
        'price': 'From $5.00',
        'description': '<p>Dried Bitter Leaf is a highly sought after ingredient. The name of the leaf is often associated with the name of the herb, and the herb is often used to flavor foods. It is often used in fish dishes and it is said to have a delicate flavor.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f1c7e4a5-4fc5-4b4f-9c50-ac7830c39083_300x300.jpg?v=1645133817'
    },
    {
        'id': 504,
        'link': 'https://gimsap.ca/collections/all/products/dried-catfish-apexol',
        'name': 'Dried Catfish (Apexol)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p><span>For those who are looking for a new and exciting dish to try, you will want to give this dried catfish a try. The catfish is seasoned with a blend of herbs and spices, making it taste great. The fish is also easy to prepare, and cooks in just minutes. This catfish can be served with rice, pasta, or any other side dish. It is also an excellent source of protein and contains zero carbohydrates. The fish can be used in a variety of dishes including soups, salads, and more.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_a976b656-9286-4561-b5ef-c7707b09bf3e_300x300.jpg?v=1650657226'
    },
    {
        'id': 505,
        'link': 'https://gimsap.ca/collections/all/products/dried-catfish-frozen',
        'name': 'Dried Catfish (Frozen)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': "<p>Frozen catfish, known for its lean and tasty meat, is perfect for those looking for a low-fat, low-calorie meal. Our catfish are caught in the wild and are then frozen to preserve the freshness and natural flavor. Once you've prepared the fish, it can be stored in the freezer for up to six months. The product is available in bulk and is perfect for restaurants and food service providers.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0338b6c1-5a33-46f3-abe9-812b73290a3a_300x300.jpg?v=1650657465'
    },
    {
        'id': 506,
        'link': 'https://gimsap.ca/collections/all/products/dried-catfish-seasoned-525g',
        'name': 'Dried Catfish Seasoned 525g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $28.00',
        'description': '<p>For those who are looking for a new and exciting dish to try, you will want to give this dried catfish a try. The catfish is seasoned with a blend of herbs and spices, making it taste great. The fish is also easy to prepare, and cooks in just minutes. This catfish can be served with rice, pasta, or any other side dish. It is also an excellent source of protein and contains zero carbohydrates. The fish can be used in a variety of dishes including soups, salads, and more.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_bbfb7167-dcb4-4c9b-a2fb-b4ae5376d1cc_300x300.jpg?v=1650657502'
    },
    {
        'id': 507,
        'link': 'https://gimsap.ca/collections/all/products/dried-croaker-fish-eja-apo-lb',
        'name': 'Dried Croaker Fish (Eja Apo) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $24.00',
        'description': '<p>The fish is used for making various dishes, most notably fish soup. It is often served as a snack or appetizer. The Dried Croaker Fish (Eja Apo) is a good source of protein and omega-3 fatty acids. It is rich in iron, phosphorus, potassium, and selenium. It is low in calories and contains no cholesterol. The Dried Croaker Fish (Eja Apo) can be prepared in a variety of ways. It can be fried, boiled, baked, or roasted. It can be served with salt, lemon, or spices.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_74a3c49d-acfe-477e-bdc5-f9d2e22558f5_300x300.jpg?v=1650657781'
    },
    {
        'id': 508,
        'link': 'https://gimsap.ca/collections/all/products/dried-open-cat-fish-box-15kg',
        'name': 'Dried Open Cat Fish Box (15kg)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $380.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_08a216c1-dc29-402a-861a-2bd9669ab43e_300x300.jpg?v=1650657968'
    },
    {
        'id': 509,
        'link': 'https://gimsap.ca/collections/all/products/dried-panla-whiting-fish-pack',
        'name': 'Dried panla (whiting) fish pack',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>They are a small, oval-shaped fish that are typically dried and packaged for consumption. A pack of dried panla fish contains five servings. It is an excellent source of protein and contains a variety of nutrients. Panla fish are a popular addition to many dishes, including soup, adobo, and pinakbet. The most important part of the fish is the head, which is why it is often left on when being dried. Panla fish have a mild flavor and a texture that is firm and flaky. It is not recommended to cook panla fish before it has been dried because it will make the meat go bad. The best way to eat this type of fish is to simply soak it in water for a few minutes before cooking it in any dish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b3f14fa4-8fb7-4bde-8148-cc1a4627384a_300x300.jpg?v=1650658167'
    },
    {
        'id': 510,
        'link': 'https://gimsap.ca/collections/all/products/dried-shrimp',
        'name': 'Dried Shrimp',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Dried shrimp are small, brownish crustaceans that have been cooked in salt and sugar. They are then left to dry for a few days before being packaged. Dried shrimp are available in a variety of sizes, shapes, and flavors. The most common varieties are dried shrimp that are curled and dried shrimp that are straight. They are usually sold in bulk and are eaten whole or chopped up. They can be eaten by themselves or added to soups, salads, and stir-fries.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_4cd486c2-45f9-4605-88b2-1a1561430357_300x300.jpg?v=1650658269'
    },
    {
        'id': 511,
        'link': 'https://gimsap.ca/collections/all/products/dried-shrimp-naija-lb',
        'name': 'Dried Shrimp (Naija) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p>Dried shrimp are small, brownish crustaceans that have been cooked in salt and sugar. They are then left to dry for a few days before being packaged. Dried shrimp are available in a variety of sizes, shapes, and flavors. The most common varieties are dried shrimp that are curled and dried shrimp that are straight. They are usually sold in bulk and are eaten whole or chopped up. They can be eaten by themselves or added to soups, salads, and stir-fries.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_997ded79-82a4-40a3-bdf6-9fc968fbdefa_300x300.jpg?v=1650658366'
    },
    {
        'id': 512,
        'link': 'https://gimsap.ca/collections/all/products/dried-shrimps-1lb',
        'name': 'dried shrimps 1lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $38.00',
        'description': '<p>Dried shrimp are small, brownish crustaceans that have been cooked in salt and sugar. They are then left to dry for a few days before being packaged. Dried shrimp are available in a variety of sizes, shapes, and flavors. The most common varieties are dried shrimp that are curled and dried shrimp that are straight. They are usually sold in bulk and are eaten whole or chopped up. They can be eaten by themselves or added to soups, salads, and stir-fries.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_bdce0171-31e5-407b-883a-b843ff7897bf_300x300.jpg?v=1650658409'
    },
    {
        'id': 513,
        'link': 'https://gimsap.ca/collections/all/products/dried-smoked-catfish-cut-20kg-box',
        'name': 'Dried smoked Catfish (cut) 20kg Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $750.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_fbb482d7-8b4b-4e3f-a4ea-68d9e34074ac_300x300.jpg?v=1650658461'
    },
    {
        'id': 514,
        'link': 'https://gimsap.ca/collections/all/products/dried-smoked-catfish-whole-20kg-box',
        'name': 'Dried smoked Catfish (whole) 20kg Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $750.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_61684805-d369-40b9-81b9-c0a0e72a1c24_300x300.jpg?v=1650658492'
    },
    {
        'id': 515,
        'link': 'https://gimsap.ca/collections/all/products/dried-smoked-cutfish-oje-20kg-box',
        'name': 'Dried smoked Cutfish (oje) 20kg Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $650.00',
        'description': '<p>Crayfish are typically a reddish-brown color, with a broad, flat body. They have a large head and claws on the front of their body. They have two pairs of antennae and seven pairs of jointed legs.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_2e0f99f4-aae4-444c-9578-2e2f3b8a1a48_300x300.jpg?v=1650658514'
    },
    {
        'id': 516,
        'link': 'https://gimsap.ca/collections/all/products/dried-ukazi-lb',
        'name': 'Dried Ukazi (lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p>Ukazi is a fruit with a pleasant sweet taste. The fruit is dried to maintain its color and provide a long shelf life. This is an excellent choice for snacking and adding to a dish to provide some sweetness.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_63cf5b74-ce9a-43f4-8f47-c0221a4c7eb4_300x300.jpg?v=1650658549'
    },
    {
        'id': 517,
        'link': 'https://gimsap.ca/collections/all/products/drum-brown-beans-50lbs-todaj',
        'name': 'Drum Brown Beans 50lbs (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $120.00',
        'description': '<p>The Drum Brown Beans 50lbs (Todaj) are the perfect addition to any pantry. The Drum Brown Beans are an excellent source of protein, iron, and zinc. They also have a mild flavor and can be cooked with any meat, vegetable, or sauce. They are also vegan and gluten-free. The Drum Brown Beans 50lbs (Todaj) are a great option for any household.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_551216c1-9098-442a-8720-8e8f8d032148_300x300.jpg?v=1650658624'
    },
    {
        'id': 518,
        'link': 'https://gimsap.ca/collections/all/products/dry-cassaav-fufu-8lb',
        'name': 'Dry Cassaav Fufu 8lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Dry Cassava Fufu is a light, crispy cassava meal that is served as a side dish or to accompany a main dish. It is made from finely grated cassava, a starchy root vegetable that is low in fat and calories. The Cassava Fufu can be made in just minutes and is great for anyone who needs to eat gluten-free or is following a vegan diet.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f4af8495-6352-4710-9381-72f91da6491a_300x300.jpg?v=1650659073'
    },
    {
        'id': 519,
        'link': 'https://gimsap.ca/collections/all/products/dry-catfish-pack-nigeria',
        'name': 'Dry Catfish pack (Nigeria)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': '<p>Dry Catfish is a natural source of protein, omega-3 fatty acids, and many other nutrients. It is perfect for cooking and it is also easy to eat and digest. This package contains 5 pounds of dry catfish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4b5ab12b-0568-4172-a409-3258c0f66f6e_300x300.jpg?v=1650659243'
    },
    {
        'id': 520,
        'link': 'https://gimsap.ca/collections/all/products/dry-fish-lb',
        'name': 'Dry Fish /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>The fish is fresh and from the Pacific Ocean. The company is sustainable and offers a variety of fresh fish. It has been voted best for customer service, and it provides top quality service. The fish is fresh and comes from the Pacific Ocean. The company is sustainable and offers a variety of fresh fish. It has been voted best for customer service, and it provides top quality service.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f786a5c0-b778-48d5-8825-cacf679d12eb_300x300.jpg?v=1645133837'
    },
    {
        'id': 521,
        'link': 'https://gimsap.ca/collections/all/products/dry-green-peas-1-7-lb',
        'name': 'Dry Green Peas 1.7 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Tasty, healthy, and versatile, dry green peas are a great addition to any meal. They can be used in any dish that requires a grain or bean, such as soups, stews, salads, and stir-fries. They are high in protein and fiber, low in fat, and contain essential vitamins and minerals.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1a2ea9a3-11d0-47fd-8664-e79804af7b3e_300x300.jpg?v=1645133838'
    },
    {
        'id': 522,
        'link': 'https://gimsap.ca/collections/all/products/dry-scent-leaves-lb',
        'name': 'Dry Scent Leaves /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>With its aromatic taste, Dry Scent leaves are mostly used as spice for cooking delicacies.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a24908a5-f9b8-4e4e-8a82-0bc72909f3ad_300x300.jpg?v=1645133839'
    },
    {
        'id': 523,
        'link': 'https://gimsap.ca/collections/all/products/dry-utazi-leaves-lb',
        'name': 'Dry Utazi Leaves /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Dry Utazi Leaves, which are also known as wild spinach, are perfect for salads, soups, or to be eaten as a side dish. These leaves are packed with antioxidants and protein. These leaves are best served as a salad, a soup, or eaten as a side dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_04bae9c1-39b9-4fc8-abc0-3c2ded50bff3_300x300.jpg?v=1650660116'
    },
    {
        'id': 524,
        'link': 'https://gimsap.ca/collections/all/products/dry-uziza-leaf-lb',
        'name': 'Dry Uziza Leaf /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Dry Uziza Leaf is a long leafed plant that is part of the pepper family. The leaves are dark green in color and are very fragrant. The leaves are ground into a powder and used as a spice in many dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_155fad10-5365-4955-a468-6a51e3dc7c03_300x300.jpg?v=1650660175'
    },
    {
        'id': 525,
        'link': 'https://gimsap.ca/collections/all/products/du-rag',
        'name': 'Du Rag',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': 'A cloth used to cover your head to protect your hairstyle.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bdf07435-259e-4f7e-9721-a544ce238b94_300x300.jpg?v=1645133857'
    },
    {
        'id': 526,
        'link': 'https://gimsap.ca/collections/all/products/ducros-curry-powder-250g',
        'name': 'Ducros curry powder 250g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This curry powder is perfect for any curry lover. It is an aromatic blend of spices, including coriander, cumin, turmeric, fenugreek, cinnamon, and red pepper. The powder is rich in turmeric, which has been shown to have many health benefits. This spice can help improve the immune system, relieve inflammation, and provide relief from digestive issues. This blend is the perfect mix of sweet and spicy. It is a great addition to your pantry and can be used in any dish you desire.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1ab7b724-2e94-4a98-bc75-7d5ec4e12dec_300x300.jpg?v=1645133842'
    },
    {
        'id': 527,
        'link': 'https://gimsap.ca/collections/all/products/ducros-curry-powder-250g-x-40',
        'name': 'Ducros curry powder 250g x 40',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>This curry powder is perfect for any curry lover. It is an aromatic blend of spices, including coriander, cumin, turmeric, fenugreek, cinnamon, and red pepper. The powder is rich in turmeric, which has been shown to have many health benefits. This spice can help improve the immune system, relieve inflammation, and provide relief from digestive issues. This blend is the perfect mix of sweet and spicy. It is a great addition to your pantry and can be used in any dish you desire.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6eb5a847-a910-4bed-9e83-e42a596c713f_300x300.jpg?v=1645133843'
    },
    {
        'id': 528,
        'link': 'https://gimsap.ca/collections/all/products/ducros-curry-powder-25g',
        'name': 'Ducros Curry Powder 25g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.00',
        'description': '<p><span>This curry powder is perfect for any curry lover. It is an aromatic blend of spices, including coriander, cumin, turmeric, fenugreek, cinnamon, and red pepper. The powder is rich in turmeric, which has been shown to have many health benefits. This spice can help improve the immune system, relieve inflammation, and provide relief from digestive issues. This blend is the perfect mix of sweet and spicy. It is a great addition to your pantry and can be used in any dish you desire.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_543bffb9-6b68-45bd-a74e-d96a171381b6_300x300.jpg?v=1645133844'
    },
    {
        'id': 529,
        'link': 'https://gimsap.ca/collections/all/products/ducros-curry-powder-25g-12x12-box',
        'name': 'Ducros Curry Powder 25g (12x12 Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>This curry powder is perfect for any curry lover. It is an aromatic blend of spices, including coriander, cumin, turmeric, fenugreek, cinnamon, and red pepper. The powder is rich in turmeric, which has been shown to have many health benefits. This spice can help improve the immune system, relieve inflammation, and provide relief from digestive issues. This blend is the perfect mix of sweet and spicy. It is a great addition to your pantry and can be used in any dish you desire.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_726f929d-04d0-4d51-96cc-3f22ad11c636_300x300.jpg?v=1645133846'
    },
    {
        'id': 530,
        'link': 'https://gimsap.ca/collections/all/products/ducros-curry-powder-500g',
        'name': 'Ducros curry powder 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.00',
        'description': '<p><span>This curry powder is perfect for any curry lover. It is an aromatic blend of spices, including coriander, cumin, turmeric, fenugreek, cinnamon, and red pepper. The powder is rich in turmeric, which has been shown to have many health benefits. This spice can help improve the immune system, relieve inflammation, and provide relief from digestive issues. This blend is the perfect mix of sweet and spicy. It is a great addition to your pantry and can be used in any dish you desire.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_75c84e71-6fab-43c5-b874-5a475f491cc3_300x300.jpg?v=1650664490'
    },
    {
        'id': 531,
        'link': 'https://gimsap.ca/collections/all/products/ducros-dried-thyme-10g',
        'name': 'Ducros Dried Thyme 10g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.00',
        'description': '<p><span>This box of Ducros thyme is a fantastic herb to use in the kitchen. It is great for cooking, but also to use in a variety of other dishes. You can use it in soups, stews, or even to season meats. The thyme is dried and then ground into a powder, so it can be easily sprinkled onto any dish. It is a good idea to use it sparingly, so as not to overpower the dish. It is also an excellent garnish for potatoes or other vegetables. The Ducros thyme will be perfect for any kitchen.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d9c003be-59bd-431d-b9a2-a499b16fe0ff_300x300.jpg?v=1645133848'
    },
    {
        'id': 532,
        'link': 'https://gimsap.ca/collections/all/products/ducros-thyme-100gx30-box',
        'name': 'Ducros thyme 100gx30 Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This box of Ducros thyme is a fantastic herb to use in the kitchen. It is great for cooking, but also to use in a variety of other dishes. You can use it in soups, stews, or even to season meats. The thyme is dried and then ground into a powder, so it can be easily sprinkled onto any dish. It is a good idea to use it sparingly, so as not to overpower the dish. It is also an excellent garnish for potatoes or other vegetables. The Ducros thyme will be perfect for any kitchen.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9fccb75b-acff-466a-869c-b3ce10b2a5c2_300x300.jpg?v=1650664658'
    },
    {
        'id': 533,
        'link': 'https://gimsap.ca/collections/all/products/ducros-thyme-10g-12x12-box',
        'name': 'Ducros Thyme 10g (12x12 Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><span>This box of Ducros thyme is a fantastic herb to use in the kitchen. It is great for cooking, but also to use in a variety of other dishes. You can use it in soups, stews, or even to season meats. The thyme is dried and then ground into a powder, so it can be easily sprinkled onto any dish. It is a good idea to use it sparingly, so as not to overpower the dish. It is also an excellent garnish for potatoes or other vegetables. The Ducros thyme will be perfect for any kitchen.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2e3e0766-4ef2-402f-bee8-471e89d9675c_300x300.jpg?v=1645133850'
    },
    {
        'id': 534,
        'link': 'https://gimsap.ca/collections/all/products/dudu-osun-black-soap',
        'name': 'Dudu-osun black soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Helps with oily skin, and acne. Restores damaged skin and heals chronic eczema.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d1503fd7-63f1-4723-b62f-5074f00e1650_300x300.jpg?v=1645133851'
    },
    {
        'id': 535,
        'link': 'https://gimsap.ca/collections/all/products/dudu-osun-black-soap-box-48x150g',
        'name': 'Dudu-osun black soap (box) 48x150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $185.00',
        'description': '<span data-mce-fragment="1">Helps with oily skin, and acne. Restores damaged skin and heals chronic eczema.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ce3dabc4-008b-434b-ad1e-177d028cc0e2_300x300.jpg?v=1645133852'
    },
    {
        'id': 536,
        'link': 'https://gimsap.ca/collections/all/products/dudu-osun-black-soap-box-48x150g-vivian',
        'name': 'Dudu-osun black soap (box) 48x150g (Vivian)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $185.00',
        'description': '<p>&nbsp;</p>\n<p><span>Helps with oily skin, and acne. Restores damaged skin and heals chronic eczema.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f863b7d5-8213-41eb-a41e-a91993112e90_300x300.jpg?v=1645133853'
    },
    {
        'id': 537,
        'link': 'https://gimsap.ca/collections/all/products/dudu-osun-lotion',
        'name': 'Dudu-osun lotion',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': 'Contains shea butter, aloe vera, plant extracts and many other therapeutic herd. Intensively moisturizes skin leaving it soft and silky smooth.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_5c98f7f3-b311-4672-962f-1314b1468aaa_300x300.jpg?v=1650665213'
    },
    {
        'id': 538,
        'link': 'https://gimsap.ca/collections/all/products/dunya-harvest-chia-seed-box-4-x-567g',
        'name': 'Dunya Harvest Chia Seed (Box 4 x 567g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': 'A great source for fiber, fat and protein, Chia Seeds are a tasty high-energy food.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b780d841-7df3-4331-aa6c-f51ba831e0a8_300x300.jpg?v=1650665264'
    },
    {
        'id': 539,
        'link': 'https://gimsap.ca/collections/all/products/durum-semolina-20kg',
        'name': 'Durum Semolina 20kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': 'A coarse flour that is made out of durum wheat. Is rich in fiber, protein and B vitamins.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dd6035b0-7461-422f-b820-a41aa6580641_300x300.jpg?v=1645133858'
    },
    {
        'id': 540,
        'link': 'https://gimsap.ca/collections/all/products/durum-semolina-yellow-10kg',
        'name': 'Durum Semolina Yellow 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $27.50',
        'description': '<p>&nbsp;</p>\n<p><span>A coarse flour that is made out of durum wheat. Is rich in fiber, protein and B vitamins.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_66838381-26b4-4496-8db3-c945ac9837eb_300x300.jpg?v=1645133859'
    },
    {
        'id': 541,
        'link': 'https://gimsap.ca/collections/all/products/dustin-powder-200g',
        'name': 'Dusting Powder 200g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': 'Absorbs oils, helps smooth your skin and has a nice fragrance.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_591109b1-adf3-49f3-b662-e6a4afb34760_300x300.jpg?v=1650665627'
    },
    {
        'id': 542,
        'link': 'https://gimsap.ca/collections/all/products/earring',
        'name': 'Earring',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Featuring a gorgeous design, these earrings are the perfect accessory for any occasion. Spice up any outfit you wear with a bit of jewelry.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_5121f5c7-4d1c-40e4-b067-da8f29726693_300x300.jpg?v=1650665742'
    },
    {
        'id': 543,
        'link': 'https://gimsap.ca/collections/all/products/ebony-fresh-harbal-soap',
        'name': 'Ebony Fresh Herbal Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Ebony Fresh Herbal Soap is a handcrafted, vegan soap made with fresh, organic ingredients. The soap is made in small batches to ensure quality and freshness. This soap is made with fresh, organic ingredients and will cleanse and refresh the skin.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_07686acd-87d8-4c16-b636-773ff4a19469_300x300.jpg?v=1645133862'
    },
    {
        'id': 544,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-black-castor-flaxseed-oil-16oz',
        'name': 'Eco Gel - Black Castor &amp; Flaxseed Oil (16oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.75',
        'description': '<p>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b4d5a162-218a-4f25-8dfd-06a8db24994f_300x300.jpg?v=1645133865'
    },
    {
        'id': 545,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-moroccan-argan-oil-16oz',
        'name': 'Eco Gel - Moroccan Argan Oil (16oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p>A single application of Eco Gel - Moroccan Argan Oil is all you need to leave your hair feeling soft and looking healthy. Made with a blend of Moroccan Argan Oil, Apricot Kernel Oil, Coconut Oil, and other natural ingredients, Eco Gel - Moroccan Argan Oil is free of parabens, sulfates, and mineral oil. The light gel texture spreads easily through your hair, making it easy to comb through and style as desired. With Eco Gel - Moroccan Argan Oil, you can create beautiful waves, curls, or straight hair without any buildup or stiffness. This natural product is ideal for both men and women and can be used on wet or dry hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3f3574eb-7d0f-4ad3-aa14-4757c3b2a81e_300x300.jpg?v=1645133866'
    },
    {
        'id': 546,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-moroccan-argan-oil-32oz',
        'name': 'Eco Gel - Moroccan Argan Oil (32oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>A single application of Eco Gel - Moroccan Argan Oil is all you need to leave your hair feeling soft and looking healthy. Made with a blend of Moroccan Argan Oil, Apricot Kernel Oil, Coconut Oil, and other natural ingredients, Eco Gel - Moroccan Argan Oil is free of parabens, sulfates, and mineral oil. The light gel texture spreads easily through your hair, making it easy to comb through and style as desired. With Eco Gel - Moroccan Argan Oil, you can create beautiful waves, curls, or straight hair without any buildup or stiffness. This natural product is ideal for both men and women and can be used on wet or dry hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9ba04166-b41c-4c22-96ab-ec207367ed4c_300x300.jpg?v=1650666517'
    },
    {
        'id': 547,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-moroccan-argan-oil-8oz',
        'name': 'Eco Gel - Moroccan Argan Oil (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.25',
        'description': '<p>A single application of Eco Gel - Moroccan Argan Oil is all you need to leave your hair feeling soft and looking healthy. Made with a blend of Moroccan Argan Oil, Apricot Kernel Oil, Coconut Oil, and other natural ingredients, Eco Gel - Moroccan Argan Oil is free of parabens, sulfates, and mineral oil. The light gel texture spreads easily through your hair, making it easy to comb through and style as desired. With Eco Gel - Moroccan Argan Oil, you can create beautiful waves, curls, or straight hair without any buildup or stiffness. This natural product is ideal for both men and women and can be used on wet or dry hair.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bc465318-3724-4e0f-b21a-41039ac19c76_300x300.jpg?v=1645133868'
    },
    {
        'id': 548,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-olive-oil-max-hold-32oz',
        'name': 'Eco Gel - Olive Oil/Max Hold (32oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': "<p>The eco gel is a hair gel that is made with 100% natural ingredients. The product is great for all hair types and leaves hair feeling healthy and shiny. It has a great scent and is easy to use. The gel is non-sticky and doesn't make hair stiff. It has a maximum hold, which means it lasts all day. The product is vegan and cruelty-free.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a65f0176-bd7e-4a35-bd56-ea15a46e8193_300x300.jpg?v=1645133869'
    },
    {
        'id': 549,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-olive-oil-max-hold-8oz',
        'name': 'Eco Gel - Olive Oil/Max Hold (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.25',
        'description': "<p><span>The eco gel is a hair gel that is made with 100% natural ingredients. The product is great for all hair types and leaves hair feeling healthy and shiny. It has a great scent and is easy to use. The gel is non-sticky and doesn't make hair stiff. It has a maximum hold, which means it lasts all day. The product is vegan and cruelty-free.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6536feba-084d-49f6-bffe-459b1aff37e7_300x300.jpg?v=1645133871'
    },
    {
        'id': 550,
        'link': 'https://gimsap.ca/collections/all/products/eco-gel-946ml',
        'name': 'Eco Gel 946ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p><span>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4af615dd-f09d-44a5-b069-33f0b303f05e_300x300.jpg?v=1645133863'
    },
    {
        'id': 551,
        'link': 'https://gimsap.ca/collections/all/products/eco-style-gel-946ml',
        'name': 'Eco Style Gel 946ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p><span>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bc95b270-7363-42d0-83b2-16a1a2c2ffd5_300x300.jpg?v=1645133872'
    },
    {
        'id': 552,
        'link': 'https://gimsap.ca/collections/all/products/eco-styler-32oz',
        'name': 'Eco Styler 32oz',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p><span>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b724a701-97ae-46c7-94f6-2ec06407bdb1_300x300.jpg?v=1645133873'
    },
    {
        'id': 553,
        'link': 'https://gimsap.ca/collections/all/products/eco-styler-gel-16oz-olive-oil',
        'name': 'Eco Styler Gel 16oz Olive Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p><span>The eco gel is a hair gel that is made with 100% natural ingredients. The product is great for all hair types and leaves hair feeling healthy and shiny. It has a great scent and is easy to use. The gel is non-sticky and doesn't make hair stiff. It has a maximum hold, which means it lasts all day. The product is vegan and cruelty-free.</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3a2991de-4f3a-4ae5-a37c-fb2fcfb59e64_300x300.jpg?v=1645133874'
    },
    {
        'id': 554,
        'link': 'https://gimsap.ca/collections/all/products/eco-styler-gel-437ml',
        'name': 'Eco Styler Gel 437ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p><span>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_980d504c-2344-469f-b9d9-2b8404697d45_300x300.jpg?v=1645133875'
    },
    {
        'id': 555,
        'link': 'https://gimsap.ca/collections/all/products/eco-styler-gel-5lbs',
        'name': 'Eco Styler Gel 5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': '<p><span>Eco Gel strengthens hair, helps repair and grow hair and gives your hair a healthy glow. It is a popular gel that allows you to style your hair in any way with no flaking, no itch and no tack.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6bf6946d-eb40-40cf-804b-b92e90c55b67_300x300.jpg?v=1645133877'
    },
    {
        'id': 556,
        'link': 'https://gimsap.ca/collections/all/products/ede-150g',
        'name': 'Ede 150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>Ede is a fruit-based gelato made with natural ingredients. It is gluten-free, dairy-free, and vegan. It comes in six flavors: watermelon, strawberry, coconut, banana, mango, and pineapple. Ede is made in small batches and is available in four packs of three flavors each.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_abf14caa-1e76-4d99-b291-33766f64689b_300x300.jpg?v=1645133879'
    },
    {
        'id': 557,
        'link': 'https://gimsap.ca/collections/all/products/ede-uri-aguleri-200g',
        'name': 'Ede Uri (Aguleri) 200g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>A Nigerian food staple that is a type of cassava. It is boiled, peeled, and then pounded into a thick paste. It is often eaten with vegetable soup or groundnut soup.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_728cdc48-e2cb-43d9-b60f-4ff384e9adfc_300x300.jpg?v=1650666956'
    },
    {
        'id': 558,
        'link': 'https://gimsap.ca/collections/all/products/eden-24mm-hair-ball-assorted',
        'name': 'Eden 24mm Hair Ball Assorted',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>Designed to hold hair in place,&nbsp;Eden 24mm Hair Ball Assorted comes in all sorts of colors so you can look good where ever you go.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a795a694-81e1-44ca-b774-07c06868e7cd_300x300.jpg?v=1645133881'
    },
    {
        'id': 559,
        'link': 'https://gimsap.ca/collections/all/products/eden-xlg-blister-medium-round-bead-assorted',
        'name': 'Eden XLG Blister Medium Round Bead Assorted',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>Eden XLG Blister Medium Round Bead Assorted is a pack of assorted beads. These beads are made of a glass material. These beads are large in size and are of a round shape. The beads are round and have a wide variety of colors. These beads are used for jewelry making and are sold by the package.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_96d5940e-fd65-49e2-bfa4-901f83047b09_300x300.jpg?v=1645133883'
    },
    {
        'id': 560,
        'link': 'https://gimsap.ca/collections/all/products/egg-plant-700gx12-box-delice',
        'name': 'Egg Plant 700gx12 Box (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Delice Eggplant is a dark purple eggplant that is harvested at the peak of ripeness. Delice Eggplant is often used in Asian cuisine, specifically Japanese and Korean cuisine. Delice Eggplant is tender and has a rich, savory flavor. It is best when used in dishes that have a sweet and savory flavor, such as sushi.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_6d1dea2f-e364-4625-b052-f70f8ef6d638_300x300.jpg?v=1650667271'
    },
    {
        'id': 561,
        'link': 'https://gimsap.ca/collections/all/products/eggs-organic',
        'name': 'Eggs (organic)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>Organic eggs from cage-free hens, are packed with protein and a variety of vitamins and minerals.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_4036a906-7ab5-43bf-9551-277055aeb44f_300x300.jpg?v=1650667306'
    },
    {
        'id': 562,
        'link': 'https://gimsap.ca/collections/all/products/eggs-regular',
        'name': 'Eggs (regular)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': "<p>Looking for the perfect egg for your morning breakfast? Try our regular eggs! Our eggs are 100% farm fresh and come from chickens raised on family farms. We have over a dozen varieties of eggs available to suit your needs. Whether you're looking for a particular color, size, or even eggshell thickness, we have the perfect egg for you.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_dcdcfcf2-e17b-405d-9541-88b587141ab2_300x300.jpg?v=1650670189'
    },
    {
        'id': 563,
        'link': 'https://gimsap.ca/collections/all/products/egusi-400g-todaj',
        'name': 'Egusi 400g (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Egusi is a traditional Nigerian dish made from ground melon seeds, which are usually soaked in water and squeezed dry before being ground into a paste. This dish is typically eaten with pounded yam, garri, or plantain. The Egusi is traditionally consumed with assorted vegetables such as boiled spinach, beans, and okra.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_f13f1229-bec5-4e8c-8f43-b6e96009a5c7_300x300.jpg?v=1650670598'
    },
    {
        'id': 564,
        'link': 'https://gimsap.ca/collections/all/products/egusi-delice',
        'name': 'Egusi Delice',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Egusi is a traditional Nigerian dish made from ground melon seeds, which are usually soaked in water and squeezed dry before being ground into a paste. This dish is typically eaten with pounded yam, garri, or plantain. The Egusi is traditionally consumed with assorted vegetables such as boiled spinach, beans, and okra.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_217a900a-159d-452f-b7cc-4bbb69f6aaaf_300x300.jpg?v=1650670622'
    },
    {
        'id': 565,
        'link': 'https://gimsap.ca/collections/all/products/egusi-egusi-259gr',
        'name': 'Egusi Egusi 259gr',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Egusi is a traditional Nigerian dish made from ground melon seeds, which are usually soaked in water and squeezed dry before being ground into a paste. This dish is typically eaten with pounded yam, garri, or plantain. The Egusi is traditionally consumed with assorted vegetables such as boiled spinach, beans, and okra.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_0bd28ad9-450a-4e65-afe0-b9b4e128fd1a_300x300.jpg?v=1650670664'
    },
    {
        'id': 566,
        'link': 'https://gimsap.ca/collections/all/products/ehuru-pepper-soup-spice-whole',
        'name': 'Ehuru (Pepper soup spice whole)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p>Ehuru is a spice used in soups and stews because of it's fragrance</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b9284192-41ce-42ce-8596-71ff6a20ec5c_300x300.jpg?v=1650670744'
    },
    {
        'id': 567,
        'link': 'https://gimsap.ca/collections/all/products/electric-pressing-comb',
        'name': 'Electric Pressing Comb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': "<p>The new Electric Pressing Comb is perfect for styling hair, as it is capable of flattening the toughest hair with ease. Made of high-quality, heavy-duty plastic, the Electric Pressing Comb is durable and can withstand the toughest of styling. The comb's extra-long teeth are designed to grip each hair, no matter how thick or coarse, and flatten it to the scalp. The electric design of the comb is perfect for styling short hair and for people who do not have the time to spend on their hair.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_8a6733f3-3d55-4ff3-8851-d7a851772711_300x300.jpg?v=1650671192'
    },
    {
        'id': 568,
        'link': 'https://gimsap.ca/collections/all/products/elubo-yam-flour-2kgx6-delice',
        'name': 'Elubo Yam Flour 2kgx6 (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Elubo Yam Flour is a high quality, organic, natural and GMO-free flour that is great for baking and cooking. It is made from the finest Ghanaian yams and carefully blended with the finest ground coconut oil, which is the most healthy fat on the planet. The product is rich in protein, gluten-free, vegan, high in fiber, and low in sugar.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_a3082979-f5bb-4382-ab91-d74db93b4565_300x300.jpg?v=1650671336'
    },
    {
        'id': 569,
        'link': 'https://gimsap.ca/collections/all/products/epiderm-lotion',
        'name': 'Epiderm Lotion',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': "<p>The Epiderm Lotion is an all-natural, soothing lotion made with essential oils and natural ingredients to keep your skin moisturized and healthy. The lotion is perfect for dry skin and can be used on the face, hands, and body. It also smells nice, so you don't have to worry about smelling like a medicinal ointment. The lotion is made with olive oil, coconut oil, shea butter, and cocoa butter to moisturize and protect your skin. The lotion is a blend of natural ingredients, so it's safe for sensitive skin. It also contains a few different essential oils that provide antibacterial properties and help to reduce the appearance of wrinkles.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fb2ee5de-7415-4040-818f-3a0b790858ed_300x300.jpg?v=1645133896'
    },
    {
        'id': 570,
        'link': 'https://gimsap.ca/collections/all/products/epsom-salt',
        'name': 'Epsom Salt',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Epsom salt is a type of mineral salt that is usually made from the ground up ashes of sea plants. It is usually found in a grainy, white form and is used for many different purposes. Epsom salt is usually used for medicinal purposes, and is also used in food preparation. Epsom salt can be used to make bread, desserts, and other food items. It can also be used as a bath additive. It is also used in skin care products and is used to reduce inflammation. Epsom salt can be purchased in many different places and is a very versatile product.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_570b7334-6b1f-420a-961f-aeb2c99e26ec_300x300.jpg?v=1645133896'
    },
    {
        'id': 571,
        'link': 'https://gimsap.ca/collections/all/products/ero-arike-balm',
        'name': 'Ero Arike (Balm)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>The Ero Arike is a balm that is specifically designed to relieve dry skin and sore muscles. It is made from a variety of natural ingredients, including olive oil, coconut oil, shea butter, and vitamin E. The balm is perfect for use before and after workouts, or as a daily moisturizer.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b48f7d98-18bb-457c-b90d-900073f21f5b_300x300.jpg?v=1650671635'
    },
    {
        'id': 572,
        'link': 'https://gimsap.ca/collections/all/products/extra-virgin-olive-oil-with-lavender',
        'name': 'Extra Virgin Olive Oil With Lavender.',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>.A fine and elegant bottle of Extra Virgin Olive Oil with a subtle hint of lavender, this oil helps repair skin, relieve pain and heal wounds.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_634328bb-aa10-4176-906d-93edb666199e_300x300.jpg?v=1645133899'
    },
    {
        'id': 573,
        'link': 'https://gimsap.ca/collections/all/products/eye-lip-liner',
        'name': 'Eye &amp; Lip Liner',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Maker yourself look bolder with our eye and lip liners.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2c6ee721-6a4c-498d-ae34-18f2d47a59a6_300x300.jpg?v=1645133901'
    },
    {
        'id': 574,
        'link': 'https://gimsap.ca/collections/all/products/f-w-serum',
        'name': 'F &amp; W Serum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Contains detoxifying agents and Vitamin C, leaving your skin soft, radiant and revitalized.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_43564014-a31e-478c-8067-194b2fc7da7b_300x300.jpg?v=1650672131'
    },
    {
        'id': 575,
        'link': 'https://gimsap.ca/collections/all/products/f-w-body-clearing-milk',
        'name': 'F&amp;W Body Clearing milk',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.99',
        'description': '<h2 class="product-page--title" itemprop="name">FAIR AND WHITE ORIGINAL BODY CLEARING MILK</h2>\n<p><span data-mce-fragment="1">Clarifying and moisturizing body lotion formulated to lighten dark areas of the body. Specifically developed to fade skin discoloration and even out skin tone. Reduces the appearance of dark spots caused by aging, repeated environmental exposure, hormonal fluctuations, and post acne scars.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_300x300.webp?v=1651665692'
    },
    {
        'id': 576,
        'link': 'https://gimsap.ca/collections/all/products/f-w-gold-ultimate-500ml',
        'name': 'F&amp;W Gold Ultimate 500ml',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $89.99',
        'description': '<span data-mce-fragment="1">&nbsp;Maxi Tone combines a lightening active ingredient with the antioxidant properties of Vitamin E as it evens out and brightens complexion.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_b4e83fb2-e5d6-4f52-9cb0-887cf4e34539_300x300.webp?v=1651665828'
    },
    {
        'id': 577,
        'link': 'https://gimsap.ca/collections/all/products/fair-whair-gold-brightening-cream',
        'name': 'Fair  &amp; Whair Gold Brightening Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.99',
        'description': '<strong data-mce-fragment="1">Description:</strong><span data-mce-fragment="1">&nbsp;Reveal skins radiance with this delicately fragranced moisturizing night cream. AHA Glycolic Acid allows for quick and efficient absorption of lightening and brightening actives into the skin, promoting a softer, brighter and more radiant complexion.&nbsp;&nbsp;</span><br data-mce-fragment="1"><br data-mce-fragment="1"><strong data-mce-fragment="1">How to use:</strong><span data-mce-fragment="1">&nbsp;For a brighter, more radiant complexion, apply Brightening Cream to dry, cleansed skin preferably at night. Avoid eye area. (Applying cream to damp skin may cause an irritation so best if skin is dried well). Follow up with a minimum SPF 50 sunscreen daily to maintain even skin tone</span><br data-mce-fragment="1"><br data-mce-fragment="1"><strong data-mce-fragment="1">Tip:</strong><span data-mce-fragment="1">&nbsp;Many consumers do not want to use lightening products with Hydroquinone hence F&amp;W has provided this Hydroquinone Free AHA as a replacement for non-hydroquinone users. After you have achieved your lightening results with more aggressive lightening ingridients, AHA’s should be used to maintain even toned results.</span><br data-mce-fragment="1"><br data-mce-fragment="1"><strong data-mce-fragment="1">Caution:</strong><span data-mce-fragment="1">&nbsp;Glycolic Acid can make the skin sensitive to sunlight during the day, therefore it is not recommended for daytime use. If skin feels dry or irritated, apply Gold Rejuvenating Moisture Lotion.</span><br data-mce-fragment="1"><br data-mce-fragment="1"><strong data-mce-fragment="1">Main Ingredient:</strong><span data-mce-fragment="1">&nbsp;Glycolic Acid</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_29645805-0478-4622-8b07-f6ddef072b43_300x300.webp?v=1651666015'
    },
    {
        'id': 578,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-exclusive-soap',
        'name': 'Fair &amp; White Exclusive Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.00',
        'description': '<span data-mce-fragment="1">Cleanses and buffs away dead skin cells, instantly restoring radiance with Apricot seed Powder, promoting a healthy glow. Smoothes skins texture with hydrating and nourishing Glycerin.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_9a2c7cd3-d179-4c1b-bc81-e2fc24e4eece_300x300.webp?v=1651666093'
    },
    {
        'id': 579,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-gel-cream',
        'name': 'Fair &amp; White Gel Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<span data-mce-fragment="1">Opaque and light textured fading gel formulated with powerful lightening properties to aggressively lighten dark spots, leaving skin with a healthy glow. Improves clarity and radiance.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_23a393dc-9972-40cc-aff1-3dea4521f2f3_300x300.webp?v=1651666139'
    },
    {
        'id': 580,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-gold-soap-1',
        'name': 'Fair &amp; White Gold Soap 1',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.99',
        'description': '<span data-mce-fragment="1">Gold Exfoliating Soap with Argan Oil</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_c7aa9365-3358-4c4a-bc3a-4bbefdb57994_300x300.webp?v=1651666201'
    },
    {
        'id': 581,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-serum',
        'name': 'Fair &amp; White Serum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.99',
        'description': '<p data-mce-fragment="1">Specifically formulated to even out overall facial discoloration. Reduces stubborn blotchy, brown spots, acne scarring and/or uneven skin tone with potent agent.</p>\n<p data-mce-fragment="1">A light serum is usally preferred by consumers who have oily/combination/blemish prone skin. Leaves skin feeling soft and silky.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_a66a20ce-e868-46bb-9429-5cbeebb051b8_300x300.webp?v=1651666371'
    },
    {
        'id': 582,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-skin-perfector-gel',
        'name': 'Fair &amp; white Skin Perfector Gel',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $19.99',
        'description': '<span data-mce-fragment="1">Brighten dull skin with this refreshing light textured fading gel formulated to fade skin discolorations on face, neck hands or body. Quick drying and formulated with powerful lighting properties, brown spots are visibly lighter, promoting a brighter, radiant even toned complexion. Gels are perfect for oily complexions, especially in hot humid climates.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/FW-SoWhite-GelSkinPerfector-30ml-b-zoom_590x_0cec809c-7bde-4da4-956e-12f6b56be703_300x300.webp?v=1651666625'
    },
    {
        'id': 583,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-skin-parfector-serum',
        'name': 'Fair &amp; White Skin Perfector Serum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $29.99',
        'description': '<span data-mce-fragment="1">Infused with a unique blend of safe brightening properties and sweet delectable scent, this silky soft, lightweight serum quickly penetrates the skin addressing all concerns of skin discoloration. Improves skin clarity and radiance for an overall healthier, brighter complexion.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/FW-SoWhite-SerumSkinPerfector-30ml-b-zoom_768x_3e15edbe-32e6-4abc-b722-445ee2995eb0_300x300.webp?v=1651666558'
    },
    {
        'id': 584,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-so-white',
        'name': 'Fair &amp; white So White',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': '<div class="product-page--description" data-mce-fragment="1">\n<div class="rte-content" data-mce-fragment="1" itemprop="description">\n<div data-mce-fragment="1">\n<div data-mce-fragment="1">Ultra-refreshing with Pomegranate and Melon extracts for a pure moment of well-being. Very gentle for the skin and enriched with emollient glycerine, it leaves a revitalizing scented trail.</div>\n</div>\n<div data-mce-fragment="1"><br data-mce-fragment="1"></div>\n<div data-mce-fragment="1">\n<span data-mce-fragment="1">*</span><i class="" data-mce-fragment="1">non-contractual picture</i>\n</div>\n</div>\n</div>\n<div class="product-page--images" data-mce-fragment="1">\n<div class="product-page--images-container" data-mce-fragment="1">\n<div class="modal--root" data-js-class="FrameworkModal" data-js-loaded="true" data-mce-fragment="1">\n<div class="modal--link" data-mce-fragment="1">\n<div class="product-page--image" data-active="true" data-id="29398205595844" data-mce-fragment="1">\n<div class="image--root" data-aspectratio="0.9974905897114178" data-mce-fragment="1">\n<div class="image--container" data-mce-fragment="1"></div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/1_795x_f8d82212-6b20-411a-bfda-10c2ae73b467_300x300.webp?v=1651666724'
    },
    {
        'id': 585,
        'link': 'https://gimsap.ca/collections/all/products/fair-white-so-white-exfoliating-soap',
        'name': 'Fair &amp; White So White Exfoliating Soap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.00',
        'description': '<span data-mce-fragment="1">Pamper yourself with this refreshing beauty bar soap. Enhanced with a sweet powdered fragrance and gentle micro-pearls, this gentle cleansing bar delicately exfoliates dead skin cells, leaving skin feeling refreshed and clean. Creamy foaming action regenerates skin as it softens, revealing instant glowing skin.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-32_300x300.jpg?v=1606150266'
    },
    {
        'id': 586,
        'link': 'https://gimsap.ca/collections/all/products/fair-and-white-body-milk-500-ml',
        'name': 'Fair and White Body Milk 500 mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': "<p>Fair and White Body Milk is the perfect choice for those who want to have a natural, non-toxic product that is made with high quality ingredients. It's made with milk protein and milk lipids, making it an excellent moisturizer. The milk protein provides a protective layer on the skin, while the milk lipids act as a moisturizer and helps to prevent dry skin. The milk protein also has natural UV filters, which help to protect your skin from the sun.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_aa515536-b0ea-45a0-9cdd-5080c0777bab_300x300.jpg?v=1645133902'
    },
    {
        'id': 587,
        'link': 'https://gimsap.ca/collections/all/products/fair-n-white-serum-exclusive-whiternizer',
        'name': 'fair n white  serum exclusive whiternizer',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p>Fair n White Serum is a product designed to reduce the appearance of dark spots and lighten skin tone. This serum is a blend of three of the most effective ingredients for brightening skin: vitamin C, niacinamide, and peptides.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7aac65b7-1fcb-46f4-a383-7d132839ad85_300x300.jpg?v=1645133905'
    },
    {
        'id': 588,
        'link': 'https://gimsap.ca/collections/all/products/fair-n-white-exculusive-body-lotion',
        'name': 'fair n white exculusive body lotion',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $50.00',
        'description': "<p>Many people don't know that the sun is a major cause of skin damage. But with the right skin care routine, you can prevent it. That's why we've created this lotion. It will keep your skin looking fresh and radiant by using natural ingredients that hydrate and protect.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0bc8bbc5-208a-4b86-a732-4ab734ea350e_300x300.jpg?v=1645133903'
    },
    {
        'id': 589,
        'link': 'https://gimsap.ca/collections/all/products/fair-n-white-pink',
        'name': 'fair n white pink',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $59.99',
        'description': '<p>The Fair n White Pink Facial is a product that will provide an instant fair and brightening effect to the skin. The Fair n White Pink Facial is for all skin types and is ideal for anyone who wants to give their skin a healthy, natural glow.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c2b78401-839e-4a64-a670-8059a1b2aa40_300x300.jpg?v=1645133904'
    },
    {
        'id': 590,
        'link': 'https://gimsap.ca/collections/all/products/fanta-300ml-bottle',
        'name': 'Fanta 300ml Glass Bottle',
        'price': 'From $2.00',
        'description': '<p>Fanta is an orange flavored soft drink made by The Coca-Cola Company. It is available in over 100 countries and is the second most popular soda in the world.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/81vXjO077mL._SY445_300x300.jpg?v=1647973626'
    },
    {
        'id': 591,
        'link': 'https://gimsap.ca/collections/all/products/fanta-nigeria-50cl-glass',
        'name': 'Fanta Nigeria 50cl Glass',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Fanta is a popular soda drink that is known for its great taste and high levels of fizzy carbonation. This Fanta 50cl glass bottle is a great choice for any fan of the refreshing, thirst-quenching beverage. It is the perfect size for serving at a party or gathering, and it is always a good idea to have a few on hand for unexpected guests. The 50cl glass bottle is available in many flavors, and it will be delivered to your door in just a few days.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5adaf954-48e1-471e-9e18-deb16183288b_300x300.jpg?v=1645133923'
    },
    {
        'id': 592,
        'link': 'https://gimsap.ca/collections/all/products/fever-grass',
        'name': 'Fever Grass',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>Fever Grass is a natural herb that has been used for centuries to help lower fever and reduce inflammation.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Fever-Grass-Lemongrass_300x300.jpg?v=1651666973'
    },
    {
        'id': 593,
        'link': 'https://gimsap.ca/collections/all/products/fever-grass-tea',
        'name': 'fever grass tea',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>With a cold, fever, or a bad sore throat, fever grass tea is the perfect remedy. It has a refreshing minty flavor and a hint of ginger. Made from the fever grass plant, this tea will bring down your fever and make you feel better. It can also be used to relieve minor pain and discomfort.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ebdcda3a-f90e-46f5-ab27-63fbcde7e327_300x300.jpg?v=1645133931'
    },
    {
        'id': 594,
        'link': 'https://gimsap.ca/collections/all/products/fine-bulgur-wheat-10kg',
        'name': 'Fine Bulgur Wheat 10Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Bulgur wheat is a great way to add fiber and protein to your diet. This organic, GMO-free bulgur wheat is a great way to make a nutritious, filling, and tasty dish for your family. It can be used in recipes like tabbouleh, pilaf, and more. The wheat is also easy to cook and store in your pantry.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_09a3bb94-5c67-4c4d-ad3c-697dd4ab0cc0_300x300.jpg?v=1645133932'
    },
    {
        'id': 595,
        'link': 'https://gimsap.ca/collections/all/products/fine-burger-4lb',
        'name': 'Fine burger 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This is a fine burger 4lb. A sandwich that is perfect for a family, friends, or just for you. The taste is excellent and you can really taste the freshness of the meat. This burger is best when it is cooked medium rare, so be sure to get it that way.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_81874b97-5846-40db-aed5-869eff277dc1_300x300.jpg?v=1651667189'
    },
    {
        'id': 596,
        'link': 'https://gimsap.ca/collections/all/products/fine-burgur-10kg',
        'name': 'Fine Burgur 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $40.00',
        'description': '<p>This is a fine burger. A sandwich that is perfect for a family, friends, or just for you. The taste is excellent and you can really taste the freshness of the meat. This burger is best when it is cooked medium rare, so be sure to get it that way.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_4ccb45b9-0465-422e-b12e-5f5a78a43a2f_300x300.jpg?v=1651667322'
    },
    {
        'id': 597,
        'link': 'https://gimsap.ca/collections/all/products/fish-seasoning',
        'name': 'fish seasoning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': "<p>Fish Seasoning is a seafood seasoning that has been created to give seafood dishes a delicious, yet different flavor. This product is perfect for anyone who loves to cook fish dishes and doesn't want to use the same old seasoning every time.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/shopping_300x300.webp?v=1651667443'
    },
    {
        'id': 598,
        'link': 'https://gimsap.ca/collections/all/products/fish-seasoning-170g',
        'name': 'Fish Seasoning 170g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p>Fish Seasoning is a seafood seasoning that has been created to give seafood dishes a delicious, yet different flavor. This product is perfect for anyone who loves to cook fish dishes and doesn't want to use the same old seasoning every time.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_239a8489-50d8-44c3-ae40-f71e4096e86b_300x300.jpg?v=1645133937'
    },
    {
        'id': 599,
        'link': 'https://gimsap.ca/collections/all/products/fish-seasoning-56g',
        'name': 'Fish Seasoning 56g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': "<p>For the die-hard fish lovers, this new seasoning is the perfect addition to any dish. The best part is that it doesn't take much to add that extra zing to your meal. Just sprinkle a little on top of your fish, bake, and enjoy! In order to fully enjoy the delicious flavor of your fish, this new seasoning is the perfect addition.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_eed9551e-ce9a-4812-a371-f7145fabe7d4_300x300.jpg?v=1645133938'
    },
    {
        'id': 600,
        'link': 'https://gimsap.ca/collections/all/products/fish-tea-soup-45g',
        'name': 'Fish Tea Soup 45g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.30',
        'description': '<p>The high quality fish tea soup is the perfect choice for any meal. The tea soup has a strong flavor of fish that is sure to please any palate. The broth is a rich brown color and has an appetizing aroma. The soup is served in a bowl with a few slices of fish and vegetables.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d6835c7f-ac4b-44c4-ae68-975de67df750_300x300.jpg?v=1645133939'
    },
    {
        'id': 601,
        'link': 'https://gimsap.ca/collections/all/products/flake-b-gone',
        'name': 'Flake B -Gone',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': '<p>Flake B-Gone is a non-toxic, odorless and non-sticky product that can be used on any surface. Flake B-Gone can be used on upholstery, furniture, countertops, carpets, bedding, mattresses, or any other fabric or surface. Flake B-Gone works by absorbing the odor from the surface and neutralizing it.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_36260510-05d6-4ab0-a48a-3e0f8a446658_300x300.jpg?v=1651667694'
    },
    {
        'id': 602,
        'link': 'https://gimsap.ca/collections/all/products/flambeau-sauce-300ml',
        'name': 'Flambeau Sauce 300mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p>The Flambeau Sauce 300mL is a creamy, robust and flavorful sauce that is a perfect blend of a rich, sweet, tangy and spicy sauce. This sauce is made with onions, tomatoes, honey, brown sugar, tomato paste, apple cider vinegar, garlic, soy sauce, ground ginger, and other spices.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d9b3a371-05ab-45d5-8781-aac28f8133dd_300x300.jpg?v=1645133941'
    },
    {
        'id': 603,
        'link': 'https://gimsap.ca/collections/all/products/flax-seed',
        'name': 'Flax Seed',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>The benefits of flax seed are endless. Flax seed is a great source of protein, fiber, and vitamins. Flax seed can be consumed raw or in its oil form. Flax seed is a great product for heart health, reducing inflammation, and supplying your body with protein, fiber, and vitamins. It can be consumed raw or in its oil form.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/W5dnY4Y_f8b94670-8e49-4f51-a343-9e3cb5855c50_300x300.jpg?v=1651667847'
    },
    {
        'id': 604,
        'link': 'https://gimsap.ca/collections/all/products/flax-seed-567g-20-oz',
        'name': 'Flax Seed 567g (20 oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The benefits of flax seed are endless. Flax seed is a great source of protein, fiber, and vitamins. Flax seed can be consumed raw or in its oil form. Flax seed is a great product for heart health, reducing inflammation, and supplying your body with protein, fiber, and vitamins. It can be consumed raw or in its oil form.</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/W5dnY4Y_a5a960eb-82fc-41db-be81-c4a2698ebd76_300x300.jpg?v=1651667951'
    },
    {
        'id': 605,
        'link': 'https://gimsap.ca/collections/all/products/fresh-garlic',
        'name': 'Fresh Garlic',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>If you love the taste of garlic, but hate the smell, this is the product for you.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_404ebd64-8383-436f-881c-e0dcbd4907a7_300x300.jpg?v=1645133945'
    },
    {
        'id': 606,
        'link': 'https://gimsap.ca/collections/all/products/fresh-mama-palm-nut-cream-800g',
        'name': 'Fresh Mama Palm Nut Cream 800g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Palm Nut Cream is made from a special type of palm tree, which is rich in vitamins A, E, and F.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_c470075c-d559-4702-b6d6-31f33a380fa0_300x300.jpg?v=1651668290'
    },
    {
        'id': 607,
        'link': 'https://gimsap.ca/collections/all/products/fresh-tomato-box',
        'name': 'Fresh Tomato Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<span>The warm, sweet flavor of ripe tomatoes is a summertime favorite. This 40lb. package of fresh tomatoes is perfect for enjoying with friends and family. These tomatoes are grown in Canada and are shipped fresh and ripe to your door. They are grown without the use of pesticides or synthetic fertilizers and are perfect for slicing, canning, or making a delicious fresh salsa.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/imageService_300x300.jpg?v=1651668673'
    },
    {
        'id': 608,
        'link': 'https://gimsap.ca/collections/all/products/fresh-tomatoes-40lb',
        'name': 'Fresh Tomatoes 40lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<p>The warm, sweet flavor of ripe tomatoes is a summertime favorite. This 40lb. package of fresh tomatoes is perfect for enjoying with friends and family. These tomatoes are grown in Canada and are shipped fresh and ripe to your door. They are grown without the use of pesticides or synthetic fertilizers and are perfect for slicing, canning, or making a delicious fresh salsa.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/imageService_204a506a-02b4-404b-b803-c5748445e2fb_300x300.jpg?v=1651668747'
    },
    {
        'id': 609,
        'link': 'https://gimsap.ca/collections/all/products/fresh-yam-box',
        'name': 'Fresh Yam',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $100.00',
        'description': '<p>Fresh Yam Box</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bad484bc-ef40-4004-b443-39af3736ab30_300x300.jpg?v=1645133949'
    },
    {
        'id': 610,
        'link': 'https://gimsap.ca/collections/all/products/fresh-yam-new-per-lb',
        'name': 'Fresh Yam (new) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>Yams are a rich source of vitamins A and C, potassium, and fiber. They are great for you, and taste delicious. In fact, many people prefer the taste of yams to potatoes. They are a great side dish for a meal or can be used in desserts.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_180x_9cda8163-16d9-4545-a3b6-4e72fd77dd62_300x300.webp?v=1651668981'
    },
    {
        'id': 611,
        'link': 'https://gimsap.ca/collections/all/products/fresh-yam-old-per-lb',
        'name': 'Fresh Yam (old) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>Yams are an excellent source of vitamins A and C, which promote eye health and provide immune system support. They are also a good source of vitamin B6, potassium, and fiber. These large tubers are a great addition to any diet and are perfect for baking or boiling.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_08be8ec2-ae75-4e8e-b792-0b4744fcddcb_300x300.jpg?v=1645133952'
    },
    {
        'id': 612,
        'link': 'https://gimsap.ca/collections/all/products/fresh-yam-box-old',
        'name': 'Fresh Yam Box (old)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p><span>Yams are a rich source of vitamins A and C, potassium, and fiber. They are great for you, and taste delicious. In fact, many people prefer the taste of yams to potatoes. They are a great side dish for a meal or can be used in desserts.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_674fcdb4-6866-4e33-95e5-ad2dc4ec2c21_300x300.jpg?v=1645133950'
    },
    {
        'id': 613,
        'link': 'https://gimsap.ca/collections/all/products/fried-fish',
        'name': 'Fried fish',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Fried fish is a dish that is typically made with fish that has been battered and deep-fried. Fish is a healthy, delicious and nutritious food that is high in protein and low in fat. The flavor of fried fish is often enhanced by the addition of spices such as salt, pepper, cayenne pepper, paprika, garlic powder, or curry powder. Some types of fish are better suited for frying than others. Cod, salmon, and tuna are three types of fish that are commonly fried.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_57a0e8f8-93bb-4620-acc6-18bddca3bc26_300x300.jpg?v=1645133953'
    },
    {
        'id': 614,
        'link': 'https://gimsap.ca/collections/all/products/fried-rice-seasoning',
        'name': 'Fried Rice Seasoning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.69',
        'description': '<p>Fried Rice Seasoning is a seasoning blend that can be used to create the perfect fried rice dish. With the mix of different spices, including onion, garlic, ginger, black pepper, and turmeric, this seasoning blend is perfect for a delicious meal. The mix of spices also includes curry powder, which will give the dish a sweet and spicy flavor. With this seasoning blend, it is easy to make fried rice at home and enjoy a meal that is not only delicious but healthy as well.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_52dba380-6c8d-4813-8adc-8cdfe660f542_300x300.jpg?v=1645133955'
    },
    {
        'id': 615,
        'link': 'https://gimsap.ca/collections/all/products/frozen-attieke-1-kg',
        'name': 'Frozen Attieke (1 kg)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>&nbsp;This product is made from ground cassava, water, and palm oil. It is then formed into balls and dried.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/attieke_1024x1024_061caba0-a373-48d3-b290-1e126d4387a6_300x300.webp?v=1651669328'
    },
    {
        'id': 616,
        'link': 'https://gimsap.ca/collections/all/products/bitter-leaf-ndole',
        'name': 'Frozen Bitter Leaf (Ndole)',
        'price': 'From $5.99',
        'description': '<p>Bitter leaf is an herbal ingredient that have been used for centuries to support a healthy, active lifestyle.&nbsp;<span data-mce-fragment="1">Bitter Leaves, a type of herb, are made from the leaves of the artemisia plant.&nbsp;It is often used as a tea, but is also popular in sauces, as a spice, and in salads.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-16at5.01.16PM_300x300.png?v=1647471707'
    },
    {
        'id': 617,
        'link': 'https://gimsap.ca/collections/all/products/frozen-cassava',
        'name': 'Frozen Cassava (Yuca)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Cassava is a tropical root vegetable that is a major food staple in Africa, Latin America, and Southeast Asia. It is high in starch and low in fat, making it a good choice for those looking to maintain a healthy diet. Cassava is usually boiled, baked, or fried. Frozen cassava is a ready-to-eat product that can be microwaved or baked. It is packaged in a plastic wrap with a resealable top. Frozen cassava is an excellent alternative to fresh cassava as it is easy to store and lasts for months.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b96344cc-53b3-46dc-bc51-97b69c6b04b2_300x300.jpg?v=1645133957'
    },
    {
        'id': 618,
        'link': 'https://gimsap.ca/collections/all/products/catfish-ww-8kg-17-6-lb-box',
        'name': 'Frozen Catfish 18lb Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $50.00',
        'description': "<p>The frozen 18lb catfish box is the perfect box for anyone who loves the taste of delicious, soft, white catfish. This box is packed with&nbsp;18 lb of catfish, and it's a great way to enjoy this popular fish without having to spend a lot of money. Catfish is a delicious fish that's often used in dishes like catfish tacos, catfish stew, and catfish fillets. The fish are 500-800g.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_eb9840af-954a-43f6-a834-2b96a17d955b_300x300.jpg?v=1645133587'
    },
    {
        'id': 619,
        'link': 'https://gimsap.ca/collections/all/products/frozen-cod',
        'name': 'Frozen Cod',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The taste of the sea in a bite-sized package. Frozen Cod is the perfect product for any occasion. It is a quick and easy meal that is ready in minutes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a8441365-215d-4bf5-beb9-f08d8351adc9_300x300.jpg?v=1651669480'
    },
    {
        'id': 620,
        'link': 'https://gimsap.ca/collections/all/products/frozen-cod-atlantic-25-kg-cut',
        'name': 'Frozen Cod (Atlantic) 25 kg cut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $315.00',
        'description': '<p>This product is frozen Atlantic Cod that is cut into 25 kg portions. Cod is a sustainable and inexpensive fish that is high in protein and Omega-3s. This product is perfect for those looking to eat more fish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b4b4278f-c80e-4066-b27b-e7bcf88c1ee7_300x300.jpg?v=1651669540'
    },
    {
        'id': 621,
        'link': 'https://gimsap.ca/collections/all/products/frozen-cod-atlantic-25-kg-uncut',
        'name': 'Frozen Cod (atlantic) 25 kg Uncut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $300.00',
        'description': '<p>"We have the best quality frozen cod, sourced from the Atlantic. These are individually quick frozen and are the perfect fish for frying, baking, or any other dish you can think of. Our cod is available in 25 kg and is cut to your desired size."</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0f879c0a-2bbd-43d8-a66b-f60a395ca106_300x300.jpg?v=1651669584'
    },
    {
        'id': 622,
        'link': 'https://gimsap.ca/collections/all/products/frozen-cod-atlantic-per-lb',
        'name': 'Frozen Cod (Atlantic) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>The Codfish are harvested from the Atlantic Ocean and flash frozen to lock in freshness and flavor. We are proud to offer these Codfish as a fresh and healthy alternative to more common fish like salmon. The Codfish is a sustainable, environmentally friendly option that can be prepared in a variety of ways. The Codfish is a great source of omega-3 fatty acids, and the white flesh is low in mercury. This is an excellent option for those looking for a healthy and sustainable seafood option.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_38692cb9-1cd3-4416-8cfd-d2a08133d872_300x300.jpg?v=1645133963'
    },
    {
        'id': 623,
        'link': 'https://gimsap.ca/collections/all/products/frozen-crab',
        'name': 'Frozen Crab',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>&nbsp;This product comes in a can and is sold by the pound.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ba9101e3-c906-4658-93e0-7df69594a04a_300x300.jpg?v=1645133964'
    },
    {
        'id': 624,
        'link': 'https://gimsap.ca/collections/all/products/frozen-crab-box',
        'name': 'Frozen Crab (box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $140.00',
        'description': '<p>What could be better than a box of frozen crab? This box of frozen crab will not only provide a fun and delicious meal, but also a family activity for kids and adults alike. They will have a blast pulling the legs off the crab and devouring the meat. This product is perfect for summer time when people are grilling and looking for ways to enjoy the summer. It can be used as a substitute for other protein in recipes and can be eaten by itself. It is great for entertaining guests, and it is perfect for those with seafood allergies.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_8fed842d-00a1-47f1-855a-025b686b4f13_300x300.jpg?v=1651669715'
    },
    {
        'id': 625,
        'link': 'https://gimsap.ca/collections/all/products/frozen-oha-de-chosen',
        'name': 'Frozen Oha (De Chosen)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Oha leaf can be used to prepare Oha or Oha soup.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/oha-leafs_300x300.jpg?v=1651669763'
    },
    {
        'id': 626,
        'link': 'https://gimsap.ca/collections/all/products/frozen-okra',
        'name': 'Frozen Okra',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>Frozen Okra is a simple, nutritious, and affordable dish that can be served at any time of the day. This product is made from fresh okra pods that are frozen and packaged for sale.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3e8b7db7-6082-4060-aff9-79723a69f654_300x300.jpg?v=1645133968'
    },
    {
        'id': 627,
        'link': 'https://gimsap.ca/collections/all/products/frozen-pap-white-1kg',
        'name': 'Frozen Pap White 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>If you are looking for a dessert to please your family and friends, this is the perfect choice. Frozen Pap White is a frozen dessert.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fb6388fb-8dad-4ae8-a549-e25e84b80207_300x300.jpg?v=1645133969'
    },
    {
        'id': 628,
        'link': 'https://gimsap.ca/collections/all/products/frozen-pap-yellow-1kg',
        'name': 'Frozen Pap Yellow 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>If you are looking for a dessert to please your family and friends, this is the perfect choice. Frozen Pap White is a frozen dessert.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_709651e3-c162-46d0-92e7-ced151ac5237_300x300.jpg?v=1651670823'
    },
    {
        'id': 629,
        'link': 'https://gimsap.ca/collections/all/products/ugu-leaves-bened-500g',
        'name': 'Frozen Ugu Leaves',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>Ugu leaves are a tree-like plant that is native to East Africa. It is typically found in the central region of Kenya. Ugu leaves are often used as a flavoring in a variety of dishes, as well as in herbal medicine. The Ugu leaves are harvested when they are still green and then dried. Ugu leaves have a very strong and distinct flavor that is often described as "earthy." Ugu leaves are a very unique and versatile ingredient. They can be used in any dish that needs a bit of extra flavor, such as curry, chili, or stew. The leaves can also be added to herbal tea to help relieve cold symptoms.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d7d2a57f-978b-42e3-b40e-f0bedae4f011_300x300.jpg?v=1645138049'
    },
    {
        'id': 630,
        'link': 'https://gimsap.ca/collections/all/products/funbact-a',
        'name': 'Funbact A',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': "<p>Funcact A.C. is a natural product that is formulated to fight against bacterial infections. It's made from ingredients that are organic and all-natural, including goldenseal, grapefruit seed extract, and green tea extract.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0bb2e09e-3866-4e14-9fc5-adaceff7ff30_300x300.jpg?v=1645133971'
    },
    {
        'id': 631,
        'link': 'https://gimsap.ca/collections/all/products/garden-egg',
        'name': 'Garden Egg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p><span>Garden egg&nbsp;(Solanum melongena) contains Protein, Dietary fiber and carbohydrates.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_57f619a2-5cb4-44af-86f8-23a03280ea5e_300x300.jpg?v=1651670933'
    },
    {
        'id': 632,
        'link': 'https://gimsap.ca/collections/all/products/garden-egg-box',
        'name': 'Garden Egg Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p><span>Garden egg&nbsp;(Solanum melongena) contains Protein, Dietary fiber and carbohydrates.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/gardenn-egg-600x600_300x300.jpg?v=1651671499'
    },
    {
        'id': 633,
        'link': 'https://gimsap.ca/collections/all/products/garlic-powderravi',
        'name': 'garlic powder(ravi)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': "<p>Garlic powder is a must-have for any kitchen. Whether you're making a delicious pasta dish or a spicy soup, garlic powder will add the perfect flavor.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_999c0887-91b6-4641-9b89-68ccc53a68ab_300x300.jpg?v=1645133977'
    },
    {
        'id': 634,
        'link': 'https://gimsap.ca/collections/all/products/garnier-nutrisse-bleach-cream',
        'name': 'Garnier Nutrisse Bleach Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Garnier Nutrisse Lightening Cream is an innovative formula that lightens hair color by up to two shades. With an advanced combination of lightening agents, this formula lightens hair in a single step. It is enriched with extracts of lime, kiwi, and lemon to protect the hair and scalp.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9f3fcaee-41a6-4d1e-9f87-3f66dbffcc08_300x300.jpg?v=1645133978'
    },
    {
        'id': 635,
        'link': 'https://gimsap.ca/collections/all/products/gboma-leaves',
        'name': 'Gboma Leaves',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Gboma Leaves are dried and ready to be brewed into a tea.&nbsp; Gboma leaves are commonly used for stomach aches, malaria, and fever.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_71c15c2b-1c9c-4489-92e8-724f0f3eb81e_300x300.jpg?v=1645133979'
    },
    {
        'id': 636,
        'link': 'https://gimsap.ca/collections/all/products/geisha-green-425g-hot-chili',
        'name': 'Geisha Green 425g (Hot Chili)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Geisha Green 425g (Hot Chili) is a blend of ginger, garlic, onion, and peppers that is so hot it can be used as a topping for pizza or eaten with cheese.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a992cff9-e2b1-4825-89e9-910d11ac6347_300x300.jpg?v=1645133981'
    },
    {
        'id': 637,
        'link': 'https://gimsap.ca/collections/all/products/geisha-red-425g',
        'name': 'Geisha Red 425g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>Geisha Green 425g is a blend of ginger, garlic, onion, and peppers that is so hot it can be used as a topping for pizza or eaten with cheese.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_66ad2223-001e-4148-a7bd-22d3d045184c_300x300.jpg?v=1645133982'
    },
    {
        'id': 638,
        'link': 'https://gimsap.ca/collections/all/products/gel-activator',
        'name': 'Gel Activator',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Gel Activator is a product that is designed to be used with a hair dryer to speed up the drying process. The product has a pleasant smell and is designed to provide the consumer with a product that will allow them to spend less time on their hair and more time on other things.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a47dc370-cf89-46e7-ad8e-0a977bafe7cf_300x300.jpg?v=1645133983'
    },
    {
        'id': 639,
        'link': 'https://gimsap.ca/collections/all/products/gemsweet-biscuit',
        'name': 'GemSweet Biscuit',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>GemSweet Biscuit is a delicious and nutritious gluten-free, dairy-free, vegan, and non-GMO snack. It is made with only wholesome ingredients, such as coconut flour, tapioca flour, pumpkin puree, eggs, almond milk, and a few other natural ingredients.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cf42becb-7257-44bc-af25-fa1aa80e13c0_300x300.jpg?v=1645133984'
    },
    {
        'id': 640,
        'link': 'https://gimsap.ca/collections/all/products/gemsweet-biscuit-box',
        'name': 'GemSweet Biscuit Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': '<p>GemSweet Biscuit is a delicious and nutritious gluten-free, dairy-free, vegan, and non-GMO snack. It is made with only wholesome ingredients, such as coconut flour, tapioca flour, pumpkin puree, eggs, almond milk, and a few other natural ingredients.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2e65cb5f-d100-4dfd-ae06-054c4e7d3be1_300x300.jpg?v=1645133985'
    },
    {
        'id': 641,
        'link': 'https://gimsap.ca/collections/all/products/ghana-fresh-egg-plant-garden-eggs-500g',
        'name': 'Ghana Fresh egg plant (garden eggs) 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Garden eggs are a type of small, light-green eggplant that is native to Africa. Garden eggs are a healthy and versatile alternative to many other types of eggplant. The skin is thin and edible, and the flavor is similar to a zucchini. They are typically served in soups, curries, and as a vegetable side dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_695da03a-8234-4b03-a90b-c7049e6c7580_300x300.jpg?v=1645133987'
    },
    {
        'id': 642,
        'link': 'https://gimsap.ca/collections/all/products/ghana-fresh-palm-cream-800g',
        'name': 'Ghana Fresh Palm Cream 800g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p><span>Ghana Fresh Palm Cream is a product that has been made from fresh&nbsp;</span><span>palmnut&nbsp;</span><span>from Ghana. It is high in protein and contains less than 3% fat. The product is rich in vitamins and minerals and is a good source of potassium. The cream is great for adding to a variety of dishes, including curries, soups, and stews.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f6c4dbbc-aacd-42b7-b8ff-f01a46b9cd48_300x300.jpg?v=1645133988'
    },
    {
        'id': 643,
        'link': 'https://gimsap.ca/collections/all/products/ghana-fresh-palm-cream-800g-box',
        'name': 'Ghana Fresh Palm Cream 800g (Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $135.00',
        'description': '<p>Ghana Fresh Palm Cream is a product that has been made from fresh palmnut from Ghana. It is high in protein and contains less than 3% fat. The product is rich in vitamins and minerals and is a good source of potassium. The cream is great for adding to a variety of dishes, including curries, soups, and stews.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f14c1f33-41eb-4d8e-834c-7f2fdef9f039_300x300.jpg?v=1645133989'
    },
    {
        'id': 644,
        'link': 'https://gimsap.ca/collections/all/products/ghana-fresh-palmnut-cream-concentrate',
        'name': 'Ghana Fresh Palmnut Cream Concentrate',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': 'Made<span data-mce-fragment="1">&nbsp;from freshly squeezed palm nut juice. Used in preparation of banga soup - a popular West African dish.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-38_300x300.png?v=1606143024'
    },
    {
        'id': 645,
        'link': 'https://gimsap.ca/collections/all/products/ghana-garri',
        'name': 'Ghana Gari',
        'price': 'From $9.00',
        'description': '<p>A West African staple made from granulated cassava tubers. It can be eaten in its dry form, soaked, or prepared with hot water.&nbsp;Ghana&nbsp;(or White) Gari is a traditional garri with coarse grain.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/160431_2_1_-500x500_300x300.jpg?v=1606139428'
    },
    {
        'id': 646,
        'link': 'https://gimsap.ca/collections/all/products/ghana-gari-100lbs',
        'name': 'Ghana Gari 100lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>Ghana Gari is a hardy, semi-soft, gluten-free grain that is high in protein and fiber. This gluten-free grain is perfect for those who are gluten-sensitive, vegan, or are on a gluten-free diet. It is also a great source of calcium, iron, and magnesium. Ghana Gari is an excellent alternative to rice, wheat, and other grains.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ef685af1-db05-49b9-8629-83e3943c6425_300x300.jpg?v=1645133990'
    },
    {
        'id': 647,
        'link': 'https://gimsap.ca/collections/all/products/ghana-gari-50lbs-cita',
        'name': 'Ghana Gari 50lbs (Cita)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $70.00',
        'description': '<p><span>Ghana Gari is a hardy, semi-soft, gluten-free grain that is high in protein and fiber. This gluten-free grain is perfect for those who are gluten-sensitive, vegan, or are on a gluten-free diet. It is also a great source of calcium, iron, and magnesium. Ghana Gari is an excellent alternative to rice, wheat, and other grains.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Screenshot2022-05-04075617_300x300.png?v=1651672595'
    },
    {
        'id': 648,
        'link': 'https://gimsap.ca/collections/all/products/ghana-gari-50lbs-gaskia',
        'name': 'Ghana Gari 50lbs (Gaskia)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $70.00',
        'description': "<p>Ghana Gari is a whole grain, parboiled rice made from rice grains that have been soaked and cooked until they are soft. They are then dried in the sun and finely ground. The ground rice is boiled and then sun-dried again. This rice is popular in West Africa and is a great source of protein. This traditional rice is parboiled and sun-dried, providing a delicious and healthy whole grain. It's a great source of protein and has a light, nutty flavor.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Screenshot2022-05-04075725_300x300.png?v=1651672663'
    },
    {
        'id': 649,
        'link': 'https://gimsap.ca/collections/all/products/ghana-gari-5lbs',
        'name': 'Ghana Gari 5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>The Ghana Gari 5lbs is a traditional food that is often served with stews, soups, and curries. The dried corn kernels are ground into a fine powder and mixed with salt, water, and other ingredients. This mix is then dried and can be used to make delicious, gluten-free, and vegan food. The Ghana Gari 5lbs is great for those who are looking for a versatile and healthy product.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Screenshot2022-05-04075725_f84fd1d2-f8f6-4f41-911f-125c7a9b7082_300x300.png?v=1651672694'
    },
    {
        'id': 650,
        'link': 'https://gimsap.ca/collections/all/products/ghana-must-go-bag-double-zip',
        'name': 'Ghana Must Go Bag (Double Zip)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Ghana Must Go Bag is a reusable tote bag that features a large main compartment with a double zip closure. The tote bag is made of a sturdy cotton canvas and features the Ghana Must Go Bag logo on the front. It can be used for carrying books, groceries, or anything else you might need. The bag can be reused as many times as you want and is available in five different colors.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b0b40a42-29b9-4a2e-ba53-632173082bc0_300x300.jpg?v=1645133999'
    },
    {
        'id': 651,
        'link': 'https://gimsap.ca/collections/all/products/ghana-oil-2lt',
        'name': 'Ghana oil 2lt',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1a494647-7d80-4244-adc7-1473c4993d65_300x300.jpg?v=1645134000'
    },
    {
        'id': 652,
        'link': 'https://gimsap.ca/collections/all/products/ghesa',
        'name': 'Ghesa',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>??</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5aabfdac-a310-45bc-8c7c-c51b7985ae36_300x300.png?v=1645134002'
    },
    {
        'id': 653,
        'link': 'https://gimsap.ca/collections/all/products/ginger',
        'name': 'Ginger',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>One of the most popular ingredients in Asian cuisine, ginger is an edible plant that is usually a deep yellow color. It has a spicy, sweet, and pungent flavor that is used in cooking and baking to add a kick to many dishes. Ginger is also known for its health benefits, such as being able to soothe nausea and reduce pain from menstrual cramps.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a2178597-d758-43f3-9a6c-7c34692a6645_300x300.jpg?v=1645134003'
    },
    {
        'id': 654,
        'link': 'https://gimsap.ca/collections/all/products/ginger-kola-drink-24x355ml',
        'name': 'Ginger Kola Drink 24x355mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Ginger Kola Drink is a ginger-flavored soda with a nice, refreshing taste. This drink is made with natural ingredients and has no artificial colors or flavors. The ginger in this drink will soothe your stomach and give you a great taste in your mouth. Ginger Kola Drink is a perfect beverage for any occasion.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_940d0e57-04b6-47ae-9ba7-9957c2cb1c4a_300x300.jpg?v=1645134005'
    },
    {
        'id': 655,
        'link': 'https://gimsap.ca/collections/all/products/gino-210',
        'name': 'Gino 210',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>Canned Tomato Sauce</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_156ffcce-79f8-4f0c-82e4-244df2358f2c_300x300.jpg?v=1645134006'
    },
    {
        'id': 656,
        'link': 'https://gimsap.ca/collections/all/products/gino-400g',
        'name': 'Gino 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.25',
        'description': '<p><span>Canned Tomato Sauce</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5105e0ff-4f3d-4e08-9746-4521b30c45ee_300x300.jpg?v=1645134008'
    },
    {
        'id': 657,
        'link': 'https://gimsap.ca/collections/all/products/gino-70g',
        'name': 'Gino 70g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': '<p><span>Canned Tomato Sauce</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_03ac7616-0216-4ca2-8a1c-eb33ebf19b4e_300x300.jpg?v=1645134009'
    },
    {
        'id': 658,
        'link': 'https://gimsap.ca/collections/all/products/gino-tomato-paste-800g',
        'name': 'gino tomato paste 800g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>This Italian tomato paste is made from a select blend of vine-ripened tomatoes, peeled and crushed to produce a rich, smooth tomato puree. The result is a delicate, delicious sauce with a deep, intense flavor. Use this tomato paste to make pasta sauces, soups, and stews.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3b4cd317-71b6-4fcf-b896-610726291747_300x300.jpg?v=1645134011'
    },
    {
        'id': 659,
        'link': 'https://gimsap.ca/collections/all/products/goat-foot',
        'name': 'Goat foot',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>The goat foot is a traditional dish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_eb391722-ac82-4ce2-8550-08b800bf12b1_300x300.jpg?v=1645134013'
    },
    {
        'id': 660,
        'link': 'https://gimsap.ca/collections/all/products/goat-head',
        'name': 'Goat head',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $23.00',
        'description': '<p>This product is a goat head that is edible. This head is perfect for anyone who wants to eat a goat head. It is great for the adventurous or for those who are simply curious. It can be a great addition to any party, especially if you are looking for something that is not typical. It is not recommended for children, because it is not as easily digestible as other meat. This goat head can be served on a platter with a side of vegetables and a dipping sauce, such as an herb aioli.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c2ef1761-0adc-410b-a958-9d3d75d2f652_300x300.jpg?v=1645134014'
    },
    {
        'id': 661,
        'link': 'https://gimsap.ca/collections/all/products/goat-head-per-lb',
        'name': 'Goat head per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.65',
        'description': '<p><span>This product is a goat head that is edible. This head is perfect for anyone who wants to eat a goat head. It is great for the adventurous or for those who are simply curious. It can be a great addition to any party, especially if you are looking for something that is not typical. It is not recommended for children, because it is not as easily digestible as other meat. This goat head can be served on a platter with a side of vegetables and a dipping sauce, such as an herb aioli.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/KARE-52922-700x700_300x300.jpg?v=1651673722'
    },
    {
        'id': 662,
        'link': 'https://gimsap.ca/collections/all/products/goat-skin-off-lb',
        'name': 'Goat Skin-off /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This is the most popular cut of goat meat that is tasty and&nbsp; a healthy alternative to beef.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/very-beautiful-vintage-goat-skin_original_300x300.webp?v=1651673753'
    },
    {
        'id': 663,
        'link': 'https://gimsap.ca/collections/all/products/goat-tripe',
        'name': 'Goat tripe',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Goat Tripe is a rich and flavorful ingredient with a strong aroma. Known for its high protein content, Goat Tripe is commonly used in soup, as a seasoning, or as a meat substitute. It is a very versatile ingredient and can be used in many dishes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/GoatTripe_1200x1200_2eb76c8b-9af7-442d-b22c-9f182d35e070_300x300.jpg?v=1651673870'
    },
    {
        'id': 664,
        'link': 'https://gimsap.ca/collections/all/products/goji-berries-natural-lb',
        'name': 'Goji Berries Natural /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>The goji berry is a tart, red fruit that grows on the Lycium barbarum plant. The goji berry is a rich source of antioxidants, carotenoids, and essential amino acids. It is also high in vitamin C, vitamin A, and beta-carotene. This fruit is a wonderful addition to any diet, especially those who are looking for an alternative to sugar.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_93458446-077c-4450-b6c4-23ab196047d8_300x300.jpg?v=1645134020'
    },
    {
        'id': 665,
        'link': 'https://gimsap.ca/collections/all/products/goji-berries-natural-10-lb',
        'name': 'Goji Berries Natural 10 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': '<p>Goji Berries are one of the most popular berries in the world. These berries are an excellent source of fiber, antioxidants, and vitamin C. They are native to the Himalayas and Tibet and can be found in many Asian cultures. They are used in a variety of different dishes and drinks.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d1a516a4-eb67-4963-bf19-c63c8d298f3e_300x300.jpg?v=1645134019'
    },
    {
        'id': 666,
        'link': 'https://gimsap.ca/collections/all/products/gold-silver-hair-nail-ring-bead',
        'name': 'Gold &amp; Silver Hair &amp; Nail Ring Bead',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.99',
        'description': '<p>Hair &amp; Nail Ring Bead</p>\n<p>Pak of 10 Pieces</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/bead_cx6627_300x300.webp?v=1651673948'
    },
    {
        'id': 667,
        'link': 'https://gimsap.ca/collections/all/products/gold-hair-nail-ring-bead-l',
        'name': 'Gold Hair &amp; Nail Ring Bead (L)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.35',
        'description': '<p>Hair &amp; Nail Ring Bead</p>\n<p>Pak of 10 Pieces</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/880544995440_01_300x300.jpg?v=1651674005'
    },
    {
        'id': 668,
        'link': 'https://gimsap.ca/collections/all/products/golden-banana-box-150g-plantain-chips',
        'name': 'Golden Banana Box 150g plantain chips',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p>A box of plantain chips from the Golden Banana brand.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bba53110-fc00-4f59-be3e-d27b090eb2d3_300x300.jpg?v=1645134021'
    },
    {
        'id': 669,
        'link': 'https://gimsap.ca/collections/all/products/golden-banana-plantain-chips-150g',
        'name': 'Golden banana plantain chips 150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.75',
        'description': '<p>This is a pack of 150g of banana plantain chips. They are fried in sunflower oil and seasoned with salt and other spices. These chips are vegan, gluten-free, and paleo-friendly. They are a great substitute for regular potato chips, and are a healthy snack.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_991131c7-a7b5-4881-883f-a0eb255d5b83_300x300.jpg?v=1645134022'
    },
    {
        'id': 670,
        'link': 'https://gimsap.ca/collections/all/products/golden-banana-plantain-chips-70g',
        'name': 'Golden banana plantain chips 70g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.50',
        'description': '<p><span>This is a pack of 70g of banana plantain chips. They are fried in sunflower oil and seasoned with salt and other spices. These chips are vegan, gluten-free, and paleo-friendly. They are a great substitute for regular potato chips, and are a healthy snack.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d1dea023-cb2a-4b04-ab33-213588049a62_300x300.jpg?v=1651674135'
    },
    {
        'id': 671,
        'link': 'https://gimsap.ca/collections/all/products/golden-king-wheatlets-10kg',
        'name': 'golden king wheatlets 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $27.50',
        'description': '<p>Golden King Wheatlets are high quality wheatlets that are free of any impurities. Golden King Wheatlets are a natural product, with no additives or preservatives. The wheatlets are a golden color, with a crispy texture and a pleasant flavor.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_513ee83f-96db-4459-bc4b-ecb9066b65d9_300x300.jpg?v=1645134024'
    },
    {
        'id': 672,
        'link': 'https://gimsap.ca/collections/all/products/box-golden-morn-1kg-maize-soya',
        'name': 'Golden Morn  (Maize &amp; Soya)',
        'price': 'From $9.99',
        'description': '<p>Golden Morn is a healthy, convenient, and sustainable meal that is packed with the essential nutrients needed for good health. The ingredients are sourced from various locations. It can be used as a healthy meal or as a protein-rich snack. Golden Morn is perfect for on-the-go, work, or school.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c6bcc8da-163e-4922-be59-57c2bccfb439_300x300.jpg?v=1645129884'
    },
    {
        'id': 673,
        'link': 'https://gimsap.ca/collections/all/products/golden-penny-butter-450g',
        'name': 'Golden Penny Butter 450g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Golden Penny Butter is a delicious spread made from real butter, cream, salt, and sugar. It is a great substitute for butter on toast, as well as a nice topping for cakes and cookies. It is a perfect addition to a breakfast sandwich, as well as for any family dinner. This butter is made with love and is the perfect gift for any occasion.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_19601608-08b7-40c2-8906-6c3e91d3563b_300x300.jpg?v=1645134027'
    },
    {
        'id': 674,
        'link': 'https://gimsap.ca/collections/all/products/golden-penny-semovita-5kg',
        'name': 'Golden Penny Semovita 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<span data-mce-fragment="1">Golden Penny Semovita is a superior quality brand of Semolina made from the finest quality wheat., It is fortified with proteins and vitamins</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7ea6bf8f-c937-4575-a415-dc518be4b0d7_300x300.jpg?v=1645134028'
    },
    {
        'id': 675,
        'link': 'https://gimsap.ca/collections/all/products/golden-pompano-40-lb-box',
        'name': 'Golden Pompano 40 lb box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $180.00',
        'description': '<p>The golden pompano has a light, flaky texture and a delicate flavor. It can be used in a variety of dishes, including salads, sandwiches, and casseroles. It can also be cooked whole and served with a sauce.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/347870_300x300.jpg?v=1651674319'
    },
    {
        'id': 676,
        'link': 'https://gimsap.ca/collections/all/products/golden-pompano-per-lb',
        'name': 'Golden Pompano per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>The golden pompano has a light, flaky texture and a delicate flavor. It can be used in a variety of dishes, including salads, sandwiches, and casseroles. It can also be cooked whole and served with a sauce.</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/347870_d83313b5-f97a-4577-a3cf-c876d9bb7cc4_300x300.jpg?v=1651674342'
    },
    {
        'id': 677,
        'link': 'https://gimsap.ca/collections/all/products/good-mama-detergent',
        'name': 'Good Mama Detergent',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>A perfect balance of plant-based, natural ingredients, and safe, gentle ingredients, Good Mama detergent is the best choice for all of your laundry needs. It will clean your clothes and leave them smelling fresh, while also providing you with peace of mind that you are not putting your family in danger with harsh chemicals.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f6024b27-40d3-4f6d-8ea6-515f60077111_300x300.jpg?v=1645134033'
    },
    {
        'id': 678,
        'link': 'https://gimsap.ca/collections/all/products/goya-saffron-467g',
        'name': 'Goya (Saffron) 467g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Goya Saffron is an organic spice that is commonly used in many Mediterranean dishes. It is best used to flavor dishes like paella, risotto, and bouillabaisse. Saffron is most often used in seafood dishes, and can be used to season meats and vegetables. This product is Kosher and Halal certified.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cda5c141-50ac-47e9-8b82-40d2fe218e0b_300x300.jpg?v=1645134046'
    },
    {
        'id': 679,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-season-with-pepper',
        'name': 'Goya Adobo All Purpose Season (with pepper)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': "<p>Goya Adobo All Purpose Season (with pepper) is a spicy, flavorful all-purpose seasoning that's perfect for any dish. A blend of salt, garlic, oregano, cumin, paprika, black pepper, and thyme, this seasoning can be used on any type of meat, poultry, seafood, or vegetables. Use Goya Adobo All Purpose Season (with pepper) to add a little spice to your next meal.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c82aa195-19f5-41d1-85eb-07555ad76c77_300x300.jpg?v=1645134043'
    },
    {
        'id': 680,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-seasoning-with-cumin',
        'name': 'Goya Adobo All Purpose Seasoning (with Cumin)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>The Goya Adobo All Purpose Seasoning is a blend of cumin, garlic, onion, paprika, oregano, and thyme. This product is an all-purpose seasoning that can be used in cooking meat, seafood, vegetables, and rice. It is available in a 16 oz jar.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9f94d7d9-3e42-4a4b-9907-0ca3bcfbd332_300x300.jpg?v=1645134038'
    },
    {
        'id': 681,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-seasoning-with-pepper',
        'name': 'Goya Adobo All Purpose Seasoning (With Pepper)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>This Goya Adobo All Purpose Seasoning is a blend of dried herbs and spices. This product is perfect for adding to your chicken, fish, pork, and beef. Goya Adobo All Purpose Seasoning is made in the USA and has no MSG. This product is gluten free and contains no allergens.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b4ccfcc0-1255-41e9-bd39-71b9228812f2_300x300.jpg?v=1645134042'
    },
    {
        'id': 682,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-seasoning-467gwith-bitter-orange',
        'name': 'Goya Adobo All purpose Seasoning 467g(with bitter orange)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>Goya Adobo All Purpose Seasoning is a staple in kitchens across the world. It can be used as a dry rub for meats, seafood, and vegetables, or as a sauce. The flavor is tangy and spicy, with a hint of citrus. The ingredients are salt, red pepper, garlic, oregano, bay leaves, thyme, and bitter orange. Goya Adobo All Purpose Seasoning is available in a 467g jar.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_53c050d8-c266-4ecb-a4ef-1dbc6ba58e32_300x300.jpg?v=1645134034'
    },
    {
        'id': 683,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-seasoning-467gwith-lemon-pepper',
        'name': 'Goya Adobo All purpose Seasoning 467g(with Lemon &amp;pepper)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>5g) This Goya Adobo All Purpose Seasoning is a 467g bag with a sprinkle of lemon for an extra flavor. It is great for meats, vegetables, and soups. It is gluten free and has no MSG.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ea6f6022-ff85-4923-98c0-d7e6d6a57a0f_300x300.jpg?v=1645134035'
    },
    {
        'id': 684,
        'link': 'https://gimsap.ca/collections/all/products/goya-adobo-all-purpose-seasoning-467gwithout-pepper',
        'name': 'Goya Adobo All purpose Seasoning 467g(without pepper)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.50',
        'description': '<p>Adobo is&nbsp; made from soy sauce, vinegar, garlic, bay leaves, and peppercorns. This Goya Adobo All Purpose Seasoning is a flavorful and easy way to make any dish a little more interesting. This seasoning is gluten-free and kosher, and it is also low in sodium. It is versatile enough to be used on everything from meat to seafood to vegetables. The best part is that it takes only a few minutes to prepare, so it is perfect for any busy cook.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8307e0fa-68bf-4ce5-9e85-31e8068bf61b_300x300.jpg?v=1645134036'
    },
    {
        'id': 685,
        'link': 'https://gimsap.ca/collections/all/products/goya-extra-virgin-olive-oil-89ml',
        'name': 'Goya Extra Virgin Olive Oil 89mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.75',
        'description': '<p>Goya Extra Virgin Olive Oil is a perfect addition to any kitchen. Made from a blend of imported and domestic olives, this oil is an excellent source of healthy monounsaturated fats. With an excellent taste and smooth texture, this oil is perfect for dipping bread, sautéing vegetables, or using in dressings.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_70b4cb97-b1e2-4f76-9b7b-b956e27a32c2_300x300.jpg?v=1645134044'
    },
    {
        'id': 686,
        'link': 'https://gimsap.ca/collections/all/products/goya-olive-oil',
        'name': 'Goya Olive Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Goya Olive Oil is the best quality olive oil that can be found in the market. It is an excellent choice for all types of cooking, but is especially good for making aioli, salad dressings, and cold sauces. The oil is made from 100% pure and natural olives, and is made with no artificial colors or flavors. The oil has a rich, golden color and a delicate, fruity flavor.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0d604403-fb18-44fe-b870-f3024624fd55_300x300.jpg?v=1645134045'
    },
    {
        'id': 687,
        'link': 'https://gimsap.ca/collections/all/products/goya-sazonador-the-seasoning-with-pepper-312g',
        'name': 'Goya Sazonador The Seasoning (with pepper)-312g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>This Goya Sazonador The Seasoning (with pepper)-312g is a product for those who love to cook. The product is made of fresh pepper, onion, and garlic. The jar contains 312g of product. The product is packaged in a jar that can be resealed. The jar also has a plastic lid.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a5e6b417-9ec5-4508-941f-d288b0a312f2_300x300.jpg?v=1645134047'
    },
    {
        'id': 688,
        'link': 'https://gimsap.ca/collections/all/products/grace-brownie',
        'name': 'Grace brownie',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p>This is a moist, rich brownie made with organic chocolate, cocoa, eggs, and butter.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0171cd2c-9215-4f04-ba70-a8893b737ddd_300x300.jpg?v=1645134048'
    },
    {
        'id': 689,
        'link': 'https://gimsap.ca/collections/all/products/grande-harvest-parboiled-rice-15lb',
        'name': 'GRANDE HARVEST PARBOILED RICE 15LB',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.99',
        'description': '<p>GRANDE HARVEST PARBOILED RICE 15LB This rice is parboiled to increase the natural nutrients and provide a more flavorful rice. The rice is then triple washed to remove excess starch and fat. The rice is then packaged in a resealable bag for your convenience.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_be3538c2-fc41-469e-9371-b1410f07af29_300x300.jpg?v=1645134049'
    },
    {
        'id': 690,
        'link': 'https://gimsap.ca/collections/all/products/granola-honey-almond-13-6kg',
        'name': 'Granola Honey Almond 13.6kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p>Our hearty, delicious Granola Honey Almond is made with real honey and almond extract. It's a delicious way to start your day, with a nutritious boost of protein and fiber. It's gluten-free, kosher, and contains no artificial colors or flavors. The perfect snack for any time of day, it's a great alternative to chips or cookies.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5ba51f5b-a1f7-4f85-80bf-3d130489b462_300x300.jpg?v=1645134050'
    },
    {
        'id': 691,
        'link': 'https://gimsap.ca/collections/all/products/granola-honey-almond-per-lb',
        'name': 'Granola Honey Almond per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p><span>Our hearty, delicious Granola Honey Almond is made with real honey and almond extract. It's a delicious way to start your day, with a nutritious boost of protein and fiber. It's gluten-free, kosher, and contains no artificial colors or flavors. The perfect snack for any time of day, it's a great alternative to chips or cookies.&nbsp;</span></p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/NPECHV_300x300.jpg?v=1651748750'
    },
    {
        'id': 692,
        'link': 'https://gimsap.ca/collections/all/products/green-lentils-2kg',
        'name': 'Green Lentils 2kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Green Lentils are a popular food product. They are the legumes of the legume family, and they are often used in soups and salads. They can also be added to casseroles, stews, and many other dishes. The lentils are green in color and are a nutritious, gluten-free, high-protein food. The packaging is a resealable bag that contains 2kg of lentils.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/www.ubuy.co_300x300.jpg?v=1651748819'
    },
    {
        'id': 693,
        'link': 'https://gimsap.ca/collections/all/products/green-tea',
        'name': 'green tea',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.50',
        'description': '<p>Nurture your mind and body with this traditional, antioxidant-rich, antioxidant-rich tea. With the many benefits of green tea, this drink is perfect for any time of day. This traditional, antioxidant-rich, antioxidant-rich tea is perfect for any time of day. What are the many benefits of green tea? Green tea is rich in antioxidants and other nutrients that can help fight against diseases and slow down the aging process. Drinking green tea can also help promote a healthy heart and reduce the risk of cancer.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_09d90766-2d24-4f32-9c19-8d3071b0490d_300x300.jpg?v=1651749164'
    },
    {
        'id': 694,
        'link': 'https://gimsap.ca/collections/all/products/green-tea-and-mint',
        'name': 'green tea and mint',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>This blend of green tea and mint has a refreshing taste that is perfect for a hot summer day. The green tea leaves are sourced from the most premium regions in China and Japan, which helps create a delicious, flavorful blend. Ingredients: green tea leaves, peppermint leaves, natural flavors Sweetened with sugar and honey.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8bbabf54-6078-4bb0-9685-c512048328cd_300x300.jpg?v=1645134058'
    },
    {
        'id': 695,
        'link': 'https://gimsap.ca/collections/all/products/greens-ogi-500g-strawberry',
        'name': "Green's Ogi  500g  Strawberry",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': "<p>Green's Ogi 500g Strawberry is great-tasting, whole-grain oatmeal, fortified with essential vitamins and minerals. It's made with no artificial flavors, colors, or preservatives.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_4fff3efa-5867-4489-92ef-34a254b8ec8a_300x300.png?v=1651749610'
    },
    {
        'id': 696,
        'link': 'https://gimsap.ca/collections/all/products/greens-ogi-500g-banana-flavor',
        'name': "Green's Ogi  500g Banana Flavor",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>The flavor of this ogi is that of banana, which is perfect for those who love bananas. The consistency is very light and fluffy, with a smooth, silky texture. This ogi is also a great source of potassium, which is essential for maintaining electrolyte balance and preventing muscle cramps. It also has a significant amount of protein and carbohydrates. This product is an excellent choice for those who want to add a more natural element to their diet, or for those who are on a vegan or gluten-free diet.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_d1e3ce2b-91b4-48f0-b6ce-4caec40e954a_300x300.jpg?v=1651749698'
    },
    {
        'id': 697,
        'link': 'https://gimsap.ca/collections/all/products/greens-ogi-500g-white',
        'name': "Green's Ogi  500g White",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': "<p>This is a popular, refreshing drink from Nigeria. It is made from millet, sorghum, and maize. Green's Ogi is a favorite for anyone who likes the traditional taste of Africa.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_170f0371-e3c2-4a84-9984-e478bb6cac6b_300x300.jpg?v=1651749736'
    },
    {
        'id': 698,
        'link': 'https://gimsap.ca/collections/all/products/greenland-dried-catfish-500g',
        'name': 'Greenland Dried Catfish 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This is a great product for those who love seafood, but do not have the time to cook it. The dried catfish can be eaten as is or cooked with a variety of spices.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/IMG-20201009-WA0026_300x300.jpg?v=1651749905'
    },
    {
        'id': 699,
        'link': 'https://gimsap.ca/collections/all/products/grinded-ogbono-4-64-lb-pack',
        'name': 'Grinded Ogbono (4.64 lb pack)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>A portion of traditional Nigerian food is made from crushed dried seeds of the African bush mango, Ogbono, this ground-up, and ready-to-use product is a staple in the African diet. With a nutty flavor and texture, Ogbono is a nutritious, flavorful addition to any dish.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_8d2b317b-aa6b-4d8a-9ccd-06a01db2b562_300x300.jpg?v=1651750153'
    },
    {
        'id': 700,
        'link': 'https://gimsap.ca/collections/all/products/grinded-ogbono-sultan',
        'name': 'Grinded Ogbono (Sultan)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p><span>A portion of traditional Nigerian food is made from crushed dried seeds of the African bush mango, Ogbono, this ground-up, and ready-to-use product is a staple in the African diet. With a nutty flavor and texture, Ogbono is a nutritious, flavorful addition to any dish.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_4384f86d-e569-4de0-bfc8-41f243ec558a_300x300.jpg?v=1651750195'
    },
    {
        'id': 701,
        'link': 'https://gimsap.ca/collections/all/products/ground-achi-per-lb',
        'name': 'Ground Achi per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<div>Grounded achi from the achi seeds used as a soup thickener. It has a flavour that is a bit sweet and can be used in soups like&nbsp;egusi, oha, ogbono, uziza.</div>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-05_060235223_300x300.png?v=1651752157'
    },
    {
        'id': 702,
        'link': 'https://gimsap.ca/collections/all/products/ground-crayfish-lb',
        'name': 'Ground Crayfish /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>It is typically used in soups, stews, and chowders.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-05_061315417_300x300.png?v=1651752797'
    },
    {
        'id': 703,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-todaj-10-lbs',
        'name': 'Ground Egusi (Todaj) 10 lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>Ground Egusi is a seed from the ground pea family. It is dried and roasted, then ground into a fine powder and can be used as a spice in many Nigerian dishes. Ground Egusi is an essential ingredient in Jollof Rice, and it is also used in a variety of other dishes such as soups, stews, and fritters.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_300x300.jpg?v=1651752977'
    },
    {
        'id': 704,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-0-5lb',
        'name': 'Ground Egusi 0.5lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>Egusi is a soup made from ground melon seeds, popular in West Africa. The ground egusi is a finely ground version of the seeds that are often used in Nigerian cooking. The egusi is rich in protein, high in fiber, and is also a good source of iron. Ground Egusi is a Nigerian soup that is popular in West Africa.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_ca52af88-4627-449d-bf41-9d7b3bdafcd6_300x300.jpg?v=1651753090'
    },
    {
        'id': 705,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-25lb-vivian',
        'name': 'Ground Egusi 25lb (Vivian)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Ground Egusi is a spice blend that is used in many Nigerian dishes. It is a mixture of seeds, grains, and dried vegetables. It is ground together to form a thick paste that is sometimes used as a soup base. The flavor is spicy and slightly sweet.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_77c737c6-b27a-4fdb-b437-290182bffc0c_300x300.jpg?v=1651753130'
    },
    {
        'id': 706,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-2lb',
        'name': 'Ground Egusi 2lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.00',
        'description': '<p>The perfect addition to any soup, stew, or sauce. Ground Egusi 2lb.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_ff731f6f-f5b4-4f56-a9d1-3a70c29e6d71_300x300.jpg?v=1651753157'
    },
    {
        'id': 707,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-4lb',
        'name': 'Ground Egusi 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $45.00',
        'description': '<p>Egusi is a Nigerian dish made from melon seeds, ground egusi, and spices. It is a dish that has been a staple in Nigerian cuisine for centuries. The ground egusi is made from ground melon seeds, so it is a vegan dish. It is great for Nigerian dishes like egusi soup, egusi stew, and egusi with fufu.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_0af6a153-2633-4b46-aa7e-396267a0fca5_300x300.jpg?v=1651753212'
    },
    {
        'id': 708,
        'link': 'https://gimsap.ca/collections/all/products/ground-egusi-5lb-todaj',
        'name': 'Ground Egusi 5lb (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p><span>Egusi is a soup made from ground melon seeds, popular in West Africa. The ground egusi is a finely ground version of the seeds that are often used in Nigerian cooking. The egusi is rich in protein, high in fiber, and is also a good source of iron. Ground Egusi is a Nigerian soup that is popular in West Africa.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/il_fullxfull.2518132873_oogg_grande-1_93f71cec-6d0e-41b0-bbac-b4cd2f55bbd6_300x300.jpg?v=1651753234'
    },
    {
        'id': 709,
        'link': 'https://gimsap.ca/collections/all/products/ground-pepper-2lb',
        'name': 'Ground Pepper 2lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': '<p>Enjoy the flavor of freshly ground pepper with this 2lb. bag of freshly ground pepper. The flavor of this pepper is unmatched and perfect for your favorite recipes. This pepper is great for adding a kick to your cooking and a little more spice to your life.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Pepper-Black-Ground-28-15505_1024x1024_0dba06f8-8295-4f87-bd29-120c9b307a04_300x300.webp?v=1651753335'
    },
    {
        'id': 710,
        'link': 'https://gimsap.ca/collections/all/products/ground-pepper-4lb',
        'name': 'Ground Pepper 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': '<p><span data-mce-fragment="1">Enjoy the flavor of freshly ground pepper with this 2lb. bag of freshly ground pepper. The flavor of this pepper is unmatched and perfect for your favorite recipes. This pepper is great for adding a kick to your cooking and a little more spice to your life.</span><br></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Pepper-Black-Ground-28-15505_1024x1024_10a81e47-95b8-40c6-846a-5339cb8a833e_300x300.webp?v=1651753370'
    },
    {
        'id': 711,
        'link': 'https://gimsap.ca/collections/all/products/ground-pepper-meduim-250g',
        'name': 'Ground Pepper Meduim 250g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p><span>Enjoy the flavor of freshly ground pepper with this 2lb. bag of freshly ground pepper. The flavor of this pepper is unmatched and perfect for your favorite recipes. This pepper is great for adding a kick to your cooking and a little more spice to your life.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Pepper-Black-Ground-28-15505_1024x1024_1db2f04c-737d-4eab-ae15-a5a3a0297a09_300x300.webp?v=1651753400'
    },
    {
        'id': 712,
        'link': 'https://gimsap.ca/collections/all/products/ground-pepper-s',
        'name': 'Ground Pepper S',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p><span>Enjoy the flavor of freshly ground pepper with this 2lb. bag of freshly ground pepper. The flavor of this pepper is unmatched and perfect for your favorite recipes. This pepper is great for adding a kick to your cooking and a little more spice to your life.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Pepper-Black-Ground-28-15505_1024x1024_54d8f406-145d-4740-b3fe-9ac2c945e05a_300x300.webp?v=1651753424'
    },
    {
        'id': 713,
        'link': 'https://gimsap.ca/collections/all/products/grounded-egusi-0-90lb-sultan',
        'name': 'Grounded Egusi 0.90lb (Sultan)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.25',
        'description': '<p>Sultan Grounded Egusi is a Nigerian food made from ground dried melon seeds, peppers, salt, and palm oil. Grounded Egusi is often used as a side dish with stews, such as groundnut stew. The thick paste is also used as a spread on bread or crackers. Sultan Grounded Egusi is great for a quick meal or as a healthy snack.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_1f5c8eaa-33a2-466a-b626-06cff544461c_300x300.jpg?v=1644953690'
    },
    {
        'id': 714,
        'link': 'https://gimsap.ca/collections/all/products/grounded-ogbono-lb',
        'name': 'Grounded Ogbono /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>The ogbono fruit, also known as a tamarind, is a small, brown, sour fruit that is native to Africa. The seeds of the fruit are dried and ground into a powder, and this powder is what is known as grounded ogbono. Grounded ogbono is a versatile spice that can be used in soups, stews, sauces, and curries. It is also a good substitute for cayenne pepper, which may not be available in some countries. Grounded ogbono has a pungent flavor that can be used to season vegetables, meat, and fish dishes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_96ee2d26-dc76-41c3-8b5e-031dffc787ed_300x300.jpg?v=1645134065'
    },
    {
        'id': 715,
        'link': 'https://gimsap.ca/collections/all/products/grounded-ogbono-0-25lb',
        'name': 'Grounded Ogbono 0.25lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p><span>&nbsp;The ogbono fruit, also known as a tamarind, is a small, brown, sour fruit that is native to Africa. The seeds of the fruit are dried and ground into a powder, and this powder is what is known as grounded ogbono. Grounded ogbono is a versatile spice that can be used in soups, stews, sauces, and curries. It is also a good substitute for cayenne pepper, which may not be available in some countries. Grounded ogbono has a pungent flavor that can be used to season vegetables, meat, and fish dishes.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/20180207_113905_530x_2x_4beb146d-fbfd-4475-b097-c1c9891fb2af_300x300.jpg?v=1651757017'
    },
    {
        'id': 716,
        'link': 'https://gimsap.ca/collections/all/products/grounded-ogbono-0-5lb',
        'name': 'Grounded Ogbono 0.5lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Grounded Ogbono is a natural ingredient used in many dishes in West Africa. This ground ogbono is the best of the best, with no stems or husks, perfect for preparing and cooking dishes such as ogbono soup, ogbono soup with pepper, and ogbono stew. The ground ogbono is an excellent spice to add to your African dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/20180207_113905_530x_2x_d7ed136b-be9a-43fc-9d27-ed8da73cf81b_300x300.jpg?v=1651757050'
    },
    {
        'id': 717,
        'link': 'https://gimsap.ca/collections/all/products/grounded-okrabistak',
        'name': 'Grounded okra(bistak)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p>Grounded okra is a dish that uses the pulp of the okra, which is then cooked with spices.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_31a4aeb7-b076-4454-bdc7-63bba47eff61_300x300.jpg?v=1644951288'
    },
    {
        'id': 718,
        'link': 'https://gimsap.ca/collections/all/products/grounded-peanut-bistak-350g',
        'name': 'Grounded Peanut (Bistak) 350g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Grounded Peanut (Bistak) 350g Tired of shelling peanuts by hand? Tired of getting your hands sticky and peanut-y? Tired of shelling a lot of peanuts and getting a little bit of the good stuff? Then the Grounded Peanut (Bistak) 350g is for you! Grounded Peanut (Bistak) 350g is an easy to use peanut that is pre-shelled.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_75b6709e-0751-4266-9bcf-56db9e5ab386_300x300.jpg?v=1651757278'
    },
    {
        'id': 719,
        'link': 'https://gimsap.ca/collections/all/products/grounded-peanut-bistak-350g-box',
        'name': 'Grounded Peanut (Bistak) 350g Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This box of grounded peanuts comes in a 350g box. Grounded peanuts are an excellent source of protein and they are full of healthy fats.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_dc8a66db-654c-4ef3-9d82-1c0a02b45be6_300x300.jpg?v=1651757329'
    },
    {
        'id': 720,
        'link': 'https://gimsap.ca/collections/all/products/grounded-pepper-10lb',
        'name': 'Grounded Pepper 10lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': '<p>Grounded Pepper is a spice that is often used in many different dishes to add a little bit of spice. It is made from the ground peppercorns that are then finely ground to make the pepper. Grounded Pepper is a great way to make food taste better and spice up the flavor.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8534e9f9-dde3-4a9c-9d1e-b1814b93bc5f_300x300.jpg?v=1645134068'
    },
    {
        'id': 721,
        'link': 'https://gimsap.ca/collections/all/products/grounded-pepper-small-150g',
        'name': 'Grounded Pepper Small 150g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Grounded Pepper Small 150g is a premium quality pepper that is suitable for any dish. Grounded Pepper is a mix of red and black pepper that is grounded, creating a finer grind than most other pepper products. The result is a smooth, consistent texture that provides the perfect balance of flavor and heat. Grounded Pepper can be used in any dish, but is especially good in chicken dishes, grilled vegetables, salads, and soups.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dff55a3b-4e8f-4151-b27a-6c086e709227_300x300.jpg?v=1645134069'
    },
    {
        'id': 722,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-cocktail-peanuts-todaj-big',
        'name': 'Groundnut (Cocktail Peanuts) Todaj Big',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This peanut is slightly smaller than the regular peanut, but they are much sweeter and they are always roasted. The taste is reminiscent of a sugar coated candy and they are great for snacking. They are the perfect size for a cocktail party or gathering, and they can be used as a topping for any dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_7d56a301-1ef6-491a-a79e-db71172a84d2_300x300.jpg?v=1651757521'
    },
    {
        'id': 723,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-peanuts',
        'name': 'Groundnut (Peanuts)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.00',
        'description': '<p>Roasted peanuts or groundnuts in a bottle.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-26_300x300.jpg?v=1606148486'
    },
    {
        'id': 724,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-big-haffinique',
        'name': 'Groundnut Big (Haffinique)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Groundnut Big is a brand of peanut butter that is made with 100% groundnuts and no artificial ingredients. Groundnut Big\'s slogan is "from the ground to the spoon."&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/IX2A0807-4_300x300.jpg?v=1651757818'
    },
    {
        'id': 725,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-big-pack-x12',
        'name': 'Groundnut Big Pack (x12)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Groundnut Big Pack includes 12 individual packages of groundnuts, which are a popular food item in Africa. Groundnuts are a type of peanut that is eaten whole, roasted, or boiled. They are high in protein and also have a significant amount of carbohydrates. They are a great source of nutrients for those who are on a low-fat diet.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_6ae6e644-0d7e-4dc7-a7c5-c6cf40801a99_300x300.jpg?v=1651757874'
    },
    {
        'id': 726,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-big-x12-todaj',
        'name': 'Groundnut Big x12 (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Groundnut Big x12 (Todaj) is a delicious snack made from ground peanuts, and the perfect blend of sweet and salty. Groundnut Big x12 (Todaj) is a delicious snack made from ground peanuts, and the perfect blend of sweet and salty. Groundnut Big x12 (Todaj) are individually wrapped, making them a great option for on-the-go snacking. These snacks are also gluten-free, making them a healthy option for anyone with food allergies.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_3278d674-76b2-459a-a8af-b460f0643278_300x300.jpg?v=1651757903'
    },
    {
        'id': 727,
        'link': 'https://gimsap.ca/collections/all/products/groundnut-paste',
        'name': 'Groundnut Paste',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Groundnut Paste is a traditional African recipe that is made from roasted groundnuts, salt, and palm oil. It is used as a dipping sauce for a variety of African dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ae62cde9-0529-4d90-87c3-0b9beeb73e42_300x300.jpg?v=1645134082'
    },
    {
        'id': 728,
        'link': 'https://gimsap.ca/collections/all/products/grouper-fish-400-600g',
        'name': 'Grouper fish 400-600g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>The grouper fish is a large saltwater fish that can grow up to 1.5 meters in length. It has a grayish-brown coloration and is found in many parts of the world. Grouper fish are a type of saltwater fish that can be cooked in many different ways, such as steaming, frying, and baking.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-05_074705936_300x300.png?v=1651758428'
    },
    {
        'id': 729,
        'link': 'https://gimsap.ca/collections/all/products/growers-peanut',
        'name': 'Growers peanut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>Growers peanut is a food product consisting of peanuts. They are raw, unsalted, and roasted. The peanuts are dry roasted to a light golden brown color. The peanuts are also processed in a way that leaves them dry and crisp.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6b2bd142-e113-4dc2-abf7-b43cc3f430c4_300x300.jpg?v=1645134088'
    },
    {
        'id': 730,
        'link': 'https://gimsap.ca/collections/all/products/guinea-corn-4lb',
        'name': 'Guinea Corn 4lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Guinea Corn is a small, hard, kernel of corn.&nbsp;It is a type of hominy and is also known as&nbsp; maize, or maseca.&nbsp; Guinea Corn is an excellent source of protein, vitamin A, and calcium. It is also gluten-free and has a low glycemic index.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Guinea-Corn-Red_300x300.jpg?v=1651758608'
    },
    {
        'id': 731,
        'link': 'https://gimsap.ca/collections/all/products/guinea-corn-9lbs',
        'name': 'guinea corn 9lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Guinea Corn is a small, hard, kernel of corn.&nbsp;It is a type of hominy and is also known as&nbsp; maize, or maseca.&nbsp; Guinea Corn is an excellent source of protein, vitamin A, and calcium. It is also gluten-free and has a low glycemic index.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d42d42f5-6a30-4de0-a8fc-3eeeb98e397c_300x300.jpg?v=1651758910'
    },
    {
        'id': 732,
        'link': 'https://gimsap.ca/collections/all/products/guinea-corn-powder',
        'name': 'Guinea Corn Powder',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>This is a product that is derived from a grain called Guinea Corn. It is the main ingredient in this product. It is a hardy cereal grain that is grown in many different parts of the world. It is used in this product because it is high in protein and has a low glycemic index. This product is perfect for people who are trying to eat more protein and avoid carbohydrates that have a high glycemic index.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_99309c04-83cb-450f-a3c1-f59977b6c841_300x300.jpg?v=1645134091'
    },
    {
        'id': 733,
        'link': 'https://gimsap.ca/collections/all/products/guinea-corn-powder-graceco-500g',
        'name': 'Guinea Corn Powder (Graceco) 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p>&nbsp;</p>\n<p><span>This is a product that is derived from a grain called Guinea Corn.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/download_931b14cb-de64-42f1-8474-b80440e40ec6_300x300.jpg?v=1651758959'
    },
    {
        'id': 734,
        'link': 'https://gimsap.ca/collections/all/products/habanero-pepper-per-lb-ata-rodo',
        'name': 'Habanero Pepper (Ata Rodo)',
        'price': 'From $10.00',
        'description': '<p>The Habanero pepper is a red chili pepper. The peppers are hot and spicy, but the flavor can be diminished by soaking the peppers in vinegar or lemon juice. The Habanero pepper has a flavor that is described as fruity and sweet with a bit of smokiness. The peppers are used in sauces, in soups, in salsa, and more. They are also used to make Habanero sauce.&nbsp;</p>\n<p><span>This spicy pepper is not for the faint of heart. It has a Scoville heat rating of 100,000 units. The heat is so intense that many people will only use a little bit at a time. It is a member of the Capsicum family and is a perennial in tropical climates. The Habanero Pepper originated in Central America and is now grown in the US.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_63c3097b-031f-4516-9949-670ffd080b9d_300x300.jpg?v=1645134098'
    },
    {
        'id': 735,
        'link': 'https://gimsap.ca/collections/all/products/habanero-pepper-box-ata-rodo-10lb',
        'name': 'Habanero Pepper (Box) Ata Rodo 10lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>We are pleased to offer our Habanero Pepper in a 10lb box. This spicy pepper is not for the faint of heart. It has a Scoville heat rating of 100,000 units. The heat is so intense that many people will only use a little bit at a time. It is a member of the Capsicum family and is a perennial in tropical climates.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_12cd2d98-84ab-41c9-a32b-d09c827072bb_300x300.jpg?v=1645134095'
    },
    {
        'id': 736,
        'link': 'https://gimsap.ca/collections/all/products/habanero-pepper-m',
        'name': 'Habanero Pepper (M)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>This red Habanero pepper is a versatile, flavorful and hot pepper that is used in a variety of cuisines. The Habanero pepper is one of the most popular peppers in the world and is used in many recipes, both sweet and savory. These peppers are known for their rich, spicy flavor and their heat. They are often found in salsas, curries, stir-fries, and sauces. Habanero peppers are about 2 inches long and 1 inch wide.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_32be362a-5757-4fd6-99fc-a3843dd91258_300x300.jpg?v=1645134097'
    },
    {
        'id': 737,
        'link': 'https://gimsap.ca/collections/all/products/hair-bonding-glue-30ml-salon-pro',
        'name': 'Hair Bonding Glue 30ml (Salon Pro)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>Hair Bonding Glue is a clear, fast-drying, adhesive for use in the hair styling industry. It is a glue for hair bonding and is also water-resistant. Hair Bonding Glue is water-resistant, dries clear, and can be used for hair bonding. It can be used for all hair types and can be used on synthetic hair.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cb34bead-20d4-4ea5-93c5-df2670b2cf91_300x300.jpg?v=1645134099'
    },
    {
        'id': 738,
        'link': 'https://gimsap.ca/collections/all/products/hair-bonding-glue-60ml-salon-pro',
        'name': 'Hair Bonding Glue 60ml (Salon Pro)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p><span>Hair Bonding Glue is a clear, fast-drying, adhesive for use in the hair styling industry. It is a glue for hair bonding and is also water-resistant. Hair Bonding Glue is water-resistant, dries clear, and can be used for hair bonding. It can be used for all hair types and can be used on synthetic hair.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a0552cfc-7eeb-46de-8520-885a98f7f343_300x300.jpg?v=1645134101'
    },
    {
        'id': 739,
        'link': 'https://gimsap.ca/collections/all/products/hair-decoration-yarn-for-braid-assorted',
        'name': 'Hair Decoration Yarn For Braid Assorted',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>This is a 100% cotton yarn that is perfect for braiding hair. The yarn is available in an assortment of colors and includes a hair tie, hair comb, and hairband.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dd9ad8a2-4d85-4dad-bd18-3dd871852820_300x300.jpg?v=1651759158'
    },
    {
        'id': 740,
        'link': 'https://gimsap.ca/collections/all/products/hair-decoration-yarn-for-braid-assorted-shiny',
        'name': 'Hair Decoration Yarn For Braid Assorted Shiny',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>This is a 100% cotton yarn that is perfect for braiding hair. The yarn is available in an assortment of colors and includes a hair tie, hair comb, and hairband.</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6cc684a1-2cde-448b-bc2a-3d1d851ed5e3_300x300.jpg?v=1645134103'
    },
    {
        'id': 741,
        'link': 'https://gimsap.ca/collections/all/products/hair-decoration-yarn-for-braid-elastic-assorted',
        'name': 'Hair Decoration Yarn For Braid Elastic Assorted',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>This is a 100% cotton yarn that is perfect for braiding hair. The yarn is available in an assortment of colors and includes a hair tie, hair comb, and hairband.</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_688691db-e5a0-40aa-9467-6ed75fee8666_300x300.jpg?v=1645134104'
    },
    {
        'id': 742,
        'link': 'https://gimsap.ca/collections/all/products/hair-decoration-yarn-for-braid-silver',
        'name': 'Hair Decoration Yarn For Braid Silver',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>This is a 100% cotton yarn that is perfect for braiding hair. The yarn is available in an assortment of colors and includes a hair tie, hair comb, and hairband.</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Sallyhair-Dreadlocks-12Strands-pack-20inch-10-Colors-Synthetic-Braiding-Hair-Extensions-Crochet-Braids-Hair-White-Silver_jpg_Q90_jpg_300x300.webp?v=1651759286'
    },
    {
        'id': 743,
        'link': 'https://gimsap.ca/collections/all/products/hair-net-large',
        'name': 'Hair Net (Large)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The hair net is a head covering that protects hair from dirt, dust, and other particles. It is made of cotton, elastic, and mesh and can be worn over hair to keep it neat and tidy. This hair net is a large size that fits most adults.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2b15f527-7646-46c7-b349-a3d9e0fdaac8_300x300.jpg?v=1645134106'
    },
    {
        'id': 744,
        'link': 'https://gimsap.ca/collections/all/products/hair-net-medium',
        'name': 'Hair Net (Medium)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This hair net is perfect for those with long hair. It is designed to go over the head and keep hair from falling in the face. It is made of durable, lightweight nylon and features a small hole in the top for easy removal. It is available in two sizes: small and medium.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/New-Arrival-Women-Ladies-Soft-Rayon-Snood-Hair-Net-Crocheted-Hair-Net-Hot-sale-accessoires-cheveux_jpg_Q90_jpg_c551fe22-8f41-48a2-b78c-c4c74b3b020f_300x300.webp?v=1651759931'
    },
    {
        'id': 745,
        'link': 'https://gimsap.ca/collections/all/products/hair-net-small',
        'name': 'Hair Net (Small)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This small hair net is perfect for women with long hair who are looking for a way to keep their hair out of their face while they cook, clean, or do other chores. The hair net has a hook and loop closure at the back for a snug fit.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6e9e8a1e-faa3-43ae-8549-306a41d35e29_300x300.jpg?v=1645134108'
    },
    {
        'id': 746,
        'link': 'https://gimsap.ca/collections/all/products/hake-fish',
        'name': 'Hake Fish',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': '<p>Hake is a fish that has a delicate, light flavor. It is best when cooked with butter and lemon. The hake fish is the perfect dinner dish for any night of the week. The delicate, light flavor is best when cooked with butter and lemon.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/U80fe93da126742169e70fb0bed132aef5_300x300.jpg?v=1651770973'
    },
    {
        'id': 747,
        'link': 'https://gimsap.ca/collections/all/products/half-box-spinach-chopped',
        'name': 'Half Box Spinach chopped',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $26.00',
        'description': "<p>This chopped spinach is packaged in a half-box, so it's perfect for any size meal. Just open the box and serve. It's great for your salads, pasta, omelets, and more.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/123098661_105254771389345_6165464606489692479_n_300x300.jpg?v=1651772276'
    },
    {
        'id': 748,
        'link': 'https://gimsap.ca/collections/all/products/half-box-spinach-chopped-10pc',
        'name': 'Half Box Spinach chopped (10pc)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.00',
        'description': "<p>It's all about the greens. You can't go wrong with spinach, and you can't go wrong with this half box of chopped spinach. It's all about the greens.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/123098661_105254771389345_6165464606489692479_n_e7d87b45-ce16-4ae0-852e-852fad0e4846_300x300.jpg?v=1651772342'
    },
    {
        'id': 749,
        'link': 'https://gimsap.ca/collections/all/products/halibut',
        'name': 'Halibut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': "<p>Halibut is a meaty, white-fleshed fish that is known for its delicate flavor and texture. The flesh is firmer than cod or salmon, but softer than trout or bass. Halibut is a fish that's at home in the deep waters of the ocean, and it's a hearty fish that will give you a lot of protein.</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_15439fe4-9fc2-4ec1-986e-34466ed2a0ad_300x300.jpg?v=1645134111'
    },
    {
        'id': 750,
        'link': 'https://gimsap.ca/collections/all/products/halo-halofruit-mix',
        'name': 'Halo-halo(fruit mix)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $69.60',
        'description': '<p>Halo-halo is a Filipino dessert made of shaved ice, various combinations of fruits, coconut milk, and ice cream. The mix of ingredients is placed in a large bowl, with a large scoop of ice cream in the center. This dessert is typically served with a variety of sauces, such as ube, leche flan, and condensed milk.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_042108832_300x300.png?v=1652264472'
    },
    {
        'id': 751,
        'link': 'https://gimsap.ca/collections/all/products/hard-chicken-cut-lb',
        'name': 'Hard Chicken Cut /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.05',
        'description': "<p>Hard Chicken Cut in pounds. Our Hard Chicken Cut is&nbsp;frozen and cut up into pieces. It's perfect for cooking. It's perfect for any recipe.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_042723111_300x300.png?v=1652264847'
    },
    {
        'id': 752,
        'link': 'https://gimsap.ca/collections/all/products/hard-chicken-leg-and-back-10kg',
        'name': 'Hard Chicken Leg Quarters 10kg (Back Attached)',
        'price': 'From $40.00',
        'description': 'Hard Chicken (Heavy/Mature Fowl) Legs quartered with back attached. Available cut &amp; uncut.',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/resize_300x300.webp?v=1647367655'
    },
    {
        'id': 753,
        'link': 'https://gimsap.ca/collections/all/products/hausa-koko-comas',
        'name': 'Hausa Koko (Comas)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>Hausa Koko (Comas) is a traditional Hausa dish consisting of a mixture of ground peanuts, honey, salt, and water. Hausa Koko is often served with a doughnut-like bread called “Nankhatai”. The dish is usually eaten as a snack or a light meal.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_25885ec9-38f4-4f39-8b80-4aa5df66fc15_300x300.jpg?v=1645134115'
    },
    {
        'id': 754,
        'link': 'https://gimsap.ca/collections/all/products/hausa-koko-endlesslove',
        'name': 'Hausa Koko (endlesslove)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Hausa Koko is a traditional Hausa dish consisting of a mixture of ground peanuts, honey, salt, and water. Hausa Koko is often served with a doughnut-like bread called “Nankhatai”. The dish is usually eaten as a snack or a light meal.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_043144940_300x300.png?v=1652265107'
    },
    {
        'id': 755,
        'link': 'https://gimsap.ca/collections/all/products/hausa-koko-home-fresh-400g',
        'name': 'Hausa Koko (Home fresh) 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.25',
        'description': '<p>This authentic Hausa Koko is a traditional Nigerian dish made from mashed and cooked corn and black-eyed peas, combined with tomatoes, onions, and various spices. It is often served with rice or with boiled cassava.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8e98d486-db2f-437c-b285-cf60b32f57ca_300x300.jpg?v=1645134117'
    },
    {
        'id': 756,
        'link': 'https://gimsap.ca/collections/all/products/hausa-koko-home-fresh-400g-box',
        'name': 'Hausa Koko (Home fresh) 400g  Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $145.00',
        'description': '<p><meta charset="utf-8"><span>This authentic Hausa Koko is a traditional Nigerian dish made from mashed and cooked corn and black-eyed peas, combined with tomatoes, onions, and various spices. It is often served with rice or with boiled cassava.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f1fb3445-bb58-41e5-9b1c-2adbf1b40023_300x300.jpg?v=1645134118'
    },
    {
        'id': 757,
        'link': 'https://gimsap.ca/collections/all/products/hausa-koko-no-1-choice',
        'name': 'Hausa Koko (No 1 choice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p><meta charset="utf-8"><span>This authentic Hausa Koko is a traditional Nigerian dish made from mashed and cooked corn and black-eyed peas, combined with tomatoes, onions, and various spices. It is often served with rice or with boiled cassava.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_043717962_300x300.png?v=1652265440'
    },
    {
        'id': 758,
        'link': 'https://gimsap.ca/collections/all/products/heney-well-semolina-5kg',
        'name': 'Heney well Semolina 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Semolina is a coarse, high-protein wheat flour that is typically used in making pastas, breads, and other baked goods. It is a great source of protein and is often used in gluten-free recipes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e71314a0-b331-4a73-b86f-9eee1f1097ce_300x300.jpg?v=1645134120'
    },
    {
        'id': 759,
        'link': 'https://gimsap.ca/collections/all/products/hermine-lip-oil-rose-hip-0-52oz',
        'name': 'HERMINE Lip Oil Rose Hip (0.52oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': "<p>If you're looking for a high-quality lip product that is rich in natural ingredients, HERMINE Lip Oil Rose Hip is the perfect choice. This lip oil is made with jojoba oil, rose hip oil, and natural vitamin E. It will leave your lips feeling hydrated and looking healthy. It can be used before applying lipstick or gloss, or as a treatment on its own.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bcd3afd6-2509-4c10-852f-687aa2fa3eeb_300x300.jpg?v=1645134121'
    },
    {
        'id': 760,
        'link': 'https://gimsap.ca/collections/all/products/hermine-lip-oil-strawberry-0-52oz',
        'name': 'HERMINE Lip Oil Strawberry (0.52oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">If you\'re looking for a high-quality lip product that is rich in natural ingredients, HERMINE Lip Oil Rose Hip is the perfect choice. This lip oil is made with jojoba oil, rose hip oil, and natural vitamin E. It will leave your lips feeling hydrated and looking healthy. It can be used before applying lipstick or gloss, or as a treatment on its own.</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d6806f4d-3333-432d-a622-7e1bfc612cf3_300x300.jpg?v=1645134122'
    },
    {
        'id': 761,
        'link': 'https://gimsap.ca/collections/all/products/herring-shawa-dried-fish-box',
        'name': 'Herring (shawa) dried fish box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Herring is a salt-cured fish with a long, slender body. It is the most common fish in Scandinavia and has been a staple of the region for centuries. The Herring is cured in salt and other spices, which removes the excess water and creates a flavorful, air-dried fish. It is used as a flavoring in various dishes, and is also eaten raw.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_051218968_300x300.png?v=1652267543'
    },
    {
        'id': 762,
        'link': 'https://gimsap.ca/collections/all/products/herring-shawa-dried-fish-per-lb',
        'name': 'Herring (shawa) dried fish per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<meta charset="utf-8">\n<p data-mce-fragment="1">Herring is a salt-cured fish with a long, slender body. It is the most common fish in Scandinavia and has been a staple of the region for centuries. The Herring is cured in salt and other spices, which removes the excess water and creates a flavorful, air-dried fish. It is used as a flavoring in various dishes, and is also eaten raw.&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_051430561_300x300.png?v=1652267675'
    },
    {
        'id': 763,
        'link': 'https://gimsap.ca/collections/all/products/hi-malt',
        'name': 'Hi-malt',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>Hi-malt is a natural, all-natural, organic malt extract made from barley. It is gluten-free, and can be used to create a variety of delicious recipes including beer, malt vinegar, and even traditional English breakfast tea. It has a light flavor and can be used to replace sugar or molasses in recipes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1ab2510a-e922-479e-a915-a5fed534bbde_300x300.jpg?v=1645134126'
    },
    {
        'id': 764,
        'link': 'https://gimsap.ca/collections/all/products/home-fresh-palm-cream',
        'name': 'Home fresh Palm Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': "<p>Home fresh&nbsp;Palm Cream is creamy and delicious, and it's made with only 100% pure ingredients. You can enjoy Home fresh Palm Cream guilt-free!</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_051613662_300x300.png?v=1652267776'
    },
    {
        'id': 765,
        'link': 'https://gimsap.ca/collections/all/products/home-fresh-palm-oil-2l-piece',
        'name': 'Home Fresh Palm Oil 2L (piece)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': '<p>Home Fresh Palm Oil is a versatile, sustainable, and healthy cooking oil. The palm oil comes from sustainable sources and is an excellent source of antioxidants, vitamins, and minerals. The taste is subtle and light, with a hint of sweetness.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_053825233_300x300.png?v=1652269108'
    },
    {
        'id': 766,
        'link': 'https://gimsap.ca/collections/all/products/home-fresh-palm-oil-2l-box',
        'name': 'Home Fresh Palm Oil 2L Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $85.00',
        'description': '<p>Home Fresh Palm Oil is a versatile, sustainable, and healthy cooking oil. The palm oil comes from sustainable sources and is an excellent source of antioxidants, vitamins, and minerals. The taste is subtle and light, with a hint of sweetness.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_053910310_300x300.png?v=1652269154'
    },
    {
        'id': 767,
        'link': 'https://gimsap.ca/collections/all/products/home-fresh-plantain-fufu-24oz-1-5-lb',
        'name': 'Home Fresh Plantain Fufu 24oz ((1.5 lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Home Fresh Plantain Fufu is made from fresh plantains, cassava, and other ingredients to make a deliciously rich and thick fufu that is perfect for cooking up some Nigerian Jollof Rice.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c96112c7-71ff-4e2f-a094-2f8cda8eb63c_300x300.jpg?v=1645134130'
    },
    {
        'id': 768,
        'link': 'https://gimsap.ca/collections/all/products/honey-oloyin-beans',
        'name': 'Honey (Oloyin) Beans',
        'price': 'From $13.00',
        'description': '<p>Honey Beans (also known as ewa oloyin or nigerian brown beans) are a naturally sweet beans that are high in protein. Our beans have been picked clean and are free from chemical preservatives. Ethically sourced.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/ScreenShot2022-03-17at3.18.06PM_300x300.png?v=1647551920'
    },
    {
        'id': 769,
        'link': 'https://gimsap.ca/collections/all/products/honey-comb-10lb',
        'name': 'Honey Comb 10lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $62.50',
        'description': '<p>Honey Comb 10lb This 10lb package of Honey Comb is the perfect way to indulge in your favorite sweet treat. Honey is harvested from bees and has been used as a natural sweetener for centuries.&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f2a1b095-0d1f-44ba-b4fa-c50f2868119f_300x300.jpg?v=1645134149'
    },
    {
        'id': 770,
        'link': 'https://gimsap.ca/collections/all/products/honey-ginger-tea-20x18x18g',
        'name': 'Honey Ginger Tea 20x18x18g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Honey Ginger Tea is a natural, refreshing drink that provides many health benefits. Made with pure honey and ginger, this tea is made with only the finest ingredients. The ginger provides relief from nausea, and the honey is a natural anti-inflammatory. The tea is caffeine-free and safe for children and pregnant women.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cbfc61c3-a984-4e3b-aa33-4c66a07f45c1_300x300.jpg?v=1645134150'
    },
    {
        'id': 771,
        'link': 'https://gimsap.ca/collections/all/products/honey-ginger-tea-w-lemon-20x18x18g',
        'name': 'Honey Ginger Tea w/ Lemon 20x18x18g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Ginger tea is made by steeping ginger root in hot water. The resulting liquid is a golden-brown color and has a taste that is both spicy and sweet. This ginger tea is made with honey and lemon. The tea is rich in antioxidants and can be used to treat a variety of ailments, including nausea, vomiting, stomach aches, and diarrhea.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_054234391_300x300.png?v=1652269429'
    },
    {
        'id': 772,
        'link': 'https://gimsap.ca/collections/all/products/honey-ginger-tea-w-mint-20x18x18g',
        'name': 'Honey Ginger Tea w/ Mint 20x18x18g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>This iced tea is made with organic ginger, organic honey, and organic mint. It is perfect for anyone who is looking for a refreshing drink.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_62a7c6da-55b2-484e-a32a-7641fa6388ab_300x300.jpg?v=1645134152'
    },
    {
        'id': 773,
        'link': 'https://gimsap.ca/collections/all/products/honey-well-semolina-5kg',
        'name': 'Honey well Semolina 5Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p><meta charset="utf-8"><span>Semolina is a coarse, high-protein wheat flour that is typically used in making pastas, breads, and other baked goods. It is a great source of protein and is often used in gluten-free recipes.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8742aceb-368c-4e3d-b0a7-d2f0a0d89229_300x300.jpg?v=1645134153'
    },
    {
        'id': 774,
        'link': 'https://gimsap.ca/collections/all/products/horlicks-chocolate-24x500g-box',
        'name': 'Horlicks Chocolate 24x500g  Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $200.00',
        'description': '<p>The Horlicks Chocolate 24x500g Box is a perfect gift for any occasion. They are also great for stocking stuffers or to have on hand for emergencies. Each box contains 24 500g containers of Horlicks Chocolate and will last up to a year if stored properly. This product is perfect for anyone who enjoys a chocolatey drink that is not too sweet.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9f6b73fd-504c-4f6a-85ed-e97ecb4285a8_300x300.jpg?v=1645134154'
    },
    {
        'id': 775,
        'link': 'https://gimsap.ca/collections/all/products/horlicks-chocolate-500g',
        'name': 'Horlicks Chocolate 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': "<p>Makes you feel good The perfect companion for any situation Chocolate flavoured Horlicks is a nutritious and delicious drink. Horlicks Chocolate is made with the goodness of Horlicks and cocoa powder. Enjoy a rich chocolate taste, while still getting the goodness of Horlicks. It's time to indulge.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f2a8f0a6-0c86-4284-b0f3-10ec33f5c780_300x300.jpg?v=1645134155'
    },
    {
        'id': 776,
        'link': 'https://gimsap.ca/collections/all/products/horlicks-plain-classic-24x500g-box',
        'name': 'Horlicks Plain (classic) 24x500g  Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $200.00',
        'description': '<p>Horlicks is a popular malted milk drink that is sold in a variety of flavors. The Plain variety is typically used as a base for other Horlicks flavors, but it can also be enjoyed on its own. This product is perfect for those who enjoy a quick and easy breakfast or want to make a healthy drink to keep them going through the day.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_44eee5b2-b71e-420c-b2fb-9242fc2cc0e9_300x300.jpg?v=1645134156'
    },
    {
        'id': 777,
        'link': 'https://gimsap.ca/collections/all/products/horlicks-plain-classic-500g',
        'name': 'Horlicks Plain (classic) 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p><meta charset="utf-8"><span>Horlicks is a popular malted milk drink that is sold in a variety of flavors. The Plain variety is typically used as a base for other Horlicks flavors, but it can also be enjoyed on its own. This product is perfect for those who enjoy a quick and easy breakfast or want to make a healthy drink to keep them going through the day.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fe72977b-cca9-41e3-8f38-48cb375ffe9f_300x300.jpg?v=1645134157'
    },
    {
        'id': 778,
        'link': 'https://gimsap.ca/collections/all/products/horse-mackerel-per-lb',
        'name': 'Horse Mackerel (per lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': "<p>It's time to experience the bounty of the sea with our delicious Horse Mackerel. Mackerel is a saltwater fish that is often used for cooking because of its delicious taste and tender meat. It's easy to prepare, as it is usually cooked with butter, lemon, and black pepper.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_88821d11-5ce3-43d3-9a60-28029cb56aec_300x300.jpg?v=1645134160'
    },
    {
        'id': 779,
        'link': 'https://gimsap.ca/collections/all/products/horse-mackerel-20kg-box',
        'name': 'Horse Mackerel 20kg box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $125.00',
        'description': '<p><meta charset="utf-8"><span>It\'s time to experience the bounty of the sea with our delicious Horse Mackerel. Mackerel is a saltwater fish that is often used for cooking because of its delicious taste and tender meat. It\'s easy to prepare, as it is usually cooked with butter, lemon, and black pepper.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_82eb06f9-ecec-48c8-90f8-a0e5db2dea96_300x300.jpg?v=1645134158'
    },
    {
        'id': 780,
        'link': 'https://gimsap.ca/collections/all/products/horse-mackerel-22-5-lbs-box',
        'name': 'Horse Mackerel 22.5 lbs box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $70.00',
        'description': '<p><meta charset="utf-8"><span>It\'s time to experience the bounty of the sea with our delicious Horse Mackerel. Mackerel is a saltwater fish that is often used for cooking because of its delicious taste and tender meat. It\'s easy to prepare, as it is usually cooked with butter, lemon, and black pepper.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_054950314_300x300.png?v=1652269794'
    },
    {
        'id': 781,
        'link': 'https://gimsap.ca/collections/all/products/huile-de-beaute-125-ml',
        'name': 'Huile de beaute 125 mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p>Huile de beaute is a rich, concentrated formula that melts onto skin to nourish and protect with a natural blend of botanical oils. This lightweight and fast-absorbing formula is a multi-tasker that can be used as a daily moisturizer, makeup remover, cuticle oil, and more.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_055157129_300x300.png?v=1652269919'
    },
    {
        'id': 782,
        'link': 'https://gimsap.ca/collections/all/products/ideal-edge-control',
        'name': 'Ideal Edge Control',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Many people struggle with the challenge of having to style their hair every day. The process can be tedious and time-consuming, but with Ideal Edge Control, that is no longer a problem. Ideal Edge Control is a product that creates a barrier on the hairline to prevent the hair from sticking to the skin and causing an unsightly mess. Ideal Edge Control can be used by both men and women, and it is available in different sizes, so there is a size for everyone.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5b943b4f-d977-461e-8f0d-682b38c35ed3_300x300.jpg?v=1645134162'
    },
    {
        'id': 783,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-pepper-soup-spices-10pck',
        'name': 'IDS INSTANT  (Pepper Soup) Spices 10pck',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': "<p>Pepper soup is a favorite dish that is popular in many cultures. However, it can be difficult to find a good quality pepper soup that doesn't contain meat or have too much salt. IDS INSTANT is a product that offers consumers a way to enjoy the taste of pepper soup without the need for a recipe. The package contains 10 packets of instant pepper soup that are just right for one person. Each packet contains 3 grams of powder and is designed to be mixed with 2 cups of water.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cd5a42a5-bba4-4212-9d5e-9a8a7de28492_300x300.jpg?v=1645134167'
    },
    {
        'id': 784,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-pepper-soup-spices-3pck',
        'name': 'IDS INSTANT  (Pepper Soup) Spices 3pck',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Pepper soup is a favorite dish that is popular in many cultures. However, it can be difficult to find a good quality pepper soup that doesn\'t contain meat or have too much salt. IDS INSTANT is a product that offers consumers a way to enjoy the taste of pepper soup without the need for a recipe.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3d988f47-b2b2-4c73-b2d0-fd3673fb81ce_300x300.jpg?v=1645134168'
    },
    {
        'id': 785,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-pepper-soup-spices-bottle',
        'name': 'IDS INSTANT  (Pepper Soup) Spices bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Pepper soup is a favorite dish that is popular in many cultures. However, it can be difficult to find a good quality pepper soup that doesn\'t contain meat or have too much salt. IDS INSTANT is a product that offers consumers a way to enjoy the taste of pepper soup without the need for a recipe.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_055628504_300x300.png?v=1652270191'
    },
    {
        'id': 786,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-banga-spices6009823590471',
        'name': 'IDS INSTANT (BANGA) Spices6009823590471',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>IDS INSTANT (BANGA) Spices A selection of spicy, tasty Indian-style flavors that can be added to any dish to make it delicious. This product is vegan, gluten-free, and low in sodium.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_055726380_300x300.png?v=1652270249'
    },
    {
        'id': 787,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-pepper-soup-spices-sachet',
        'name': 'IDS INSTANT (Pepper soup) Spices sachet',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>IDS INSTANT (BANGA) Spices. A selection of spicy, tasty Indian-style flavors that can be added to any dish to make it delicious.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d88ca7c5-05fc-4b52-a601-4e168e383981_300x300.jpg?v=1645134170'
    },
    {
        'id': 788,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-banga-spices-bottle',
        'name': 'Ids instant banga spices bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p><meta charset="utf-8"><span>Pepper soup is a favorite dish that is popular in many cultures. However, it can be difficult to find a good quality pepper soup that doesn\'t contain meat or have too much salt. IDS INSTANT is a product that offers consumers a way to enjoy the taste of pepper soup without the need for a recipe.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_060042852_300x300.png?v=1652270445'
    },
    {
        'id': 789,
        'link': 'https://gimsap.ca/collections/all/products/ids-instant-banga-spices-sachet',
        'name': 'Ids instant banga spices sachet',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p><meta charset="utf-8"><span>Pepper soup is a favorite dish that is popular in many cultures. However, it can be difficult to find a good quality pepper soup that doesn\'t contain meat or have too much salt. IDS INSTANT is a product that offers consumers a way to enjoy the taste of pepper soup without the need for a recipe.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_060105545_300x300.png?v=1652270468'
    },
    {
        'id': 790,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari',
        'name': 'Ijebu Gari',
        'price': 'From $9.00',
        'description': '<p>A West African staple made from granulated cassava tubers. It can be eaten in its dry form, soaked, or prepared with hot water. Ijebu Gari has a pleasant sour taste and finer grain than other types of garri.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/GARI_ijebu_300x300.jpg?v=1603147452'
    },
    {
        'id': 791,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-rfv-10lbs',
        'name': 'Ijebu Gari  (RFV) 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.00',
        'description': '<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061250649_300x300.png?v=1652271174'
    },
    {
        'id': 792,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-ks-20lb',
        'name': 'Ijebu gari (KS) 20lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $35.00',
        'description': '<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061516879_300x300.png?v=1652271320'
    },
    {
        'id': 793,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-sultan-1-6kg-3-6lbs',
        'name': 'Ijebu Gari (Sultan 1.6kg) 3.6lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061530948_300x300.png?v=1652271334'
    },
    {
        'id': 794,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-sultan-4-1-9lbs',
        'name': 'Ijebu Gari (Sultan 4.1) 9lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.00',
        'description': '<p>Ijebu Gari is a Nigerian dish that is a favorite in the region.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061545732_300x300.png?v=1652271349'
    },
    {
        'id': 795,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-sultan-8-16-18lbs',
        'name': 'Ijebu Gari (Sultan 8.16) 18lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061625829_300x300.png?v=1652271389'
    },
    {
        'id': 796,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-10kg',
        'name': 'Ijebu Gari 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $40.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061639115_300x300.png?v=1652271402'
    },
    {
        'id': 797,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-10lbs',
        'name': 'Ijebu Gari 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061727995_300x300.png?v=1652271451'
    },
    {
        'id': 798,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-17lbs',
        'name': 'Ijebu Gari 17lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061809796_300x300.png?v=1652271493'
    },
    {
        'id': 799,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-20lb',
        'name': 'Ijebu Gari 20lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $30.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061836648_300x300.png?v=1652271520'
    },
    {
        'id': 800,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-40lbs-todaj',
        'name': 'Ijebu Gari 40lbs (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<meta charset="utf-8"><span>Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061922477_300x300.png?v=1652271568'
    },
    {
        'id': 801,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-50lbs-acm',
        'name': 'Ijebu gari 50lbs (ACM)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_061947061_300x300.png?v=1652271591'
    },
    {
        'id': 802,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-50lbs-todaj',
        'name': 'Ijebu Gari 50lbs (Todaj)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $73.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_062047056_300x300.png?v=1652271650'
    },
    {
        'id': 803,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-5kg',
        'name': 'Ijebu Gari 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_062058429_300x300.png?v=1652271662'
    },
    {
        'id': 804,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-5lbs',
        'name': 'Ijebu Gari 5lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_062114318_300x300.png?v=1652271678'
    },
    {
        'id': 805,
        'link': 'https://gimsap.ca/collections/all/products/ijebu-gari-60lb',
        'name': 'Ijebu Gari 60lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $90.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Ijebu Gari is a Nigerian dish that is a favorite in the region.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_062200723_300x300.png?v=1652271724'
    },
    {
        'id': 806,
        'link': 'https://gimsap.ca/collections/all/products/ilarun',
        'name': 'Ilarun',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Hair care product.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f9306581-ecc2-4c1a-b72c-b7ef425702bb_300x300.jpg?v=1645134184'
    },
    {
        'id': 807,
        'link': 'https://gimsap.ca/collections/all/products/indomie-indonesia-vegetable-flavour-75g',
        'name': 'Indomie (Indonesia) Vegetable flavour 75g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.55',
        'description': '<p>Indomie is a popular Asian brand of instant noodles, originating from Indonesia. This product, Vegetable flavour, is available in 75g packs. Indomie noodles are a convenient, quick meal option, with the dry noodles mixed with water to create a tasty meal.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_27360ddb-9e27-4aea-a8c0-a6b47733c158_300x300.jpg?v=1645134198'
    },
    {
        'id': 808,
        'link': 'https://gimsap.ca/collections/all/products/indomie-indonesia-vegetable-flavour-box',
        'name': 'Indomie (Indonesia) Vegetable flavour Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.00',
        'description': '<p>This particular product is the vegetable flavour, which is popular in Asia. The noodles are made from wheat flour, palm oil, salt, spices, and onion. It is designed to be cooked in boiling water for 3 minutes. The box contains 10 individual servings.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6edd2abe-dacc-41a0-827d-a7d3aab6ba03_300x300.jpg?v=1645134199'
    },
    {
        'id': 809,
        'link': 'https://gimsap.ca/collections/all/products/indomie-120g',
        'name': 'Indomie 120g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $45.00',
        'description': '<p>&nbsp;The noodles are made from rice flour and are boiled for three minutes. The noodles are then seasoned with soy sauce, vinegar, chili, and salt. The noodles are served with a variety of seasonings, including tomato, green beans, and ketchup.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e886c733-fb01-4f74-98d9-d7fc97a96df6_300x300.jpg?v=1645134185'
    },
    {
        'id': 810,
        'link': 'https://gimsap.ca/collections/all/products/indomie-130g',
        'name': 'indomie 130g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.50',
        'description': '<p>Noodle lovers rejoice! Indomie noodles are the perfect meal for any occasion. These tasty noodles are available in various shapes and flavors to satisfy any craving. Indomie noodles are cooked and seasoned with traditional spices to give them a delicious taste. Indomie noodles are available in 130g packs for convenience.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_03600daf-7b5e-4851-8cd1-814e8cadf61c_300x300.jpg?v=1645134186'
    },
    {
        'id': 811,
        'link': 'https://gimsap.ca/collections/all/products/indomie-instant-noodles-chicken-flavour',
        'name': 'Indomie Instant Noodles - Chicken Flavour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Indomie Instant Noodles are delicious, convenient, and quick. They are the perfect choice for a busy lunch break or an easy dinner on the go.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_51f0ecdd-13e7-46f1-8249-13379927642a_300x300.jpg?v=1645134200'
    },
    {
        'id': 812,
        'link': 'https://gimsap.ca/collections/all/products/indomie-instant-noodles-onion-chicken-flavour',
        'name': 'Indomie Instant Noodles - Onion Chicken Flavour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p>Indomie Instant Noodles - Onion Chicken Flavour Indomie Instant Noodles are an all-time favourite of many. They are a versatile and tasty dish that can be enjoyed as a snack, a meal, or as a late-night snack. These noodles are made from premium quality ingredients and are cooked in just three minutes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f208161b-ff81-4d76-aafa-cd9bee8dca3d_300x300.jpg?v=1645134202'
    },
    {
        'id': 813,
        'link': 'https://gimsap.ca/collections/all/products/indomie-instant-noodles-chicken-flavour-box',
        'name': 'Indomie Instant Noodles Chicken Flavour Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.50',
        'description': "<p>Indomie Instant Noodles Chicken Flavour Box is a great meal to eat when you're on the go. It is made from natural ingredients and has a light, savory taste.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9e684c59-ad0e-4d08-a227-08325ef99a88_300x300.jpg?v=1645134201'
    },
    {
        'id': 814,
        'link': 'https://gimsap.ca/collections/all/products/indomie-instant-noodles-onion-chicken-flavour-box',
        'name': 'Indomie Instant Noodles Onion Chicken Flavour Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.50',
        'description': '<p>Indomie Instant Noodles Onion Chicken Flavour Box is a spicy, savory, and flavorful instant noodle that can be eaten as a meal or a snack. These noodles are ready in 3 minutes and can be eaten straight out of the packet or cooked in a microwave. The flavor of these noodles is a delicious combination of onion, garlic, and spices that will keep you coming back for more.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9a0c7d30-c0e2-412f-bf54-4af2dd0c2708_300x300.jpg?v=1645134204'
    },
    {
        'id': 815,
        'link': 'https://gimsap.ca/collections/all/products/indomie70g-piece',
        'name': 'indomie70g piece',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.80',
        'description': '<p>In just a few minutes, you can have a quick and delicious meal with Indomie Mi Goreng noodles. They are the perfect choice for anyone looking for a fast, healthy, and filling meal. The noodles are available in two flavors: chicken and shrimp. The noodles are made from a variety of natural ingredients, including wheat flour, palm oil, salt, and MSG.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0990db20-e8ed-4b6d-9d6d-f28a87188288_300x300.jpg?v=1645134187'
    },
    {
        'id': 816,
        'link': 'https://gimsap.ca/collections/all/products/instant-honeyed-ginger-drink',
        'name': 'Instant Honeyed Ginger Drink',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.50',
        'description': '<p>A&nbsp;healthy, ready-to-drink, honeyed ginger drink. It is available in three flavors: Original,&nbsp;Mint and Lemon.&nbsp;It is a great alternative to other high-sugar drinks on the market. It is low in calories and high in antioxidants. With a mild ginger flavor and hints of honey, it tastes great and can be enjoyed any time of day.&nbsp;<span data-mce-fragment="1">This product can be enjoyed as a warm drink on a cold day or as a cold drink on a hot day. It is a refreshing drink that will bring warmth to your soul. This drink mix can be prepared in just minutes. Simply add hot water and stir.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/InstantHoneyedGingerDrink_300x300.jpg?v=1646875111'
    },
    {
        'id': 817,
        'link': 'https://gimsap.ca/collections/all/products/irish-spring',
        'name': 'Irish Spring',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Irish Spring soap is a quality product that has been used for decades by many people. The soap is made with Irish moss, which is a natural plant that grows in Ireland. This soap is known for its rich lather and natural scent. The soap is available in a variety of different scents and sizes. The bar soap is also a favorite of many athletes. It can be used as a body wash, shampoo, and conditioner. The soap is gentle on the skin and is not irritating to the eyes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_070157943_300x300.png?v=1652274124'
    },
    {
        'id': 818,
        'link': 'https://gimsap.ca/collections/all/products/iyan-ado-10lbs',
        'name': 'Iyan Ado 10lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $28.00',
        'description': 'Iyan Ado can be made into pounded yam.\n<p>&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ba89aa2d-442b-4a50-8655-972748c993b3_300x300.jpg?v=1645134211'
    },
    {
        'id': 819,
        'link': 'https://gimsap.ca/collections/all/products/iyan-ado-20lbs',
        'name': 'Iyan Ado 20lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $54.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Iyan Ado can be made into pounded yam.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a40bb332-34d8-475b-9c81-f82fff7db740_300x300.jpg?v=1645134212'
    },
    {
        'id': 820,
        'link': 'https://gimsap.ca/collections/all/products/iyan-ado-4lbs',
        'name': 'Iyan Ado 4lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.00',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Iyan Ado can be made into pounded yam.</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5ebc9c4f-e691-4e71-82c6-7cce8f3e7cd3_300x300.jpg?v=1645134212'
    },
    {
        'id': 821,
        'link': 'https://gimsap.ca/collections/all/products/jam-condition-shine-gel',
        'name': 'Jam Condition &amp; Shine Gel',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': '<p>This all-natural jam is made with fresh fruits and the best quality ingredients. It is preservative-free and gluten-free. The sweet and tangy flavor is perfect for toast, waffles, pancakes, and more. The ingredients are hand-picked and blended together to create a jam that is made for any time of day.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ecd064bb-c428-48e4-81e4-8033e306583e_300x300.jpg?v=1645134221'
    },
    {
        'id': 822,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-black-castor-oil',
        'name': 'Jamaican Black Castor Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Jamaican Black Castor Oil is a natural product extracted from the seeds of the plant called Ricinus communis. It is a thick, dark, sticky oil that is made up of many different fatty acids. Jamaican Black Castor Oil is a rich source of vitamin E, calcium, and potassium. It is also a source of linoleic acid, which is an omega-6 fatty acid. Jamaican Black Castor Oil has been used for centuries to treat skin problems such as eczema, psoriasis, and acne. It is also known to stimulate hair growth and to be a potent anti-inflammatory.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d6379bb5-7580-4fec-b56c-4f07c13b27d5_300x300.jpg?v=1645134213'
    },
    {
        'id': 823,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-black-castor-oil-co-wash',
        'name': 'Jamaican Black Castor Oil Co-Wash',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>&nbsp;</p>\n<p><meta charset="utf-8"><span>Jamaican Black Castor Oil is a natural product extracted from the seeds of the plant called Ricinus communis. It is a thick, dark, sticky oil that is made up of many different fatty acids. Jamaican Black Castor Oil is a rich source of vitamin E, calcium, and potassium. It is also a source of linoleic acid, which is an omega-6 fatty acid. Jamaican Black Castor Oil has been used for centuries to treat skin problems such as eczema, psoriasis, and acne. It is also known to stimulate hair growth and to be a potent anti-inflammatory.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2a1cd0ba-218f-4744-a891-a92e68df7458_300x300.jpg?v=1645134214'
    },
    {
        'id': 824,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-black-castor-oil-lavender',
        'name': 'Jamaican Black Castor Oil Lavender.',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>What is Jamaican Black Castor Oil Lavender? Jamaican Black Castor Oil Lavender is a plant-based hair and skin product. It is a combination of Jamaican Black Castor Oil and lavender essential oil. This combination is perfect for people who want to maintain their hair and skin. It has the added benefit of a light, pleasant lavender scent. How does Jamaican Black Castor Oil Lavender work? Jamaican Black Castor Oil Lavender will provide many benefits to your hair and skin. The Jamaican Black Castor Oil will help to condition your hair and provide a deep, penetrating shine.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_25cdfd9d-a29e-4784-a2fc-da3af2fc5619_300x300.jpg?v=1645134215'
    },
    {
        'id': 825,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-black-rosemarry',
        'name': 'Jamaican Black Rosemarry.',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p><meta charset="utf-8"><span>A quick, easy and effective way to grow your hair and get rid of split ends, Jamaican Black Castor Oil Rosemary hair growth treatment is made with 100% pure castor oil, black Jamaican castor oil, rosemary essential oil, and vitamin E.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cb24f21c-743a-479a-99a0-fa64eb352ea1_300x300.jpg?v=1645134216'
    },
    {
        'id': 826,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-castor-oil-mist',
        'name': 'Jamaican Castor Oil Mist',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Jamaican Castor Oil Mist is a hair and skin care product that contains 100% pure Jamaican castor oil. The product is an all-natural, organic product that has been used for centuries to help hair grow. The product also has a variety of other benefits such as protecting the skin from UV rays, preventing acne, soothing a sunburn, and reducing inflammation.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d7ebc2e3-0836-48cf-a19a-2a79c7d85e24_300x300.jpg?v=1645134217'
    },
    {
        'id': 827,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-curry-powder-170g',
        'name': 'Jamaican Curry Powder  170g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Jamaican Curry Powder is a blend of the finest spices from the West Indies, East Indies, and Africa. The blend includes turmeric, coriander, cumin, fenugreek, ginger, cinnamon, black pepper, nutmeg, and allspice. This delicious blend is perfect for making Jamaican dishes such as chicken curry or Jamaican beef curry.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e5277ea1-e6ab-481c-bbd9-e632e8c212da_300x300.jpg?v=1645134218'
    },
    {
        'id': 828,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-hot-curry-powder-110g',
        'name': 'Jamaican hot curry powder 110g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.70',
        'description': '<p>There is no better way to prepare a hot and spicy dish than with Jamaican hot curry powder. This blend of spices is a deliciously spicy blend of cumin, coriander, ginger, turmeric, chilies, black pepper, and more.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_07e8a2f0-69d3-4b47-8c86-c02d0713823e_300x300.jpg?v=1645134219'
    },
    {
        'id': 829,
        'link': 'https://gimsap.ca/collections/all/products/jamaican-twist-colour-2',
        'name': 'Jamaican Twist Colour 2',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_071618551_300x300.png?v=1652274980'
    },
    {
        'id': 830,
        'link': 'https://gimsap.ca/collections/all/products/jassan-bened-28-lb-box',
        'name': 'Jassan (Bened) 28 lb box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $300.00',
        'description': '<p>??</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_071734678_300x300.png?v=1652275057'
    },
    {
        'id': 831,
        'link': 'https://gimsap.ca/collections/all/products/jassan-bened-per-lb',
        'name': 'Jassan (Bened) per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.00',
        'description': '<p>??</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_071839517_300x300.png?v=1652275121'
    },
    {
        'id': 832,
        'link': 'https://gimsap.ca/collections/all/products/jerk-bbq-sauce-480ml',
        'name': 'Jerk BBQ Sauce 480mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p>Specially blended with fresh pineapple, allspice, ginger, brown sugar, and other herbs and spices, this Jerk BBQ Sauce will have your mouth watering in no time. Try it on chicken, pork, and even beef for a zesty and sweet taste.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b38f3094-ffe7-4e70-960a-ac0ebb86f570_300x300.jpg?v=1645134225'
    },
    {
        'id': 833,
        'link': 'https://gimsap.ca/collections/all/products/jerk-seasoning-284g',
        'name': 'Jerk Seasoning 284g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p>Jerk Seasoning 284g Jerk Seasoning is a blend of ground allspice, brown sugar, dried onion, ginger, garlic, thyme, Scotch bonnet pepper, salt, black pepper, cinnamon, nutmeg, cayenne pepper, and white pepper. It is the perfect accompaniment to any dish, whether it be a chicken breast or a side of rice.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a23d86fd-07a2-4ad9-a107-956c0bcb3cdb_300x300.jpg?v=1645134226'
    },
    {
        'id': 834,
        'link': 'https://gimsap.ca/collections/all/products/jollof-rice-seasoning-70g',
        'name': 'Jollof Rice Seasoning 70g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.69',
        'description': '<p>Jollof Rice Seasoning 70g is a seasoning mix for preparing Jollof Rice. The seasoning mix is made from a blend of various herbs and spices. The blend includes ginger, garlic, thyme, bay leaves, nutmeg, onion, black pepper, turmeric, salt, paprika, and cayenne pepper.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fd16d5c5-79d8-4714-bf68-d1321805e109_300x300.jpg?v=1645134227'
    },
    {
        'id': 835,
        'link': 'https://gimsap.ca/collections/all/products/juicy-fruity-gum',
        'name': 'Juicy fruity gum',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': '<p>This gum is perfect for anyone who loves fruity flavors. The bubbles in the gum are juicy and juicy. The gum will last a long time and the flavor will never go away.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8ec8cd73-1ca5-432d-90d4-d77f48ead60f_300x300.jpg?v=1645134228'
    },
    {
        'id': 836,
        'link': 'https://gimsap.ca/collections/all/products/jumbo-calling-card',
        'name': 'jumbo calling card',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>Calling cards are a long-standing tradition for those who travel internationally. They provide a way to stay in touch with friends and family back home. A jumbo calling card is a larger version of the traditional calling card, and can be used for international calls. A jumbo calling card can hold up to four different numbers, and can be used in the same way as a traditional calling card.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8d2c6910-795e-4a97-a88d-d3afabd3e4a9_300x300.jpg?v=1645134229'
    },
    {
        'id': 837,
        'link': 'https://gimsap.ca/collections/all/products/jumbo-maggi-cube',
        'name': 'JUMBO MAGGI CUBE',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>This is a delicious, quick, and easy way to&nbsp;spice your favorite meal.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_072121253_300x300.png?v=1652275283'
    },
    {
        'id': 838,
        'link': 'https://gimsap.ca/collections/all/products/turkey-drum-5kg-cut',
        'name': 'Jumbo Turkey Drumsticks 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $20.00',
        'description': '<p>The Turkey Drum is a cut of meat that can be cooked in a variety of ways. It is made up of the leg and thigh of the turkey, and is typically a bone-in cut. It is a healthy alternative to red meat and has less saturated fat than most other poultry options. The Turkey Drum is an excellent source of protein, vitamin B6, vitamin B12, selenium, phosphorus, zinc, and niacin.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_52e2ad8a-73b2-4708-bcc0-4b281e77ec2a_300x300.jpg?v=1645138018'
    },
    {
        'id': 839,
        'link': 'https://gimsap.ca/collections/all/products/turkey-wings-5kg-uncut-superior',
        'name': 'Jumbo Turkey Wings 5kg',
        'price': 'From $26.00',
        'description': '<p>The turkey wings are about the size of a small human arm. These wings are cut and not cut, so they are still whole, but you have the option to cut them as you see fit. The turkey wings are covered in a tasty and thick layer of a delicious marinade that is sure to leave your mouth watering. These wings are perfect for a barbecue or other party because they are so large and come in a 5kg package.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/turkey-wings_300x300.jpg?v=1647977567'
    },
    {
        'id': 840,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-hair-milk',
        'name': 'Just for Me Hair Milk',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p>If you are looking for a product that is both gentle and effective, Just for Me Hair Milk is a great choice. The product contains coconut oil, and essential oils that provide nourishment to the hair. It is made to be used on dry hair, and leaves hair looking soft and healthy. The product is safe for all hair types, and is available in three different scents: floral, citrus, and vanilla.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_072248520_300x300.png?v=1652275370'
    },
    {
        'id': 841,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-hair-milk-curl-smoother-8oz',
        'name': 'Just For Me Hair Milk Curl Smoother (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': "<p>For women with curly hair, this is the product for you. It's not just a conditioner, it's a curl smoother. Curls will look frizz-free and well-defined, while being touchable and manageable. No more flyaways and unruly hair. The milk curl smoother will leave your hair feeling like silk and smelling like heaven.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2c296eec-332d-48d0-9c13-d6e64288ac50_300x300.jpg?v=1645134232'
    },
    {
        'id': 842,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-hair-milk-sulfate-free-moist-shampoo-13-5oz',
        'name': 'Just for me Hair Milk Sulfate-free Moist. Shampoo (13.5oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Just for me Hair Milk Sulfate-free Moist. Shampoo (13.5oz) is the ultimate deep conditioner and is gentle enough for everyday use. This gentle shampoo leaves hair soft, shiny, and manageable with a clean, fresh scent. It is made with botanical extracts and ingredients to condition and moisturize hair. The shampoo is free of sulfates, which can strip hair of its natural oils and dry it out. It can be used on color-treated hair, even with frequent use.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_77d71b66-29ba-435e-a1af-f42b6330aa48_300x300.jpg?v=1645134233'
    },
    {
        'id': 843,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-naturally-gentle-texture-softener',
        'name': 'Just For Me Naturally Gentle Texture Softener',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.50',
        'description': "<p>You don't have to worry about your hair being a tangled mess when you use Just For Me Naturally Gentle Texture Softener. The softener will help detangle your hair and leave it feeling moisturized and soft. Just For Me Naturally Gentle Texture Softener will also help your hair be less frizzy and flyaway. It's available in a variety of sizes and will leave your hair feeling soft and looking healthy.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2e897a7b-4e20-47fd-9a52-33e1d32eea45_300x300.jpg?v=1645134234'
    },
    {
        'id': 844,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-no-lye-conditioning-relaxer-regular',
        'name': 'Just For Me No-Lye Conditioning Relaxer (Regular)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.50',
        'description': '<p>Just For Me No-Lye Conditioning Relaxer (Regular) is a great product for people who are looking for a no-lye, non-permanent, and gentle relaxer. It is a cream that is designed to provide excellent conditioning and smoothness. This product is especially designed for relaxed hair and will not break your hair or make it feel dry.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3bb967ed-717a-4f71-bc43-5aab118ceb81_300x300.jpg?v=1645134235'
    },
    {
        'id': 845,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-relaxer-regular',
        'name': 'Just for me Relaxer (Regular)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>Just for me Relaxer (Regular) is a permanent hair relaxer. It provides smooth, shiny, manageable hair that is less frizzy and easier to style. Just for me Relaxer (Regular) is perfect for all hair types and textures.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2ae3ad5a-6bb9-408d-a350-fb3a424bf85a_300x300.jpg?v=1645134236'
    },
    {
        'id': 846,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-relaxer-super',
        'name': 'Just For Me Relaxer (Super)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>Just For Me Relaxer (Super) is a permanent, non-permanent hair relaxer that is used to straighten hair. It comes in two different types: with or without sulfates. It has a formula that has been specially developed to suit all hair types, including hair that is naturally curly. This product is easy to use and has a low odor.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_af909213-4eda-4505-a96a-bdee3742009b_300x300.jpg?v=1645134237'
    },
    {
        'id': 847,
        'link': 'https://gimsap.ca/collections/all/products/just-for-me-texture',
        'name': 'Just For Me Texture',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p>A silky and luxurious texture cream that feels light and fresh on the skin. Our new Just For Me Texture is a silky and luxurious texture cream that feels light and fresh on the skin. The refreshing formula absorbs quickly, leaving your skin feeling moisturized, hydrated, and beautifully soft.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_86c03e30-8ac2-4f03-98ed-f5186ecc6d41_300x300.jpg?v=1645134237'
    },
    {
        'id': 848,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaf',
        'name': 'Jute Leaf',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.99',
        'description': 'Jute leaf can be used to prepare Ewedu soup. It is&nbsp;<meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7e28d574-96bf-4bd3-ae17-8c47c44adb02_300x300.jpg?v=1645134238'
    },
    {
        'id': 849,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaf-big-obehi',
        'name': 'Jute Leaf -Big (Obehi)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p><meta charset="utf-8"><span>Jute leaf can be used to prepare Ewedu soup. It is&nbsp;</span><meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_074535569_300x300.png?v=1652276738'
    },
    {
        'id': 850,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaf-box-40-x-8-oz',
        'name': 'Jute Leaf Box (40 x 8 oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $65.00',
        'description': '<p><meta charset="utf-8"><span>Jute leaf can be used to prepare Ewedu soup. It is&nbsp;</span><meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_075242436_300x300.png?v=1652277166'
    },
    {
        'id': 851,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaves-bened-22x700g-box',
        'name': 'Jute Leaves (Bened 22x700g) box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': '<p><meta charset="utf-8"><span>Jute leaf can be used to prepare Ewedu soup. It is&nbsp;</span><meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_075311796_300x300.png?v=1652277195'
    },
    {
        'id': 852,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaves-bened-700g',
        'name': 'Jute Leaves (Bened) 700g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p><meta charset="utf-8"><span>Jute leaf can be used to prepare Ewedu soup. It is&nbsp;</span><meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_075345604_300x300.png?v=1652277230'
    },
    {
        'id': 853,
        'link': 'https://gimsap.ca/collections/all/products/jute-leaves-500g',
        'name': 'Jute Leaves 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.99',
        'description': '<p><meta charset="utf-8"><span>Jute leaf can be used to prepare Ewedu soup. It is&nbsp;</span><meta charset="utf-8"><span data-mce-fragment="1">rich in immune- and bone-supporting nutrients like calcium and vitamins A and C</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a69b2750-f0f3-4b01-9a38-ea941ca84fd2_300x300.jpg?v=1645134241'
    },
    {
        'id': 854,
        'link': 'https://gimsap.ca/collections/all/products/kabiya-fufu-flour',
        'name': 'Kabiya Fufu Flour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>Kabiya Fufu Flour is a perfect solution for the person who loves to cook. This product is made from cassava, yam, and maize. It is a finely ground flour that can be used in many dishes. It is perfect for making dough, such as bread, pancakes, and pizza dough. The ingredients are gluten-free and can be made without salt. This product is perfect for anyone who wants to eat healthy, gluten-free, and/or without salt.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_075536634_300x300.png?v=1652277417'
    },
    {
        'id': 855,
        'link': 'https://gimsap.ca/collections/all/products/kafura-1-piece',
        'name': 'Kafura (1 piece)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.50',
        'description': '<p>Natural Camphor</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_075956140_300x300.png?v=1652277598'
    },
    {
        'id': 856,
        'link': 'https://gimsap.ca/collections/all/products/kafura-32-pc-box',
        'name': 'Kafura (32 pc) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $95.00',
        'description': '<p>Kafura is a Turkish delight, a delicate dessert of a type of semolina, syrup, and pistachios. These individually wrapped pieces are perfect for people on the go. They are individually wrapped in a cellophane bag, and come in a box of 32 pieces. They are an easy and tasty snack, and come in a variety of flavors.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_080332215_300x300.png?v=1652277814'
    },
    {
        'id': 857,
        'link': 'https://gimsap.ca/collections/all/products/kare-kare',
        'name': 'Kare-kare',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $33.36',
        'description': '<p>Kare-kare is a Filipino dish that is traditionally made with oxtail, tripe, beef, and vegetables cooked in a rich peanut sauce. The Kare-kare is a traditional Filipino dish that has been passed down from generation to generation.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_080449933_300x300.png?v=1652277892'
    },
    {
        'id': 858,
        'link': 'https://gimsap.ca/collections/all/products/kilishi-vivian',
        'name': 'Kilishi (Vivian)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Kingfish is a delicious fish, but not many people know about it. They are a close relative to tuna and swordfish, but with a distinctive taste. They are an excellent choice for those who want to explore seafood without breaking the bank. The Kingfish steak is perfect for those who love to grill or fry. The package contains five pounds of steak that is sold by the pound.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ffd82b3d-ccd0-4e3b-a8a7-9db675cb0567_300x300.jpg?v=1645134251'
    },
    {
        'id': 859,
        'link': 'https://gimsap.ca/collections/all/products/kingfish-steak-spanish-mackerel-5lb-box',
        'name': 'Kingfish steak (spanish Mackerel) 5lb box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $38.00',
        'description': '<p>Kingfish is a delicious fish, but not many people know about it. They are a close relative to tuna and swordfish, but with a distinctive taste. They are an excellent choice for those who want to explore seafood without breaking the bank. The Kingfish steak is perfect for those who love to grill or fry. The package contains five pounds of steak that is sold by the pound.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_080854569_300x300.png?v=1652278137'
    },
    {
        'id': 860,
        'link': 'https://gimsap.ca/collections/all/products/kingfish-steak-per-lb',
        'name': 'Kingfish steak per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Kingfish is a type of fish that is found in the Atlantic Ocean. This fish is rich in Omega-3 fatty acids, which are known to help lower blood pressure and cholesterol. Kingfish is typically caught in the Gulf of Mexico and Atlantic Ocean. The most common way to cook this fish is to grill it. It is also a good source of vitamin B12, which helps promote healthy skin and hair.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_649e8638-3f21-4cbf-8a55-5ac2e5f595ea_300x300.jpg?v=1645134252'
    },
    {
        'id': 861,
        'link': 'https://gimsap.ca/collections/all/products/kinkeliba-leaves-bened-25x300g-box',
        'name': 'Kinkeliba Leaves (Bened 25x300g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $137.00',
        'description': '<p>Kinkeliba Leaves are an extract from the kinkeliba plant, a wild tree found in parts of the Congo and the Ivory Coast. The leaves are dried and ground into a powder, then packaged in a box of 25 packs of 300g each. This product is a rich source of antioxidants, flavonoids, and other nutrients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8bd65e5b-ee97-431e-af0c-52df6c76ab5d_300x300.jpg?v=1645134254'
    },
    {
        'id': 862,
        'link': 'https://gimsap.ca/collections/all/products/kinkeliba-leaves-bened-300g',
        'name': 'Kinkeliba Leaves (Bened) 300g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>A natural, soothing tea that can be used to soothe an upset stomach. Kinkeliba leaves are a type of plant that is native to the African continent. The leaves are often used in cooking, but they also have a long history of being used as a soothing tea. It is typically consumed as a herbal tea, and can be brewed as a hot or cold drink.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b2d460d5-7ca7-4ac4-a25d-c2e25c75e6ab_300x300.jpg?v=1645134255'
    },
    {
        'id': 863,
        'link': 'https://gimsap.ca/collections/all/products/kitchen-glory-per-10-pieces',
        'name': 'Kitchen Glory (per 10 pieces)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Flavour your favourite meal.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_081157416_300x300.png?v=1652278321'
    },
    {
        'id': 864,
        'link': 'https://gimsap.ca/collections/all/products/kitchen-glory-per-single-peice',
        'name': 'Kitchen Glory (per single peice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.65',
        'description': '<p>Flavour your favourite meal.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_081144879_300x300.png?v=1652278308'
    },
    {
        'id': 865,
        'link': 'https://gimsap.ca/collections/all/products/klin-detergent-190g',
        'name': 'Klin Detergent 190g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p>Klin Detergent 190g is a highly effective and efficient detergent that removes stubborn stains and odors from clothes.&nbsp; Klin Detergent 190g is also hypoallergenic, pH balanced, and biodegradable.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cf629939-57bd-482b-b003-14bf6faac20d_300x300.jpg?v=1645134258'
    },
    {
        'id': 866,
        'link': 'https://gimsap.ca/collections/all/products/knorr',
        'name': 'knorr',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.99',
        'description': "<p>Knorr is a brand of sauces, seasonings, and soups. They have a wide variety of products that all have their own unique flavor. Their original sauce is made with only the finest ingredients, and it's a great addition to any dish. Knorr sauces are made to be used in many different types of dishes, and they are all very tasty.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e43b1693-6d7e-44e8-9ee4-cf6f0075912a_300x300.jpg?v=1645134259'
    },
    {
        'id': 867,
        'link': 'https://gimsap.ca/collections/all/products/knorr-beef',
        'name': 'Knorr Beef',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>The dish is not just a good thing to make, it is a good thing to eat. The beef has the perfect balance of salt and pepper. The vegetables give the dish a nice pop of color and crunch. The dish is also healthy and can be made in just a few minutes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3f00a75e-bbcd-4aff-864c-523f96e8ef86_300x300.jpg?v=1645134260'
    },
    {
        'id': 868,
        'link': 'https://gimsap.ca/collections/all/products/knorr-beef-repack-20-pack',
        'name': 'Knorr Beef  (Repack) 20/pack',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': "<p>A family favorite, Knorr Beef has been a staple in many homes for decades. Our easy-to-prepare, seasoned beef cubes are made with tender, all-natural beef, and have no artificial flavors or preservatives. They're the perfect addition to any meal and are great for tacos, stews, and more.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1718a34e-d493-44c1-886c-adebb3c8b445_300x300.jpg?v=1645134263'
    },
    {
        'id': 869,
        'link': 'https://gimsap.ca/collections/all/products/knorr-beef-half-pack',
        'name': 'Knorr Beef (half pack)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>This Knorr Beef (half pack) contains a flavorful mix of spices and fresh vegetables to make a quick and easy meal. It is an easy to prepare meal that is perfect for busy families. It is rich in protein and a healthy source of iron. This product can be used as a topping for a number of dishes such as pasta, potatoes, rice, and vegetables.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b3a42558-c3ad-49bc-92c8-a1e85367779f_300x300.jpg?v=1645134262'
    },
    {
        'id': 870,
        'link': 'https://gimsap.ca/collections/all/products/knorr-beef-box-16',
        'name': 'Knorr Beef Box (16)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $180.00',
        'description': '<p>Knorr Beef Box is a convenient way to prepare a complete dinner with the least amount of effort. Each box includes a fully cooked beef roast, onions, potatoes, carrots, mushrooms, and seasonings. Just pop the ingredients in the oven and dinner is ready in 45 minutes. Knorr Beef Boxes are great for a family dinner or when you are hosting a dinner party.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_de65b0ab-67e4-479e-bede-dfd51686db4e_300x300.jpg?v=1645134261'
    },
    {
        'id': 871,
        'link': 'https://gimsap.ca/collections/all/products/knorr-chicken',
        'name': 'Knorr Chicken',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.50',
        'description': '<p>Knorr Chicken is a flavorful, convenient and healthy meal that provides balanced nutrition for the whole family. It is made with whole, natural ingredients and is made with no artificial flavors, colors or preservatives. It is quick and easy to prepare in the microwave, and can be made in minutes. Knorr Chicken is a flavorful, convenient and healthy meal that provides balanced nutrition for the whole family.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e1d89e96-ad42-4ed0-8340-15eb8054d00e_300x300.jpg?v=1645134264'
    },
    {
        'id': 872,
        'link': 'https://gimsap.ca/collections/all/products/knorr-chicken-box-17',
        'name': 'Knorr Chicken Box (17)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $200.00',
        'description': '<p><meta charset="utf-8"><span>Knorr Chicken is a flavorful, convenient and healthy meal that provides balanced nutrition for the whole family. It is made with whole, natural ingredients and is made with no artificial flavors, colors or preservatives. It is quick and easy to prepare in the microwave, and can be made in minutes. Knorr Chicken is a flavorful, convenient and healthy meal that provides balanced nutrition for the whole family.&nbsp;</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_081456022_300x300.png?v=1652278498'
    },
    {
        'id': 873,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-chicken-6x1-14kg',
        'name': 'Knorr Chicken Powder 1.14kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.99',
        'description': '<p>Knorr is a brand of soup mixes, seasonings, and convenience foods. They are most well-known for their dried soup mixes. These packets of dry ingredients make it easy to cook delicious, home-cooked meals. Knorr has been in business since 1887. Knorr Chicken is a dried soup mix that makes it easy to create a home-cooked meal. The chicken flavor is made with a creamy soup base and enriched with protein and vitamins. The product is made with high-quality ingredients, which makes it easy to create a delicious meal. The product is free from artificial colors, flavors, and preservatives. This product can be served with a variety of side dishes. The ingredients in this product are: dehydrated potatoes, dried onion, powdered chicken, powdered carrot, powdered celery, dried parsley, salt, sugar, dried chives, and natural flavors. Knorr Chicken is a convenient and flavorful soup mix that can be served with a variety of side dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/71j5H61VohL._AC_SX425_300x300.jpg?v=1647373659'
    },
    {
        'id': 874,
        'link': 'https://gimsap.ca/collections/all/products/knorr-chicken-powder-6x900g-2-2lb',
        'name': 'Knorr Chicken Powder 6x900g (2.2lb)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Knorr Chicken Powder is a must-have for any kitchen. It’s perfect for creating a flavorful dish in minutes. The powder can be added to any dish that needs a boost of flavor. This is a great product for busy people who don’t have time to cook from scratch. It’s also perfect for making quick, nutritious dishes for kids. The package contains six 900g bags of powder, which is enough to make six different dishes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_091232459_300x300.png?v=1652281957'
    },
    {
        'id': 875,
        'link': 'https://gimsap.ca/collections/all/products/knorr-chicken-repack-20-pack',
        'name': 'Knorr Chicken Repack (20/pack)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p>Knorr Chicken Repack is a 20-pack of individual servings of chicken soup. It is a convenient, easy-to-make, and easy-to-eat product. The soup is full of flavor and perfect for lunch or dinner.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_99e3d956-2b42-491c-8737-8dd008a732bf_300x300.jpg?v=1645134266'
    },
    {
        'id': 876,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-usa-1-14kg',
        'name': 'Knorr Powder (USA) 1.14kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.50',
        'description': '<p>Knorr Powder mix is a delicious and easy way to make a satisfying side dish.&nbsp;It is the perfect solution for the time-strapped home cook who needs a side dish in a hurry.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e0cff19a-ebc8-4f86-b8af-29cc6b29701d_300x300.jpg?v=1645134272'
    },
    {
        'id': 877,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-1kg-broth-mix',
        'name': 'Knorr Powder 1kg Broth Mix',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Knorr is a brand that specializes in convenience foods and soup mixes. They have a range of different soup mixes, including chicken, beef, mushroom, and celery. One of their more popular soup mixes is their chicken soup mix. It is a powdered soup mix that comes in a 1kg package. It is made with vegetable and chicken stock, and has vegetables such as onions, carrots, celery, and parsley. This soup mix is an easy way to make a hearty chicken soup at home.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0c012357-71f8-4553-8110-d131c65fe73c_300x300.jpg?v=1645134267'
    },
    {
        'id': 878,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-225g',
        'name': 'Knorr Powder 225g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': "<p>Knorr Powder 225g is a long-lasting, savory sauce that is perfect for enhancing any dish. Knorr Powder 225g is the perfect addition to a home chef's kitchen. It is a shelf-stable product that is easy to use and easy to store. Knorr Powder 225g is perfect for adding flavor to any dish. It can be used as a base for soups, stews, and sauces, or it can be added to meat, vegetables, and rice dishes.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6433903e-5730-4ccf-a37a-56508a169967_300x300.jpg?v=1645134268'
    },
    {
        'id': 879,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-450g',
        'name': 'Knorr Powder 450g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>With a flavor as diverse as the world, Knorr has a variety of products to make every meal a culinary experience. Knorr powder is one of the many products in the Knorr line. With 450g of product, this is enough to make 10 cups of cooked rice. The Knorr powder provides a great tasting rice, perfect for any meal. With a variety of flavors, such as Thai, Tomato and Basil, there is a flavor for every occasion. Knorr powder is an easy way to make a great tasting rice for any meal.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_688e5756-b4cf-4f10-8cc0-1c9d48cdb68e_300x300.jpg?v=1645134269'
    },
    {
        'id': 880,
        'link': 'https://gimsap.ca/collections/all/products/knorr-powder-beef-1kg',
        'name': 'Knorr Powder Beef 1kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.99',
        'description': '<p>Knorr Powder Beef is a freeze-dried beef product that is made to be an easy and convenient way to add a delicious beef flavor to any dish. The package contains 1kg of powder and will last up to 2 years in the pantry. To use, simply add 2 tablespoons of the powder to a pot with 1 liter of water, mix well, and simmer for 10 minutes.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ec9a7a8f-c4d6-41a0-8d9d-b5f7587b8d4a_300x300.jpg?v=1645134270'
    },
    {
        'id': 881,
        'link': 'https://gimsap.ca/collections/all/products/copy-of-knorr-seasoning-cubes-chicken',
        'name': 'Knorr Seasoning Cubes - Chicken',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.50',
        'description': '<p>Special blend of spices, combined into a cube. Ideal as a soup base and for a variety of other dishes.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/KNORRCHICKENCUBES_1200x1200_6eb16e59-92ed-426e-ac31-390c15c4939b_300x300.jpg?v=1606142280'
    },
    {
        'id': 882,
        'link': 'https://gimsap.ca/collections/all/products/knorr-seasoning-cubes-classic',
        'name': 'Knorr Seasoning Cubes - Classic',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': '<p>Special blend of spices, combined into a cube. Ideal as a soup base and for a variety of other dishes.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-39_300x300.png?v=1606142174'
    },
    {
        'id': 883,
        'link': 'https://gimsap.ca/collections/all/products/knorr-sinigang-mix',
        'name': 'Knorr sinigang mix',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $130.00',
        'description': "<p>Knorr sinigang mix is a Filipino dish with a mixture of vegetables, meat, and seafood. This dish is a traditional recipe that's been around for generations. Now, it's easier than ever to enjoy this dish with Knorr sinigang mix.&nbsp;</p>\n<p>&nbsp;</p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ab2bb85b-9883-46b4-9c79-0224f9cb9ca7_300x300.jpg?v=1645134274'
    },
    {
        'id': 884,
        'link': 'https://gimsap.ca/collections/all/products/knorr-tomato-bouillon-900-g',
        'name': 'Knorr Tomato Bouillon (900 g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.99',
        'description': '<p>Knorr Tomato Bouillon is a low-sodium soup base that has been made with real tomatoes, onions, and celery. It is a rich, savory soup that is perfect for hearty soups, chowders, or casseroles. It is also the perfect ingredient for rich, savory sauces and gravies.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bb31eaa0-ac38-4512-b477-cb64bf886f0d_300x300.jpg?v=1645134277'
    },
    {
        'id': 885,
        'link': 'https://gimsap.ca/collections/all/products/knorr-tomato-bouillon-1kg',
        'name': 'Knorr Tomato Bouillon 1Kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $18.99',
        'description': '<p>Knorr Tomato Bouillon is a tomato-flavored bouillon. They are sold in packages of one kilogram. Knorr Tomato Bouillon is a convenient way to flavor your food. They are also gluten-free and have no MSG. Knorr Tomato Bouillon is an excellent source of potassium, sodium, and vitamin C.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_154b7271-e157-40fb-af2e-934dc88d8deb_300x300.jpg?v=1645134275'
    },
    {
        'id': 886,
        'link': 'https://gimsap.ca/collections/all/products/knorr-tomato-bouillon-450g',
        'name': 'Knorr Tomato Bouillon 450g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': "<p>Soup is a favorite food for many people and with Knorr Tomato Bouillon, you can enjoy it any time of the year. The bouillon is made with natural tomato extract and a hint of spice. It's a perfect way to enjoy the comfort of soup on a cold winter day. You can also use the bouillon to make an easy, delicious pasta sauce. Simply cook some ground beef or ground turkey, add in some Knorr Tomato Bouillon, and top with your favorite pasta and cheese. It's a quick and easy way to enjoy the flavors of soup without all the work.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d4960b09-2926-4cf6-99c3-ca0eabd5fc33_300x300.jpg?v=1645134276'
    },
    {
        'id': 887,
        'link': 'https://gimsap.ca/collections/all/products/knorr-tomatoe-bouillon-225g',
        'name': 'Knorr Tomatoe Bouillon (225g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Knorr Tomatoe Bouillon is a sauce that is rich in flavor and perfect for any dish. It can be used in soups, sauces, and stews, and is also a great way to add a little bit of zest to your dish. The tomato bouillon has a deep and intense flavor, which makes it the perfect addition to any dish. It also has a savory and slightly sweet taste, making it a perfect complement to any dish.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0b140605-1a02-4a32-9159-b5542e3f8ec6_300x300.jpg?v=1645134278'
    },
    {
        'id': 888,
        'link': 'https://gimsap.ca/collections/all/products/koko-rubber-band',
        'name': 'Koko Rubber band',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.99',
        'description': '<p>Elastic rubber band</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2add0a15-c326-46ae-88e4-978276f4eb09_300x300.jpg?v=1645134283'
    },
    {
        'id': 889,
        'link': 'https://gimsap.ca/collections/all/products/kokonte',
        'name': 'kokonte',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>Kokonte Cassava Flour is a low-carbohydrate, gluten-free, non-GMO, organic, and raw flour. Kokonte Cassava Flour is made from dried and ground cassava root, which is then dehydrated to preserve its natural goodness. This flour is a great option for those with gluten sensitivities, or for those who are on a low-carb diet.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_092434440_300x300.png?v=1652282697'
    },
    {
        'id': 890,
        'link': 'https://gimsap.ca/collections/all/products/kokonte-1kg-delice',
        'name': 'Kokonte 1Kg (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Kokonte Cassava Flour is a low-carbohydrate, gluten-free, non-GMO, organic, and raw flour. Kokonte Cassava Flour is made from dried and ground cassava root, which is then dehydrated to preserve its natural goodness. This flour is a great option for those with gluten sensitivities, or for those who are on a low-carb diet.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8ed67a31-9ef5-490c-8f2e-233518953b32_300x300.jpg?v=1645134279'
    },
    {
        'id': 891,
        'link': 'https://gimsap.ca/collections/all/products/kokonte-cassava-flour-1kgx10',
        'name': 'Kokonte Cassava Flour 1kgx10',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Kokonte Cassava Flour is a low-carbohydrate, gluten-free, non-GMO, organic, and raw flour. Kokonte Cassava Flour is made from dried and ground cassava root, which is then dehydrated to preserve its natural goodness. This flour is a great option for those with gluten sensitivities, or for those who are on a low-carb diet.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0a1f3228-7763-41aa-8b06-a3120e950c78_300x300.jpg?v=1645134280'
    },
    {
        'id': 892,
        'link': 'https://gimsap.ca/collections/all/products/kokonte-cassava-flour-3kgx5',
        'name': 'Kokonte Cassava Flour 3kgx5',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Kokonte Cassava Flour is a low-carbohydrate, gluten-free, non-GMO, organic, and raw flour. Kokonte Cassava Flour is made from dried and ground cassava root, which is then dehydrated to preserve its natural goodness. This flour is a great option for those with gluten sensitivities, or for those who are on a low-carb diet.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_092958933_300x300.png?v=1652283010'
    },
    {
        'id': 893,
        'link': 'https://gimsap.ca/collections/all/products/kola-nut-lb-obi-gbanja',
        'name': 'Kola Nut /lb Obi Gbanja',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Colanut Obi is a pack of dried kolanuts, native to West Africa. Kolanuts are used in the preparation of traditional dishes, drinks, and confections.</span><br>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/image_2022-05-11_093407808_300x300.png?v=1652283252'
    },
    {
        'id': 894,
        'link': 'https://gimsap.ca/collections/all/products/kolanut-1-3-lb-pack-colanut-obi',
        'name': 'Kolanut (1.3 lb pack) (Colanut Obi)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Colanut Obi is a pack of dried kolanuts, native to West Africa. Kolanuts are used in the preparation of traditional dishes, drinks, and confections.&nbsp;</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c3cea2b7-95d4-42dd-bc58-768da38b025a_300x300.jpg?v=1645134284'
    },
    {
        'id': 895,
        'link': 'https://gimsap.ca/collections/all/products/kolanut-lb-obi-colanut',
        'name': 'Kolanut /lb Obi Colanut',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p><meta charset="utf-8"><span>Colanut Obi is a pack of dried kolanuts, native to West Africa. Kolanuts are used in the preparation of traditional dishes, drinks, and confections.</span></p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_90ab1625-40e7-4788-b3fc-1e833b4e1eb5_300x300.jpg?v=1645134285'
    },
    {
        'id': 896,
        'link': 'https://gimsap.ca/collections/all/products/konkonte-flour',
        'name': 'KonKonte Flour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<meta charset="utf-8"><span data-mce-fragment="1">Kokonte Cassava Flour is a low-carbohydrate, gluten-free, non-GMO, organic, and raw flour. Kokonte Cassava Flour is made from dried and ground cassava root, which is then dehydrated to preserve its natural goodness. This flour is a great option for those with gluten sensitivities, or for those who are on a low-carb diet.&nbsp;</span>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_09cf7829-b1c9-4b8b-ba11-cbdceffea275_300x300.jpg?v=1645134287'
    },
    {
        'id': 897,
        'link': 'https://gimsap.ca/collections/all/products/kopiko-coffee-candy-150g-50pcs',
        'name': 'Kopiko Coffee Candy 150g (50pcs)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Kopiko Coffee Candy is a new, refreshingly sweet coffee candy. Kopiko Coffee Candy is made with coffee extract and sugar, with a coffee flavor that is not too strong, not too sweet, and a chewy texture. This candy is perfect for coffee lovers who want a sweet treat without all the calories.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_85320c6e-c3e6-4580-9495-8d25ac6b56e8_300x300.jpg?v=1645134288'
    },
    {
        'id': 898,
        'link': 'https://gimsap.ca/collections/all/products/kotoko-fufu-14lbs',
        'name': 'kotoko fufu 14lbs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $32.00',
        'description': '<p>This is a 2-pound bag of fufu. It is made from the finest yams and water, so it is gluten-free and can be cooked in minutes. The fufu can be used to make a delicious and hearty meal.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9b93b8ea-f9f5-4204-9251-18318b7cffd6_300x300.jpg?v=1645134289'
    },
    {
        'id': 899,
        'link': 'https://gimsap.ca/collections/all/products/kotoko-fufuf-7lb',
        'name': 'Kotoko Fufuf 7lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $21.00',
        'description': "<p>Squeeze Play Kotoko Fufuf 7lb. Squeeze Play is a durable, easy to use, and fun way to play fetch with your dog. The perfect toy for dogs of all sizes, Kotoko Fufuf 7lb. Squeeze Play is a foam toy that can be compressed and released for hours of fun. Your dog will love playing with Kotoko Fufuf 7lb. Squeeze Play, and you'll love watching them play!</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0059fbab-8d2b-4173-9793-7bc236d6d1f3_300x300.jpg?v=1645134290'
    },
    {
        'id': 900,
        'link': 'https://gimsap.ca/collections/all/products/kotoko-oil-4l',
        'name': 'Kotoko Oil 4L',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': "<p>A clear, light-weight, odorless oil that is great for deep frying and cooking. The Kotoko Oil 4L is a great product for those who are in need of a new oil to fry their food with. The Kotoko Oil 4L is odorless and clear, so you can see what you are cooking. It is also a light-weight oil, so it is easy to use and doesn't feel heavy.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a7918812-156c-4a5f-a01b-96f5ed82a328_300x300.jpg?v=1645134291'
    },
    {
        'id': 901,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-bistak',
        'name': 'Kulikuli (Bistak)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>The Bistak is a small bowl that is traditionally used in a Turkish dish called Külbastı. The dish is a kind of roast lamb, where the meat is cooked with onions, spices, tomatoes, and eggplant. The Bistak is used to cook the meat and mix it with the other ingredients.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_87f95023-39c1-42eb-8a28-d9d2f8f26338_300x300.jpg?v=1645134296'
    },
    {
        'id': 902,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-bucket-22-lb',
        'name': 'Kulikuli (Bucket) 22 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $220.00',
        'description': "<p>Capacity It's time to get organized! Our Kulikuli Bucket is perfect for all your organization needs. Keep all your items in one place and get a handle on the clutter. It has a 22 lb. capacity and is made of durable, recyclable plastic.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_15ea7b99-549d-483c-b509-743b957c00da_300x300.jpg?v=1645134297'
    },
    {
        'id': 903,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-kimie-kimie-lb',
        'name': 'Kulikuli (Kimie Kimie) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>Kulikuli is a delicious and natural Hawaiian snack made from a sweet bread crust, filled with butter, coconut, and either walnuts or macadamia nuts. Kulikuli is baked to perfection in an oven and served in a gift box. Kulikuli is a delicious and natural Hawaiian snack made from a sweet bread crust, filled with butter, coconut, and either walnuts or macadamia nuts. The bread is baked to perfection in an oven and served in a gift box.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4705aca3-5bc3-4de0-b208-1088208dbb2c_300x300.jpg?v=1645134298'
    },
    {
        'id': 904,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-kimie-kimie-bottle-0-53kg',
        'name': 'Kulikuli (Kimie Kimie) Bottle 0.53kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p>The Kulikuli (Kimie Kimie) Bottle is a 5-inch bottle that contains 0.53kg of water. The bottle is designed to be lightweight and easy to carry, making it a great companion for any occasion. The bottle features a simple design with a flip-top lid and carrying handle, making it easy to transport and store. The Kulikuli (Kimie Kimie) Bottle is made from BPA-free plastic, making it safe for children to use.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/168315804_216068903641264_3659574424456411558_n_de9d8f82-ae01-43cf-9f72-b6f67534c990_300x300.jpg?v=1644953801'
    },
    {
        'id': 905,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-vivian',
        'name': 'Kulikuli (Vivian)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Kulikuli is a great way to get your kids away from their screens and exercise while they have fun. The game is designed for kids 3-10 years old, and can be played with 2-4 players. The game consists of three plastic rings, a bat, and a small rubber ball. The player who is it throws the ball and tries to hit the rings. The other players try to dodge the ball. If they get hit, they have to go back to the starting line. If they make it back to the starting line without getting hit, they can tag someone else. If they get tagged, they have to go back to the starting line. The first player to make it back to the starting line three times wins.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9be4d9ff-1150-4838-b7c2-75274472179f_300x300.jpg?v=1645134299'
    },
    {
        'id': 906,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-20kg-sack',
        'name': 'KuliKuli 20kg Sack',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': "<p>The KuliKuli 20kg Sack is a very light and compact way to keep food fresh. It is made of a 100% natural and biodegradable bag made from the pulp of the kenaf plant. This bag is made of a thin material that is porous enough to allow air to flow through. This means that the food will stay fresh and won't have any bad odors. The KuliKuli 20kg Sack is great for camping, hiking, and other outdoor activities.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_685e6e33-c488-465d-b01f-115592db1de5_300x300.jpg?v=1645134292'
    },
    {
        'id': 907,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-20kg-sack-less-spicy',
        'name': 'KuliKuli 20kg Sack Less Spicy',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>KuliKuli is a new organic product that offers healthy and organic chips made from banana and cassava root. The company has two products that offer different flavors. The 20kg Sack Less Spicy is a spicier flavor and includes an organic chili seasoning. KuliKuli is the first product of its kind that uses the root of the cassava plant as the main ingredient. The cassava root is a starchy and gluten-free vegetable that has a high content of protein and iron. The root is a versatile ingredient that can be eaten raw, roasted, boiled, or mashed. It can also be fermented to make a sweet beverage or distilled to make a clear alcohol. KuliKuli chips are healthy, delicious, and are GMO-free.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5e15db52-9f24-4eb4-ba08-596b281eaad4_300x300.jpg?v=1645134293'
    },
    {
        'id': 908,
        'link': 'https://gimsap.ca/collections/all/products/kulikuli-250gx16-delice',
        'name': 'Kulikuli 250gx16 (Delice)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Kulikuli is a chocolate-coated wafer. Kulikuli is the perfect balance of the crispiness of a wafer and the sweetness of chocolate. Kulikuli is the ideal snack to have with a cup of coffee or to satisfy your sweet tooth.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_44da6df0-b000-494b-9f7f-05219d2bcfdc_300x300.jpg?v=1645134294'
    },
    {
        'id': 909,
        'link': 'https://gimsap.ca/collections/all/products/kuza-100-indian-hemp-hair-scalp-18oz',
        'name': 'KUZA 100% Indian Hemp Hair &amp; Scalp (18oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $16.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1eb64e08-70c3-4eaf-bda3-226ca46a5209_300x300.jpg?v=1645134300'
    },
    {
        'id': 910,
        'link': 'https://gimsap.ca/collections/all/products/kuza-100-indian-hemp-hair-scalp-8oz',
        'name': 'KUZA 100% Indian Hemp Hair &amp; Scalp (8oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_35e2cfd6-81da-49ad-9de9-fe944f3276ed_300x300.jpg?v=1645134301'
    },
    {
        'id': 911,
        'link': 'https://gimsap.ca/collections/all/products/kuza-coconut-oil-hair-cream-113g',
        'name': 'Kuza Coconut oil Hair Cream 113g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_92c557ea-f888-4490-83ba-4c491995e8df_300x300.jpg?v=1645134302'
    },
    {
        'id': 912,
        'link': 'https://gimsap.ca/collections/all/products/kuza-hair-food',
        'name': 'Kuza Hair Food',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0e0e36c3-fa86-41e9-802d-7e49e83a565d_300x300.jpg?v=1645134303'
    },
    {
        'id': 913,
        'link': 'https://gimsap.ca/collections/all/products/kuza-hair-food-133g',
        'name': 'Kuza Hair Food 133g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3183a09a-c5cb-4cfb-8fda-e3fea37d32b5_300x300.jpg?v=1645134304'
    },
    {
        'id': 914,
        'link': 'https://gimsap.ca/collections/all/products/kuza-indian-hemp-hair-cream',
        'name': 'Kuza Indian Hemp Hair Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4078117f-2aee-459f-8092-5db0bee23684_300x300.jpg?v=1645134305'
    },
    {
        'id': 915,
        'link': 'https://gimsap.ca/collections/all/products/kuza-indian-hemp-hair-cream-113g',
        'name': 'Kuza Indian Hemp Hair Cream 113g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_120113a7-2015-41ca-bb66-da0cdcda99b6_300x300.jpg?v=1645134306'
    },
    {
        'id': 916,
        'link': 'https://gimsap.ca/collections/all/products/kwanga-cassava-bread',
        'name': 'Kwanga (Cassava Bread)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5b10d986-6cde-4109-9cf0-e5b0d947189c_300x300.jpg?v=1645134307'
    },
    {
        'id': 917,
        'link': 'https://gimsap.ca/collections/all/products/la-bamakoise-tamarin-125-ml',
        'name': 'La Bamakoise Tamarin 125 mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $11.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d27ebef6-0653-4a26-90ab-9ec017e6ae50_300x300.jpg?v=1645134308'
    },
    {
        'id': 918,
        'link': 'https://gimsap.ca/collections/all/products/la-casera-apple-drink',
        'name': 'la casera apple drink',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.50',
        'description': '<p>la casera apple drink is a non-alcoholic drink made from fresh apples and other natural ingredients. la casera apple drink is made with 100% apple juice, apple pectin, citric acid, and ascorbic acid. It has a light and refreshing taste that is perfect for those looking for a healthier alternative to soda. The refreshing taste is the perfect balance of sweet and tart and is great on its own or mixed with your favorite spirit.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8befd707-4074-4847-8932-9e447ba97738_300x300.jpg?v=1645134310'
    },
    {
        'id': 919,
        'link': 'https://gimsap.ca/collections/all/products/lady-b-custard-24x500g-box',
        'name': 'Lady B Custard 24x500g Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $95.00',
        'description': '<p>Lady B Custard is a premium custard dessert, made with a blend of eggs, sugar, and cream. It is served cold and makes a great snack for children and adults alike. This custard dessert is made with a blend of eggs, sugar, and cream. It is served cold and makes a great snack for children and adults alike. The custard is made with a proprietary blend of eggs, sugar, and cream. This custard dessert is made in small batches, hand-filled into custard cups, and then packaged. Lady B Custard is available in both a large size (24x500g) and a small size (6x500g).</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cafb4cb4-ea0a-47fb-8d4e-36b66c303398_300x300.jpg?v=1645134311'
    },
    {
        'id': 920,
        'link': 'https://gimsap.ca/collections/all/products/lady-b-custard-2kg',
        'name': 'Lady B Custard 2kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $17.50',
        'description': '<p>Lady B Custard is a rich and decadent dessert for all of your dinner parties. Made with only the finest ingredients, this custard will make any dinner a delight. This is the perfect dish for a dinner party, so get yours today!</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f09792ad-7efd-4a7f-9a86-38d9506483d5_300x300.jpg?v=1645134312'
    },
    {
        'id': 921,
        'link': 'https://gimsap.ca/collections/all/products/lady-b-custard-2kg-box',
        'name': 'Lady B Custard 2kg (Box)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p>Lady B Custard is a fluffy, creamy custard dessert that can be served cold or hot. Made with eggs, milk, sugar, and flour, this custard is a decadent treat. Lady B Custard is a delicious dessert that can be served hot or cold. This custard is made with eggs, milk, sugar, and flour. Served cold, this custard is a light and fluffy dessert that can be enjoyed by the whole family. Served hot, this custard is a decadent dessert that is sure to satisfy your sweet tooth.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_337179f0-eb8c-4265-895d-1f847bc445b7_300x300.jpg?v=1645134313'
    },
    {
        'id': 922,
        'link': 'https://gimsap.ca/collections/all/products/lady-b-custard-500g',
        'name': 'Lady B Custard 500g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Lady B Custard is a rich and creamy custard that is perfect for breakfast, dessert, or anytime you want a decadent dessert. This traditional custard recipe is creamy and smooth, and made with milk, sugar, and egg yolks. There are no artificial flavors or colors in this custard, and it can be enjoyed right out of the jar or baked into a dish. Lady B Custard is a rich and creamy custard that is perfect for breakfast, dessert, or anytime you want a decadent dessert. This traditional custard recipe is creamy and smooth, and made with milk, sugar, and egg yolks. There are no artificial flavors or colors in this custard, and it can be enjoyed right out of the jar or baked into a dish.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_c4f59c70-5957-4f58-87d3-499f6d4222e0_300x300.jpg?v=1645134314'
    },
    {
        'id': 923,
        'link': 'https://gimsap.ca/collections/all/products/lamb-meat-per-lb',
        'name': 'Lamb Meat per lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Lamb meat is high in protein and low in fat. This meat is tender and flavorful. It is a delicious option for those who are looking for a healthy and hearty meal.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_cbdd8059-6b7d-46ed-a7fe-4a51f79617c9_300x300.jpg?v=1645134315'
    },
    {
        'id': 924,
        'link': 'https://gimsap.ca/collections/all/products/larsor-peppersoup-seasoning-sachet',
        'name': 'Larsor Peppersoup Seasoning  sachet',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.00',
        'description': '<p>Larsor Peppersoup Seasoning is a perfect blend of the right amount of pepper, onion, and other spices. Larsor Peppersoup Seasoning is perfect for anyone who likes to add flavor to their food. Larsor Peppersoup Seasoning is also a good way to add flavor to your eggs, mashed potatoes, soups, and even salads.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_fe703b3e-7747-4185-b4ed-51bd51825cd5_300x300.jpg?v=1645134317'
    },
    {
        'id': 925,
        'link': 'https://gimsap.ca/collections/all/products/larsor-peppersoup-seasoning-box',
        'name': 'Larsor Peppersoup Seasoning Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $170.00',
        'description': '<p>Larsor Peppersoup Seasoning Box is a collection of three sauces that are best for making pepper soup. The sauces are made from natural ingredients and do not contain any artificial flavors. The three sauces are mild, medium, and hot. The mild sauce is made from roasted peppers, tomatoes, garlic, onion, celery, and green pepper. The medium sauce is made from roasted peppers, tomatoes, garlic, onion, celery, green pepper, cumin, and cayenne pepper. The hot sauce is made from roasted peppers, tomatoes, garlic, onion, celery, green pepper, cumin, cayenne pepper, and chile de arbol.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e57b0c7d-ea42-4074-abe0-34b7e7fce653_300x300.jpg?v=1645134316'
    },
    {
        'id': 926,
        'link': 'https://gimsap.ca/collections/all/products/lavender-castor-oil',
        'name': 'Lavender Castor Oil',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.99',
        'description': '<p>Lavender Castor Oil is a product made from a blend of oils including castor oil, olive oil, and lavender essential oil. This oil can be used for hair and skin, and is especially helpful for dry skin. Lavender Castor Oil is safe for use on all skin types, including sensitive skin.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_45a1f57d-4269-4b12-b11b-87945c9bfbad_300x300.jpg?v=1645134318'
    },
    {
        'id': 927,
        'link': 'https://gimsap.ca/collections/all/products/lemonvate-cream-50g',
        'name': 'Lemonvate Cream 50g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p>Lemonvate Cream is a natural, botanical based, non-oily, non-greasy, hypoallergenic, non-comedogenic cream for use on the face, neck, and chest. Lemonvate Cream is formulated with lemongrass, lemon peel, and other natural ingredients to provide protection from the sun and to moisturize the skin. Lemonvate Cream is a unique, botanical based, non-oily, non-greasy, hypoallergenic, non-comedogenic cream for use on the face, neck, and chest. Lemonvate Cream is formulated with lemongrass, lemon peel, and other natural ingredients to provide protection from the sun and to moisturize the skin. The non-oily, non-greasy formula makes it perfect for use on oily skin types and those with sensitive skin. It is made with natural ingredients such as lemongrass, lemon peel, and other botanical extracts to provide protection from the sun and to moisturize the skin. The botanical based formula also provides a natural alternative to chemicals found in most sunscreens.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bfd86fa6-22c7-4908-af13-6dd25d8366b2_300x300.jpg?v=1645134319'
    },
    {
        'id': 928,
        'link': 'https://gimsap.ca/collections/all/products/lemonvate-gel-30g',
        'name': 'Lemonvate Gel 30g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.99',
        'description': '<p>Lemonvate Gel is a topical cream that soothes the skin and provides natural relief from the pain of a sunburn. It is a topical cream that soothes the skin and provides natural relief from the pain of a sunburn. It is made with natural ingredients that are safe for sensitive skin. This product contains no artificial fragrance, and it is vegan, gluten-free, and cruelty-free. Lemonvate Gel is a topical cream that soothes the skin and provides natural relief from the pain of a sunburn. This product contains no artificial fragrance, and it is vegan, gluten-free, and cruelty-free. It is made with natural ingredients that are safe for sensitive skin. This topical cream soothes the skin and provides natural relief from the pain of a sunburn. It is made with natural ingredients that are safe for sensitive skin.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_198a43b9-6c5c-4c09-b1b0-e602dc79e18a_300x300.jpg?v=1645134320'
    },
    {
        'id': 929,
        'link': 'https://gimsap.ca/collections/all/products/lesieur-mayonnaise-475g-x12',
        'name': 'Lesieur Mayonnaise 475g x12',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Lesieur mayonnaise is a tangy, yet smooth mayonnaise that can be used in a variety of ways. With an average of 475g per jar, it is perfect for sandwiches, salads, dips, and dressings. Lesieur mayonnaise is a tangy, yet smooth mayonnaise that can be used in a variety of ways. With an average of 475g per jar, it is perfect for sandwiches, salads, dips, and dressings. With a tangy flavor and creamy texture, Lesieur mayonnaise is made with carefully selected ingredients. Lesieur mayonnaise is perfect for all occasions, whether you are entertaining guests or need a quick meal.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9f5f14c4-d317-4918-a709-f29481eef687_300x300.jpg?v=1645134322'
    },
    {
        'id': 930,
        'link': 'https://gimsap.ca/collections/all/products/lima-beans',
        'name': 'lima beans',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>Limas are a type of green bean. They are long and thin, and can be eaten raw or cooked. They are best in a salad, but can also be used in soup, casseroles, and even desserts. Limas are an excellent source of vitamin A, vitamin C, vitamin K, and iron.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9cf5fff1-5de5-4082-9f88-aa556cfd1c2b_300x300.jpg?v=1645134323'
    },
    {
        'id': 931,
        'link': 'https://gimsap.ca/collections/all/products/lion-dried-thyme',
        'name': 'Lion  Dried Thyme',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>Lion Dried Thyme is a savory blend of organic thyme, organic oregano, organic sage, organic marjoram, organic savory, organic basil, organic parsley, organic rosemary, organic bay leaves, organic garlic, organic onion, organic black pepper, organic celery, organic cumin, organic coriander, organic cayenne pepper, and sea salt. Lion Dried Thyme is a savory blend of organic thyme, organic oregano, organic sage, organic marjoram, organic savory, organic basil, organic parsley, organic rosemary, organic bay leaves, organic garlic, organic onion, organic black pepper, organic celery, organic cumin, organic coriander, organic cayenne pepper, and sea salt. Lion Dried Thyme is a savory blend of organically grown thyme, oregano, sage, marjoram, savory, basil, parsley, rosemary, bay leaves, garlic, onion, black pepper, celery, cumin, coriander, cayenne pepper and sea salt. It is perfect for roasts and poultry dishes and can be used as a flavor enhancer in soups and stews.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7ea48823-aff2-435f-b433-d4046313d325_300x300.jpg?v=1645134325'
    },
    {
        'id': 932,
        'link': 'https://gimsap.ca/collections/all/products/lion-curry-powder-25g',
        'name': 'Lion Curry Powder 25g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p>With the unique and robust flavor of Africa, Lion Curry Powder will spice up any dish with a kick. In the classic curry dish, a few tablespoons of this spice will infuse the sauce with an exotic flavor. Try using it in an African soup, Indian dish, or a Thai recipe. Lion Curry Powder is a classic African spice that will bring a robust flavor to any dish. Made from cumin, coriander, turmeric, ginger, cayenne pepper, garlic, and other spices, this blend is a mix of different flavors that will bring any dish to life. Use it in African soups, Indian dishes, or Thai recipes for a truly exotic flavor.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6e170714-e445-4f22-9207-ba62ce12d6df_300x300.jpg?v=1645134324'
    },
    {
        'id': 933,
        'link': 'https://gimsap.ca/collections/all/products/lipton',
        'name': 'Lipton',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p>Iced tea has become a staple in many homes. Whether you are drinking it to help you wake up in the morning or to cool down in the evening, there is no denying that Lipton has a great selection of flavors. It is a trusted brand that has been around for decades. One of their most popular flavors is peach. It is made with the perfect blend of peaches and black tea. It is delicious and refreshing. You can drink it hot or cold. You can make it in the morning or enjoy it in the evening. It is a great drink for any time of day. Lipton is a trusted brand that has been around for decades. One of their most popular flavors is peach. It is made with the perfect blend of peaches and black tea. It is delicious and refreshing. You can drink it hot or cold. You can make it in the morning or enjoy it in the evening. It is a great drink for any time of day.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0ef380a8-6a36-43f4-8c41-8252fcd36353_300x300.jpg?v=1645134326'
    },
    {
        'id': 934,
        'link': 'https://gimsap.ca/collections/all/products/liquid-mouse',
        'name': 'Liquid Mouse',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.99',
        'description': "<p>Your home is your sanctuary. Whether you have pets or not, you don't want to have to deal with a mouse infestation. That's why Liquid Mouse is the perfect solution. It's the natural way to rid your home of mice. Made from all natural ingredients, Liquid Mouse is made to be non-toxic to pets and humans. It has a pleasant smell and can be used around the home without worry. All you have to do is set up a trap with a bit of Liquid Mouse and wait for the mice to come to you. Liquid Mouse is a unique product that has been shown to be effective in removing mice from homes. Made from all natural ingredients, Liquid Mouse is non-toxic to pets and humans. All you have to do is set up a trap with a bit of Liquid Mouse and wait for the mice to come to you. The smell of the product is pleasant and can be used around the home without worry.</p><p></p>",
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9a9ea3ff-8d39-4c32-be84-825e1c66293d_300x300.jpg?v=1645134327'
    },
    {
        'id': 935,
        'link': 'https://gimsap.ca/collections/all/products/liquid-peak-evaporated-milk-48x156ml',
        'name': 'Liquid Peak Evaporated Milk',
        'price': 'From $2.50',
        'description': '<p>Liquid Peak Evaporated Milk is a traditional, creamy, and rich evaporated milk. This product is gluten-free, kosher, and has no added sugar. It is available in a 380mL and 158mL can. This product is a staple in any kitchen, and it is also used in many recipes.</p>\n<p>&nbsp;</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3dc5bf3f-c430-4eff-945f-d1e1fc3f19c5_300x300.jpg?v=1645134328'
    },
    {
        'id': 936,
        'link': 'https://gimsap.ca/collections/all/products/liquid-peak-milk-48x380ml',
        'name': 'Liquid Peak Milk 48x380mL',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p>Liquid Peak Milk is a dairy product with a shelf life of 12 months. The milk is imported from the United States and it has a shelf life of 12 months. The product is available in packs of 48x380mL and has a unique formula which ensures the milk is fresh and good quality.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0b30038c-4f6a-48cc-9beb-018a48bbdd92_300x300.jpg?v=1645134329'
    },
    {
        'id': 937,
        'link': 'https://gimsap.ca/collections/all/products/liz-aloe-vera-soothing-gel-10oz',
        'name': 'Liz Aloe Vera Soothing Gel (10oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p>Liz Aloe Vera Soothing Gel is a skin care product that is perfect for those who have dry skin. This product is made from all natural ingredients and is soothing to the skin. It has been created to moisturize the skin and to promote healthy skin. The product can be used by people of all ages and it is available in a 10 ounce container.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a8ad5212-6961-4c0b-994f-0a2de659b0a2_300x300.jpg?v=1645134330'
    },
    {
        'id': 938,
        'link': 'https://gimsap.ca/collections/all/products/liz-aloe-vera-soothing-gel-16-9oz',
        'name': 'Liz Aloe Vera Soothing Gel (16.9oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.00',
        'description': '<p>Liz Aloe Vera Soothing Gel is an all-natural moisturizer made with ingredients that are safe for the skin. Aloe Vera gel is well known for its ability to help heal the skin and this gel is no exception. When applied to the skin, it soothes and cools the skin and provides a protective barrier against the elements. It can be used on sunburns, irritated skin, and more. This product is vegan, cruelty-free, and contains no synthetic fragrances or dyes. Liz Aloe Vera Soothing Gel is an all-natural moisturizer made with ingredients that are safe for the skin. Aloe Vera gel is well known for its ability to help heal the skin and this gel is no exception. When applied to the skin, it soothes and cools the skin and provides a protective barrier against the elements. It can be used on sunburns, irritated skin, and more. This product is vegan, cruelty-free, and contains no synthetic fragrances or dyes. When applied to the skin, Liz Aloe Vera Soothing Gel soothes and cools the skin and provides a protective barrier against the elements. It can be used on sunburns, irritated skin, and more. This product is vegan, cruelty-free, and contains no synthetic fragrances or dyes.</p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_dd632d79-8c7e-4c23-80fc-b2d4df6a325f_300x300.jpg?v=1645134331'
    },
    {
        'id': 939,
        'link': 'https://gimsap.ca/collections/all/products/liz-aloe-vera-soothing-gel-98-tube-4-05oz',
        'name': 'Liz Aloe Vera Soothing Gel 98% Tube (4.05oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.25',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_9d403405-e7a6-40dd-a67b-770aa206e156_300x300.jpg?v=1645134332'
    },
    {
        'id': 940,
        'link': 'https://gimsap.ca/collections/all/products/liz-professional-cocoa-black-soap-120g',
        'name': 'Liz Professional Cocoa Black Soap (120g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3609361b-5672-4c34-b4ce-beefe62b6ea2_300x300.jpg?v=1645134333'
    },
    {
        'id': 941,
        'link': 'https://gimsap.ca/collections/all/products/liz-twisted-wire-net',
        'name': 'LIZ Twisted Wire Net',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $7.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3389bfee-cadd-42dc-a800-18f11697cdcc_300x300.jpg?v=1645134334'
    },
    {
        'id': 942,
        'link': 'https://gimsap.ca/collections/all/products/local-scooper-calabash-igbako',
        'name': 'Local  Scooper (calabash Igbako)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6a917091-c295-4164-bb2c-c7da575840cb_300x300.jpg?v=1645134335'
    },
    {
        'id': 943,
        'link': 'https://gimsap.ca/collections/all/products/local-sponge-kankan-lb',
        'name': 'Local Sponge (kankan) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7387489f-ae7c-4d53-97c1-d84a18596b77_300x300.jpg?v=1645134336'
    },
    {
        'id': 944,
        'link': 'https://gimsap.ca/collections/all/products/locust-bean-iru-lb',
        'name': 'locust bean (Iru) /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d12c9d27-7d8b-49a8-9bd3-fba6bb5804f0_300x300.jpg?v=1645134339'
    },
    {
        'id': 945,
        'link': 'https://gimsap.ca/collections/all/products/locust-bean-iru-0-3-lb',
        'name': 'locust bean (Iru) 0.3 lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f690fe04-0f83-45a1-8fe4-38561b096bb8_300x300.jpg?v=1645134337'
    },
    {
        'id': 946,
        'link': 'https://gimsap.ca/collections/all/products/locust-bean-iru-11lb-bucket',
        'name': 'locust bean (Iru) 11lb bucket',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $190.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ac575fe8-a18d-47a7-ad93-fde2de146012_300x300.jpg?v=1645134338'
    },
    {
        'id': 947,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-900ml-energy',
        'name': 'Lucozade 900mL Original',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.00',
        'description': '<p>Lucozade 900mL Energy</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/LucozadeOriginal_300x300.jpg?v=1644953909'
    },
    {
        'id': 948,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-900mlx12-energy',
        'name': 'Lucozade 900mLx12 Energy',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ad29377d-8632-4e78-9514-b346a2fb629f_300x300.png?v=1645134341'
    },
    {
        'id': 949,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-900mlx12-orange',
        'name': 'Lucozade 900mLx12 Orange',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_77ea3b93-2f25-41c7-ab09-51d2694d4cfe_300x300.jpg?v=1645134342'
    },
    {
        'id': 950,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-energy-380-ml-bottle',
        'name': 'Lucozade Energy (380 ml) bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_02d8f865-28fa-4d9a-be12-b6c71dae3cac_300x300.jpg?v=1645134344'
    },
    {
        'id': 951,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-energy-380-ml-fridge-pack-4-pcs',
        'name': 'Lucozade Energy (380 ml) fridge pack 4 pcs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5e84926b-f6e2-47f3-bee4-d10534784c37_300x300.jpg?v=1645134345'
    },
    {
        'id': 952,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-energy-250ml-can',
        'name': 'Lucozade Energy 250mL Can',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b10691d4-ac85-4e40-9247-ed24d7cc6b3c_300x300.jpg?v=1645134343'
    },
    {
        'id': 953,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-orange-380-ml-bottle',
        'name': 'Lucozade Orange (380 ml) bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6f67f3e1-3c9c-4585-b242-0b75ff17b671_300x300.jpg?v=1645134346'
    },
    {
        'id': 954,
        'link': 'https://gimsap.ca/collections/all/products/lucozade-orange-380-ml-fridge-pack-4-pcs',
        'name': 'Lucozade Orange (380 ml) fridge pack 4 pcs',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $12.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3edc60f2-3660-4ee1-9208-9a3408b884c3_300x300.jpg?v=1645134347'
    },
    {
        'id': 955,
        'link': 'https://gimsap.ca/collections/all/products/ludo',
        'name': 'Ludo',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $22.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7b439d15-9a19-4806-8c22-c22539dc175d_300x300.jpg?v=1645134348'
    },
    {
        'id': 956,
        'link': 'https://gimsap.ca/collections/all/products/lusters-pink-shea-butter-coconut-oil',
        'name': "Luster''s Pink Shea Butter Coconut oil",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bd717ac0-30ad-4c0a-85af-5071d90b9e1e_300x300.jpg?v=1645134351'
    },
    {
        'id': 957,
        'link': 'https://gimsap.ca/collections/all/products/lusters-pink-no-lye-relaxer',
        'name': "Luster's Pink No Lye Relaxer",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_333eb399-08fd-4b85-b3a3-b566958aa614_300x300.jpg?v=1645134349'
    },
    {
        'id': 958,
        'link': 'https://gimsap.ca/collections/all/products/lusters-pink-oil-59ml',
        'name': "Luster's Pink Oil 59ml",
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1fdcf5da-89bb-4693-9848-1203e060504a_300x300.jpg?v=1645134350'
    },
    {
        'id': 959,
        'link': 'https://gimsap.ca/collections/all/products/macep-scent-leaves-bened-22x700g-box',
        'name': 'Macep (scent Leaves Bened 22x700g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $175.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_354714b0-6376-4989-a691-18a543d0200f_300x300.jpg?v=1645134354'
    },
    {
        'id': 960,
        'link': 'https://gimsap.ca/collections/all/products/macep-scent-leaves-bened-600g',
        'name': 'Macep (scent Leaves Bened) 600g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6df6ab4a-fe2a-403d-8e4b-5c324fc68c21_300x300.jpg?v=1645134355'
    },
    {
        'id': 961,
        'link': 'https://gimsap.ca/collections/all/products/macep-scent-leaves-24x400g-box',
        'name': 'Macep (Scent leaves) 24x400g Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $135.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_595c4169-2a14-433b-be53-55e6a7bdc644_300x300.jpg?v=1645134352'
    },
    {
        'id': 962,
        'link': 'https://gimsap.ca/collections/all/products/macep-scent-leaves-400g',
        'name': 'Macep (Scent leaves) 400g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_33170678-35b0-4778-bcd4-f05c0a2a5a8a_300x300.jpg?v=1645134353'
    },
    {
        'id': 963,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-lb',
        'name': 'Mackerel',
        'price': 'From $10.00',
        'description': '<p>&nbsp;</p>\n<p><span>Mackerel is a delicious oily fish, known for both for its iridescent skin and rich flavour. Mackerel is a nutritious fish&nbsp;with high levels of essential fatty acids, which improve endurance, aid in recovery after exercise, and help to maintain beautiful skin.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_300795b0-2fd1-41b5-9f4a-27072f016eb0_300x300.jpg?v=1645134368'
    },
    {
        'id': 964,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-titus',
        'name': 'Mackerel (Titus)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $95.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_37369050-9987-4ef7-9d0c-2d50494ad8e0_300x300.jpg?v=1645134370'
    },
    {
        'id': 965,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-10kg',
        'name': 'Mackerel 10kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $75.00',
        'description': '<p>&nbsp;</p>\n<p><span>Mackerel is a delicious oily fish, known for both for its iridescent skin and rich flavour. Mackerel is a nutritious fish&nbsp;with high levels of essential fatty acids, which improve endurance, aid in recovery after exercise, and help to maintain beautiful skin.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3b568b98-1e85-4297-aef2-ba08454b72d8_300x300.jpg?v=1645134356'
    },
    {
        'id': 966,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-20kg-norway',
        'name': 'Mackerel 20kg (Norway)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $145.00',
        'description': '<p>&nbsp;</p>\n<p><span>Mackerel is a delicious oily fish, known for both for its iridescent skin and rich flavour. Mackerel is a nutritious fish&nbsp;with high levels of essential fatty acids, which improve endurance, aid in recovery after exercise, and helps to maintain beautiful skin. Norway is know as having the best mackerel. A mackerel caught in Norwegian waters is bigger, fatter, and of higher quality than those caught in the waters of the Faroe Islands or Iceland.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Atlantic_Mackerel_2800x_dced9f64-fe32-4d1c-a61d-f32827cecc00_300x300.png?v=1648059837'
    },
    {
        'id': 967,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-24kg-icelandia',
        'name': 'Mackerel 24kg (icelandia)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $150.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_aee14194-04a2-4315-bc20-8d81f20683d5_300x300.jpg?v=1645134361'
    },
    {
        'id': 968,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-15kg',
        'name': 'Mackerel 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $110.00',
        'description': '<p>&nbsp;</p>\n<p><span>Mackerel is a delicious oily fish, known for both for its iridescent skin and rich flavour. Mackerel is a nutritious fish&nbsp;with high levels of essential fatty acids, which improve endurance, aid in recovery after exercise, and help to maintain beautiful skin.&nbsp;</span></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_aec19046-579b-425e-a2f9-c6a78db49018_300x300.jpg?v=1645134359'
    },
    {
        'id': 969,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-8kg',
        'name': 'Mackerel 8kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_8070125e-3b4c-42ed-8ca4-4807dfe2baff_300x300.png?v=1645134364'
    },
    {
        'id': 970,
        'link': 'https://gimsap.ca/collections/all/products/mackerel-cut-lb',
        'name': 'Mackerel Cut /lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6fc08914-d9d1-4109-aa8c-6d938c7ab3b7_300x300.jpg?v=1645134366'
    },
    {
        'id': 971,
        'link': 'https://gimsap.ca/collections/all/products/madurito-chips-salted-unripe-box-30-x-85g',
        'name': 'Madurito Chips Salted Unripe Box (30 x 85g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_b823f2c8-5d60-4b8b-8656-9a5255a5cacc_300x300.jpg?v=1645134372'
    },
    {
        'id': 972,
        'link': 'https://gimsap.ca/collections/all/products/maduritos-box-plantain-chips-30-x-85g',
        'name': 'Maduritos Box Plantain Chips (30 x 85g)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $60.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_557043fc-705e-4c81-b180-a4c18aa7e079_300x300.jpg?v=1645134373'
    },
    {
        'id': 973,
        'link': 'https://gimsap.ca/collections/all/products/maduritos-plantain-chips-85g',
        'name': 'Maduritos Plantain Chips 85g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.15',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_984855a6-0419-45f9-917a-d968c72226ff_300x300.jpg?v=1645134375'
    },
    {
        'id': 974,
        'link': 'https://gimsap.ca/collections/all/products/maduritos-plantanitos-chips-salted-unripe-85g',
        'name': 'Maduritos Plantanitos Chips Salted Unripe 85g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.15',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_e592be5d-ef15-44ee-a08d-eab8d22e01ce_300x300.jpg?v=1645134376'
    },
    {
        'id': 975,
        'link': 'https://gimsap.ca/collections/all/products/magadjo-corn-meal-5kg',
        'name': 'Magadjo Corn Meal 5kg',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $25.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_af8e7903-9a02-4522-b835-2f40225847e7_300x300.jpg?v=1645134377'
    },
    {
        'id': 976,
        'link': 'https://gimsap.ca/collections/all/products/maganjo-10kg-supreme-real-maize-flour',
        'name': 'Maganjo 10kg Supreme Real Maize Flour',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $38.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6154bec6-8e45-43b1-b89c-f86eeb3cbafb_300x300.jpg?v=1645134378'
    },
    {
        'id': 977,
        'link': 'https://gimsap.ca/collections/all/products/maggi-chicken-24x60x10g-box',
        'name': 'Maggi Chicken 24x60x10g Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $280.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_6577071b-3f94-4997-8f74-dbf6354f2a55_300x300.jpg?v=1645134379'
    },
    {
        'id': 978,
        'link': 'https://gimsap.ca/collections/all/products/maggi-chicken-60x10g',
        'name': 'Maggi Chicken 60x10g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $14.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a96d023e-d18d-490c-8327-0c4f953fe525_300x300.jpg?v=1645134380'
    },
    {
        'id': 979,
        'link': 'https://gimsap.ca/collections/all/products/maggi-crayfish-24x60x10g-box',
        'name': 'Maggi Crayfish (24x60x10g) Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $250.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_85f4ace8-a438-41f4-b35d-0c74b026ff26_300x300.jpg?v=1645134381'
    },
    {
        'id': 980,
        'link': 'https://gimsap.ca/collections/all/products/maggi-crayfish-packed-35lb',
        'name': 'Maggi crayfish (packed) .35lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $4.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_f264d5c5-8f11-42bb-b814-a1190c790177_300x300.jpg?v=1645134383'
    },
    {
        'id': 981,
        'link': 'https://gimsap.ca/collections/all/products/maggi-crayfish-packed-7lb',
        'name': 'Maggi crayfish (packed) .7lb',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_0b45422d-e0b2-4d95-967e-cb4c3dc7ddbd_300x300.jpg?v=1645134384'
    },
    {
        'id': 982,
        'link': 'https://gimsap.ca/collections/all/products/maggi-crayfish-600g',
        'name': 'Maggi Crayfish 600g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a1c107d6-d24c-4698-b0c6-fd93c5bccc1c_300x300.jpg?v=1645134382'
    },
    {
        'id': 983,
        'link': 'https://gimsap.ca/collections/all/products/maggi-cube-seasoning-21x100-cubes-x-4g-box-expired',
        'name': 'Maggi Cube Seasoning (21x100 cubes x 4g) Box - Expired',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_51e5cd4c-b91f-4a32-bd03-f2ae851a4dfa_300x300.jpg?v=1645134385'
    },
    {
        'id': 984,
        'link': 'https://gimsap.ca/collections/all/products/maggi-nija-pot',
        'name': 'Maggi Nija Pot',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_2ff54cc4-6807-4670-b227-3179614ca1f5_300x300.jpg?v=1645134386'
    },
    {
        'id': 985,
        'link': 'https://gimsap.ca/collections/all/products/maggi-sarap',
        'name': 'Maggi Sarap',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $3.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1881b256-307d-4466-bdca-5d0b2410e64f_300x300.jpg?v=1645134387'
    },
    {
        'id': 986,
        'link': 'https://gimsap.ca/collections/all/products/maggi-shrimp-crevette-600g',
        'name': 'Maggi Shrimp Crevette 600g',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $15.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7f6e2a79-513f-468d-8587-164b6492ad12_300x300.jpg?v=1645134388'
    },
    {
        'id': 987,
        'link': 'https://gimsap.ca/collections/all/products/maggi-star',
        'name': 'Maggi Star',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $9.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_5d854da0-fed0-4f5b-88bd-9ba3033f1dff_300x300.jpg?v=1645134390'
    },
    {
        'id': 988,
        'link': 'https://gimsap.ca/collections/all/products/maggi-star-packed',
        'name': 'Maggi Star (packed)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $5.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_84b795cd-c76b-4bf3-b825-e7005dbfd1c6_300x300.jpg?v=1645134399'
    },
    {
        'id': 989,
        'link': 'https://gimsap.ca/collections/all/products/maggi-star-box',
        'name': 'Maggi Star Box',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $150.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_83322ba0-4ed1-42cf-a2cf-9af3a32345eb_300x300.jpg?v=1645134397'
    },
    {
        'id': 990,
        'link': 'https://gimsap.ca/collections/all/products/maggi-star-seasoning-cubes',
        'name': 'Maggi Star Seasoning Cubes',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $10.00',
        'description': '<p>Seasoning for soups, stews, grills, marinades, etc.</p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/iu-40_300x300.png?v=1606141954'
    },
    {
        'id': 991,
        'link': 'https://gimsap.ca/collections/all/products/magic-gold-hair-accessories',
        'name': 'Magic Gold Hair Accessories',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $2.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_d7274961-01eb-4f2f-b2e1-c107a992835a_300x300.jpg?v=1645134401'
    },
    {
        'id': 992,
        'link': 'https://gimsap.ca/collections/all/products/magic-gold-twin-afo-twist-braid',
        'name': 'Magic Gold Twin Afo Twist Braid',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $13.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4b4dc48e-cf8d-48d5-934a-9e119c2b4f92_300x300.jpg?v=1645134403'
    },
    {
        'id': 993,
        'link': 'https://gimsap.ca/collections/all/products/magic-gold-yarn-for-braid',
        'name': 'Magic Gold Yarn For Braid',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $1.75',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_4f482530-2975-49be-b0bd-c7542bfda663_300x300.jpg?v=1645134405'
    },
    {
        'id': 994,
        'link': 'https://gimsap.ca/collections/all/products/magic-malt-4x330-ml',
        'name': 'Magic Malt (4x330 ml)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_bb23f995-3f7a-46fd-9fee-1c167e9107f7_300x300.jpg?v=1645134407'
    },
    {
        'id': 995,
        'link': 'https://gimsap.ca/collections/all/products/magic-malt-bottle',
        'name': 'Magic Malt bottle',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $0.00',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_7c030f43-894a-4d2b-91e4-903b844bd614_300x300.jpg?v=1645134409'
    },
    {
        'id': 996,
        'link': 'https://gimsap.ca/collections/all/products/magic-razoless-cream',
        'name': 'Magic Razoless Cream',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_1b8b74df-0244-4480-93b8-d30475e2a34b_300x300.jpg?v=1645134410'
    },
    {
        'id': 997,
        'link': 'https://gimsap.ca/collections/all/products/magic-shave-cream-extra-strength-6oz',
        'name': 'Magic Shave Cream  Extra Strength (6oz)',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $8.99',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_3aa94c13-bf2b-47cf-b9ca-e9456a0e0a14_300x300.jpg?v=1645134412'
    },
    {
        'id': 998,
        'link': 'https://gimsap.ca/collections/all/products/magic-shaving-powder-fragrant',
        'name': 'Magic Shaving Powder Fragrant',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_a53b5b13-5ed0-40be-9373-d99e59109f7a_300x300.jpg?v=1645134413'
    },
    {
        'id': 999,
        'link': 'https://gimsap.ca/collections/all/products/magic-shaving-powder-skin-conditioning',
        'name': 'Magic Shaving Powder Skin Conditioning',
        'price': '<span class="visually-hidden">Regular price</span>\n          \n          $6.50',
        'description': '<p></p><p></p>',
        'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_ab8978ce-696e-4580-8b38-6e3b6f25573e_300x300.jpg?v=1645134414'
    }
]

with open('test_gimsap.json', 'w') as f:
    f.write(json.dumps(collection))
