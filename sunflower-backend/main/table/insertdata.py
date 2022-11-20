
from .mytable import *


def insert_data():
    u1 = User(username='Delicia',
              password='delicia123',
              avatar='https://i0.wp.com/www.groundedgirlsguide.com/wp-content/uploads/2016/10/GAYLE-ILLUSTRATED-HEADSHOT-HighRes.png?resize=768%2C846',
              email='Delicia123@gmail.com',
              BIO='Welcome to my kitchen',
              create_time='2022-10-01 23:18:17',
              following='2;3;9;10',
              like='1;2;3;10',
              tried='1;3;4;5;6;8;9;10')
    u2 = User(username='Ying Cheng',
              password='yingcheng123',
              avatar='https://sheisfiercehq.com/home/content/p3pnexwpnas06_data02/50/2350050/html/wp-content/uploads/2015/01/Kelly-Cartoon-Headshot-300x300.jpg',
              email='Yingcheng@gmail.com',
              BIO='I am a professional chef, welcome to my kitchen',
              create_time='2022-05-15 08:12:17',
              following='3;5',
              like='1;2;3;4;5;6',
              tried='1;3')
    u3 = User(username='Dylan',
              password='dylan123',
              avatar='https://climate-xchange.org/wp-content/uploads/2018/09/Ryan-Illustrated-Headshot-Circle-01-684x690.png',
              email='dylan123@gmail.com',
              BIO='I am a professional chef, nice to meet you',
              create_time='2022-06-20 10:15:30',
              following='1;2;5;6;9;12',
              like='2;3;4;5;6;7;8;9;12',
              tried='1')
    u4 = User(username='Kris Li',
              password='kris123456',
              avatar='https://517459.smushcdn.com/2168432/wp-content/uploads/2022/05/Steve-Anderson-01.png?lossy=1&strip=1&webp=1',
              email='kris123@126.com',
              BIO='Food Editor at Open Kitchen',
              create_time='2022-09-10 12:16:30',
              following='1',
              like='6',
              tried='')
    u5 = User(username='Devan Grimsrud',
              password='devan12345',
              avatar='https://517459.smushcdn.com/2168432/wp-content/uploads/2022/05/Savannah-2-01.png?lossy=1&strip=1&webp=1',
              email='devan123@126.com',
              BIO='I am new to Open Kitchen, please take care of me',
              create_time='2022-10-10 15:16:30',
              following='',
              like='',
              tried='1;2;3;4;5;12')
    u6 = User(username='Alan Chen',
              password='alan123456',
              avatar='https://sheisfiercehq.com/home/content/p3pnexwpnas06_data02/50/2350050/html/wp-content/uploads/2015/01/Kelly-Cartoon-Headshot-300x300.jpg',
              email='alan123@163.com',
              BIO='Test Kitchen Manager and Chef at Open Kitchen',
              create_time='2022-10-10 15:16:30',
              following='2;3;7',
              like='1;3;6;8;9;10',
              tried='3;4;5')
    u7 = User(username='Jamie Oliver',
              password='JamieOliver123',
              avatar='https://i0.wp.com/www.groundedgirlsguide.com/wp-content/uploads/2016/10/GAYLE-ILLUSTRATED-HEADSHOT-HighRes.png?resize=768%2C846',
              email='Jamie@gmial.com',
              BIO='Food Editor at Open Kitchen',
              create_time='2022-10-12 15:16:30',
              following='1;2;3;4;5;6;8;9',
              like='1;2;3;4;5;6',
              tried='')
    u8 = User(username='Candy Tian',
              password='CandyTian123',
              avatar='https://sheisfiercehq.com/home/content/p3pnexwpnas06_data02/50/2350050/html/wp-content/uploads/2015/01/Kelly-Cartoon-Headshot-300x300.jpg',
              email='CandyTian@gmail.com',
              BIO='Welcome to my kitchen',
              create_time='2022-1-12 15:16:30',
              following='6;7;10',
              like='1;2;3;4;5;6;7;8;9;10;11;12',
              tried='6;12')
    u9 = User(username='Adam',
              password='adam98765',
              avatar='https://i0.wp.com/www.groundedgirlsguide.com/wp-content/uploads/2016/10/GAYLE-ILLUSTRATED-HEADSHOT-HighRes.png?resize=768%2C846',
              email='adama123@gmail.com',
              BIO='I am a professional chef, nice to meet you',
              create_time='2022-1-12 15:16:30',
              following='1;6;7',
              like='',
              tried='8')
    u10 = User(username='Jackson Yi',
               password='jacksonYi123',
               avatar='https://climate-xchange.org/wp-content/uploads/2018/09/Ryan-Illustrated-Headshot-Circle-01-684x690.png',
               email='jackson123@gmail.com',
               BIO='I am new to Open Kitchen, please take care of me',
               create_time='2022-1-12 15:16:30',
               following='3;4;5;6;7;8;9',
               like='5;6;7',
               tried='5;6;7;9;10;11;12')

    # recip information
    r1 = Recipe(user_id=2,
                name='Kung Pao cauliflower',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FVvffW4mVMuLqxzEW3WyPS-IYyM0%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2724-final-photo-extra.jpg&w=1440&q=85',
                meal_type='Dinner',
                create_time='2022-05-16 08:12:17')
    r2 = Recipe(user_id=3,
                name='Vegan pulled mushroom burger',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FMSnusZzx9L-eGI8BL3NpYUaFK4o%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2643-photo-final-1.jpg&w=1440&q=85',
                meal_type='Lunch',
                create_time='2022-05-17 18:46:21')
    r3 = Recipe(user_id=5,
                name='Kale pesto pasta',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FI56_EjJC6cBmKwcGLEHaqQzwZhg%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2522-final-photo-new.jpg&w=1440&q=85',
                meal_type='Lunch',
                create_time='2022-05-18 19:46:21')
    r4 = Recipe(user_id=4,
                name='mushroom quesadillas',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fs747QN8WUZLPFiysOl_Glqqv3iE%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2547-final-photo-_0.jpg&w=1440&q=85',
                meal_type='Dinner',
                create_time='2022-05-19 20:46:21')
    r5 = Recipe(user_id=1,
                name='Cauliflower steak',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FCjlxXyEStLTiGFMbTrCmZddR5Sc%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeImages%2FR1258-photo-final.jpg&w=1440&q=85',
                meal_type='Dinner',
                create_time='2022-07-29 20:46:21')
    r6 = Recipe(user_id=6,
                name='Romanesco soup',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F56w9MY3Mzg4SHKW8ziXI2T4LoE0%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeImages%2FR932-photo-final-4x3.jpg&w=1440&q=85',
                meal_type='Breakfast',
                create_time='2022-09-29 21:46:21')
    r7 = Recipe(user_id=3,
                name='Carrot miso soup',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F-SrDpYqTpNLOsHVjbPRYrsS9IUg%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeImages%2FR888-photo-final-4x3.jpg&w=1440&q=85',
                meal_type='Lunch',
                create_time='2022-09-30 21:46:21')
    r8 = Recipe(user_id=7,
                name='Fluffy buttermilk pancakes',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F2ZYBYz50espQ-k3FRiLmCKN4Dzg%3D%2F864x648%2Fimages.kitchenstories.io%2FarticleCellImages%2F02_5PerfectPancakes_TITLE_2e484836.jpg&w=1440&q=90',
                meal_type='Lunch',
                create_time='2022-10-30 21:46:21')
    r9 = Recipe(user_id=8,
                name='Fluffy waffles',
                picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F70XyEpdu6hOmw_zVorB17YkXBXQ%3D%2F864x648%2Fimages.kitchenstories.io%2FrecipeImages%2F06_05_FluffigeWaffelnMitApfelZimtChutney_titlePicture.jpg&w=1440&q=90',
                meal_type='Breakfast',
                create_time='2022-10-30 21:46:21')
    r10 = Recipe(user_id=9,
                 name='Red, white, and blue trifle',
                 picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F6PMM2bUI4if7YKlfEBGJ6_LDrQQ%3D%2F864x648%2Fimages.kitchenstories.io%2FrecipeImages%2F06_31_03_blueRedAndWhiteBerryTrifle_TitlePicture.jpg&w=1440&q=90',
                 meal_type='Breakfast',
                 create_time='2022-10-30 21:46:21')
    r11 = Recipe(user_id=10,
                 name='Braised beef noodle soup',
                 picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FbMoy5KEucPWtO3T1RKrTKfvK9mY%3D%2F864x648%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2764-final-photo-_1.jpg&w=1440&q=90',
                 meal_type='Lunch',
                 create_time='2022-10-30 21:46:21')
    r12 = Recipe(user_id=8,
                 name='Chicken udon noodle soup',
                 picture='https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FQlS3dVm7ajGNthV7UsUJyaTX9ro%3D%2F864x648%2Fimages.kitchenstories.io%2FcommunityImages%2F7ac4fd82bfa49258c772ad60d8a914a8_823f17e6-5902-469b-adb2-33d6263273a8.jpg&w=1440&q=90',
                 meal_type='Lunch',
                 create_time='2022-10-30 21:46:21')

    # recip ingredient
    # 1.
    i2 = Recipe_Ingredient(id_recipe=1, ingredient_name='green bell pepper', ingredient_num=1, ingredient_unit='')
    i3 = Recipe_Ingredient(id_recipe=1, ingredient_name='yellow bell pepper', ingredient_num=1, ingredient_unit='')
    i1 = Recipe_Ingredient(id_recipe=1, ingredient_name='cauliflower', ingredient_num=600, ingredient_unit='g')
    i4 = Recipe_Ingredient(id_recipe=1, ingredient_name='ginger', ingredient_num=1, ingredient_unit='tbsp')
    i5 = Recipe_Ingredient(id_recipe=1, ingredient_name='garlic', ingredient_num=2, ingredient_unit='cloves')
    i6 = Recipe_Ingredient(id_recipe=1, ingredient_name='scallion', ingredient_num=1, ingredient_unit='')
    i7 = Recipe_Ingredient(id_recipe=1, ingredient_name='light soy sauce', ingredient_num=3, ingredient_unit='tbsp')
    i8 = Recipe_Ingredient(id_recipe=1, ingredient_name='dark rice vinegar', ingredient_num=4, ingredient_unit='tsp')
    i9 = Recipe_Ingredient(id_recipe=1, ingredient_name='vegetable broth', ingredient_num=120, ingredient_unit='ml')
    i10 = Recipe_Ingredient(id_recipe=1, ingredient_name='Sichuan peppercorn', ingredient_num=1, ingredient_unit='tsp')
    i11 = Recipe_Ingredient(id_recipe=1, ingredient_name='dried chilies', ingredient_num=2, ingredient_unit='')
    i12 = Recipe_Ingredient(id_recipe=1, ingredient_name='roasted peanuts', ingredient_num=20, ingredient_unit='g')
    i13 = Recipe_Ingredient(id_recipe=1, ingredient_name='vegetable oila', ingredient_num=3, ingredient_unit='tbsp')

    # 2.
    i14 = Recipe_Ingredient(id_recipe=2, ingredient_name='king oyster mushrooms', ingredient_num=500,
                            ingredient_unit='g')
    i15 = Recipe_Ingredient(id_recipe=2, ingredient_name='canola oil', ingredient_num=4, ingredient_unit='tbsp')
    i16 = Recipe_Ingredient(id_recipe=2, ingredient_name='garlic powder', ingredient_num=0.5, ingredient_unit='tsp')
    i17 = Recipe_Ingredient(id_recipe=2, ingredient_name='smoked paprika powder', ingredient_num=1,
                            ingredient_unit='tsp')
    i18 = Recipe_Ingredient(id_recipe=2, ingredient_name='cayenne pepper', ingredient_num=0.5, ingredient_unit='tsp')
    i19 = Recipe_Ingredient(id_recipe=2, ingredient_name='ground cumin', ingredient_num=0.5, ingredient_unit='tsp')
    i20 = Recipe_Ingredient(id_recipe=2, ingredient_name='ketchup', ingredient_num=4, ingredient_unit='tbsp')
    i21 = Recipe_Ingredient(id_recipe=2, ingredient_name='vegan Worcestershire sauce', ingredient_num=2,
                            ingredient_unit='')
    i22 = Recipe_Ingredient(id_recipe=2, ingredient_name='raw sugar', ingredient_num=1, ingredient_unit='tbsp')
    i23 = Recipe_Ingredient(id_recipe=2, ingredient_name='balsamic vinegar', ingredient_num=1, ingredient_unit='tbsp')
    i24 = Recipe_Ingredient(id_recipe=2, ingredient_name='red cabbage', ingredient_num=200, ingredient_unit='g')
    i25 = Recipe_Ingredient(id_recipe=2, ingredient_name='vegan mayonnaise', ingredient_num=4, ingredient_unit='tbsp')

    # 3.
    i26 = Recipe_Ingredient(id_recipe=3, ingredient_name='mixed mushrooms', ingredient_num=300, ingredient_unit='g')
    i27 = Recipe_Ingredient(id_recipe=3, ingredient_name='flour tortillas (large)', ingredient_num=2,
                            ingredient_unit='')
    i28 = Recipe_Ingredient(id_recipe=3, ingredient_name='sour cream', ingredient_num=4, ingredient_unit='tbsp')
    i29 = Recipe_Ingredient(id_recipe=3, ingredient_name='tabasco', ingredient_num=0.5, ingredient_unit='tsp')
    i30 = Recipe_Ingredient(id_recipe=3, ingredient_name='shredded cheddar cheese', ingredient_num=120,
                            ingredient_unit='g')
    i31 = Recipe_Ingredient(id_recipe=3, ingredient_name='salt', ingredient_num=10, ingredient_unit='g')
    i32 = Recipe_Ingredient(id_recipe=3, ingredient_name='pepper', ingredient_num=20, ingredient_unit='g')
    i33 = Recipe_Ingredient(id_recipe=3, ingredient_name='olive', ingredient_num=30, ingredient_unit='g')

    # 4.
    i34 = Recipe_Ingredient(id_recipe=4, ingredient_name='egg', ingredient_num=4, ingredient_unit='')
    i35 = Recipe_Ingredient(id_recipe=4, ingredient_name='new potatoes', ingredient_num=600, ingredient_unit='g')
    i36 = Recipe_Ingredient(id_recipe=4, ingredient_name='baby spinach', ingredient_num=300, ingredient_unit='g')
    i37 = Recipe_Ingredient(id_recipe=4, ingredient_name='shallot', ingredient_num=2, ingredient_unit='')
    i38 = Recipe_Ingredient(id_recipe=4, ingredient_name='garlic', ingredient_num=1, ingredient_unit='clove')
    i39 = Recipe_Ingredient(id_recipe=4, ingredient_name='crème fraîche', ingredient_num=250, ingredient_unit='g')
    i40 = Recipe_Ingredient(id_recipe=4, ingredient_name='mustard', ingredient_num=1, ingredient_unit='tbsp')

    # 5.
    i41 = Recipe_Ingredient(id_recipe=5, ingredient_name='cauliflower', ingredient_num=1, ingredient_unit='head')
    i42 = Recipe_Ingredient(id_recipe=5, ingredient_name='orange juice', ingredient_num=100, ingredient_unit='ml')
    i43 = Recipe_Ingredient(id_recipe=5, ingredient_name='peanut', ingredient_num=30, ingredient_unit='g')
    i44 = Recipe_Ingredient(id_recipe=5, ingredient_name='scallion', ingredient_num=50, ingredient_unit='g')
    i45 = Recipe_Ingredient(id_recipe=5, ingredient_name='mirin', ingredient_num=1, ingredient_unit='')
    i46 = Recipe_Ingredient(id_recipe=5, ingredient_name='peanut oil for frying', ingredient_num=80,
                            ingredient_unit='ml')
    i47 = Recipe_Ingredient(id_recipe=5, ingredient_name='peanut oil for serving', ingredient_num=80,
                            ingredient_unit='ml')
    i48 = Recipe_Ingredient(id_recipe=5, ingredient_name='fleur de sel for serving', ingredient_num=80,
                            ingredient_unit='ml')

    # 6.
    i49 = Recipe_Ingredient(id_recipe=6, ingredient_name='Romanesco', ingredient_num=300, ingredient_unit='g')
    i50 = Recipe_Ingredient(id_recipe=6, ingredient_name='walnut', ingredient_num=3, ingredient_unit='tbsp')
    i51 = Recipe_Ingredient(id_recipe=6, ingredient_name='mint', ingredient_num=10, ingredient_unit='g')
    i52 = Recipe_Ingredient(id_recipe=6, ingredient_name='onion', ingredient_num=1, ingredient_unit='')
    i53 = Recipe_Ingredient(id_recipe=6, ingredient_name='lemon (zest and juice)', ingredient_num=1, ingredient_unit='')
    i54 = Recipe_Ingredient(id_recipe=6, ingredient_name='olive oil (divided)', ingredient_num=4,
                            ingredient_unit='tbsp')
    i55 = Recipe_Ingredient(id_recipe=6, ingredient_name='bay leaf', ingredient_num=1,
                            ingredient_unit='')
    i56 = Recipe_Ingredient(id_recipe=6, ingredient_name='turmeric', ingredient_num=0.25,
                            ingredient_unit='tsp')
    i57 = Recipe_Ingredient(id_recipe=6, ingredient_name='coconut milk', ingredient_num=400,
                            ingredient_unit='ml')
    i58 = Recipe_Ingredient(id_recipe=6, ingredient_name='water', ingredient_num=250,
                            ingredient_unit='ml')
    i59 = Recipe_Ingredient(id_recipe=6, ingredient_name='salt', ingredient_num=0.5,
                            ingredient_unit='tsp')
    i60 = Recipe_Ingredient(id_recipe=6, ingredient_name='egg', ingredient_num=2,
                            ingredient_unit='')

    # 7.
    i61 = Recipe_Ingredient(id_recipe=7, ingredient_name='carrot', ingredient_num=500, ingredient_unit='g')
    i62 = Recipe_Ingredient(id_recipe=7, ingredient_name='onion', ingredient_num=1, ingredient_unit='cloves')
    i63 = Recipe_Ingredient(id_recipe=7, ingredient_name='garlic', ingredient_num=2, ingredient_unit='g')
    i64 = Recipe_Ingredient(id_recipe=7, ingredient_name='ginger', ingredient_num=10, ingredient_unit='')
    i65 = Recipe_Ingredient(id_recipe=7, ingredient_name='chili', ingredient_num=1, ingredient_unit='')
    i66 = Recipe_Ingredient(id_recipe=7, ingredient_name='coconut oil', ingredient_num=2, ingredient_unit='tbsp')
    i67 = Recipe_Ingredient(id_recipe=7, ingredient_name='vegetable stock', ingredient_num=750, ingredient_unit='ml')
    i68 = Recipe_Ingredient(id_recipe=7, ingredient_name='light miso paste', ingredient_num=0.5, ingredient_unit='tbsp')
    i69 = Recipe_Ingredient(id_recipe=7, ingredient_name='lime (juice)', ingredient_num=1, ingredient_unit='')

    # 8.
    i70 = Recipe_Ingredient(id_recipe=8, ingredient_name='egg', ingredient_num=1, ingredient_unit='')
    i71 = Recipe_Ingredient(id_recipe=8, ingredient_name='vegetable oil', ingredient_num=2, ingredient_unit='tbsp')
    i72 = Recipe_Ingredient(id_recipe=8, ingredient_name='maple syrup', ingredient_num=0.5, ingredient_unit='tbsp')
    i73 = Recipe_Ingredient(id_recipe=8, ingredient_name='buttermilk', ingredient_num=120, ingredient_unit='ml')
    i74 = Recipe_Ingredient(id_recipe=8, ingredient_name='flour', ingredient_num=100, ingredient_unit='g')
    i75 = Recipe_Ingredient(id_recipe=8, ingredient_name='baking power', ingredient_num=0.5, ingredient_unit='tsp')
    i76 = Recipe_Ingredient(id_recipe=8, ingredient_name='salt', ingredient_num=0.5, ingredient_unit='tsp')

    # 9
    i77 = Recipe_Ingredient(id_recipe=9, ingredient_name='butter', ingredient_num=100, ingredient_unit='g')
    i78 = Recipe_Ingredient(id_recipe=9, ingredient_name='sugar', ingredient_num=240, ingredient_unit='g')
    i79 = Recipe_Ingredient(id_recipe=9, ingredient_name='eggs', ingredient_num=2, ingredient_unit='')
    i80 = Recipe_Ingredient(id_recipe=9, ingredient_name='flour', ingredient_num=125, ingredient_unit='g')
    i81 = Recipe_Ingredient(id_recipe=9, ingredient_name='baking power', ingredient_num=1, ingredient_unit='tsp')
    i82 = Recipe_Ingredient(id_recipe=9, ingredient_name='milk', ingredient_num=100, ingredient_unit='ml')
    i83 = Recipe_Ingredient(id_recipe=9, ingredient_name='apples', ingredient_num=300, ingredient_unit='g')
    i84 = Recipe_Ingredient(id_recipe=9, ingredient_name='lemons', ingredient_num=2, ingredient_unit='')
    i85 = Recipe_Ingredient(id_recipe=9, ingredient_name='apple juice', ingredient_num=1, ingredient_unit='stick')

    # 10
    i86 = Recipe_Ingredient(id_recipe=10, ingredient_name='ladyfingers', ingredient_num=250, ingredient_unit='g')
    i87 = Recipe_Ingredient(id_recipe=10, ingredient_name='cream cheese', ingredient_num=1, ingredient_unit='kg')
    i88 = Recipe_Ingredient(id_recipe=10, ingredient_name='buttermilk', ingredient_num=140, ingredient_unit='ml')
    i89 = Recipe_Ingredient(id_recipe=10, ingredient_name='confectioner’s sugar', ingredient_num=220,
                            ingredient_unit='g')
    i90 = Recipe_Ingredient(id_recipe=10, ingredient_name='lemons', ingredient_num=3, ingredient_unit='')
    i91 = Recipe_Ingredient(id_recipe=10, ingredient_name='blueberries', ingredient_num=250, ingredient_unit='g')
    i92 = Recipe_Ingredient(id_recipe=10, ingredient_name='mint', ingredient_num=10, ingredient_unit='g')
    i93 = Recipe_Ingredient(id_recipe=10, ingredient_name='strawberries', ingredient_num=1, ingredient_unit='kg')

    # 11
    i94 = Recipe_Ingredient(id_recipe=11, ingredient_name='beef stock', ingredient_num=500, ingredient_unit='ml')
    i95 = Recipe_Ingredient(id_recipe=11, ingredient_name='water', ingredient_num=200, ingredient_unit='ml')
    i96 = Recipe_Ingredient(id_recipe=11, ingredient_name='ginger', ingredient_num=1, ingredient_unit='slices')
    i97 = Recipe_Ingredient(id_recipe=11, ingredient_name='scallion', ingredient_num=2, ingredient_unit='')
    i98 = Recipe_Ingredient(id_recipe=11, ingredient_name='start anise', ingredient_num=2, ingredient_unit='')
    i99 = Recipe_Ingredient(id_recipe=11, ingredient_name='bay leaves', ingredient_num=1, ingredient_unit='')
    i100 = Recipe_Ingredient(id_recipe=11, ingredient_name='cinnamon stick', ingredient_num=2, ingredient_unit='tbsp')
    i101 = Recipe_Ingredient(id_recipe=11, ingredient_name='fennel seeds', ingredient_num=2, ingredient_unit='')
    i102 = Recipe_Ingredient(id_recipe=11, ingredient_name='dried chills', ingredient_num=5, ingredient_unit='')
    i103 = Recipe_Ingredient(id_recipe=11, ingredient_name='Sichuan peppercorns', ingredient_num=10,
                             ingredient_unit='g')
    i104 = Recipe_Ingredient(id_recipe=11, ingredient_name='sugar', ingredient_num=1, ingredient_unit='tbsp')
    i105 = Recipe_Ingredient(id_recipe=11, ingredient_name='doubanjiang', ingredient_num=3, ingredient_unit='tbsp')
    i106 = Recipe_Ingredient(id_recipe=11, ingredient_name='light soy sauce', ingredient_num=1, ingredient_unit='tbsp')

    # 12
    i107 = Recipe_Ingredient(id_recipe=12, ingredient_name='whole chicken', ingredient_num=1, ingredient_unit='')
    i108 = Recipe_Ingredient(id_recipe=12, ingredient_name='orange', ingredient_num=1, ingredient_unit='')
    i109 = Recipe_Ingredient(id_recipe=12, ingredient_name='onions', ingredient_num=2, ingredient_unit='')
    i110 = Recipe_Ingredient(id_recipe=12, ingredient_name='garlic', ingredient_num=3, ingredient_unit='cloves')
    i111 = Recipe_Ingredient(id_recipe=12, ingredient_name='salt', ingredient_num=1, ingredient_unit='')
    i112 = Recipe_Ingredient(id_recipe=12, ingredient_name='chili', ingredient_num=1, ingredient_unit='tsp')
    i113 = Recipe_Ingredient(id_recipe=12, ingredient_name='oil', ingredient_num=1, ingredient_unit='tbsp')
    i114 = Recipe_Ingredient(id_recipe=12, ingredient_name='udon noodles', ingredient_num=500, ingredient_unit='g')
    i115 = Recipe_Ingredient(id_recipe=12, ingredient_name='shallots', ingredient_num=3, ingredient_unit='')
    i116 = Recipe_Ingredient(id_recipe=12, ingredient_name='lime', ingredient_num=1, ingredient_unit='')

    # recipe method
    # recipe 1
    s1 = Recipe_Method(id_recipe=1, method_step=1,
                       method_content="Preheat the oven to 220ºC/430ºF fan. Cut or use your hands to separate the cauliflower into small bite sized-florets. Add the cauliflower florets to a baking sheet lined with parchment paper. ​​Toss the cauliflower in vegetable oil and season with salt. Roast for approx. 18–20 min., until the cauliflowers are cooked and slightly charred.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fvx_Rh_rLF2iaPPcRlUAEskjBzK4%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2724-step-photo-_0.jpg&w=1440&q=85",
                       method_photo_file_name="step 1 picture name")
    s2 = Recipe_Method(id_recipe=1, method_step=2,
                       method_content="Meanwhile, roughly cut bell peppers into bite-sized pieces. Mince ginger and garlic. Slice scallions to 2–3 cm/1 in. pieces, and reserve some of the green parts for garnishing. To make the sauce, in a measuring cup or bowl, mix light soy sauce, dark soy sauce, sugar, dark rice vinegar, vegetable stock, and starch. Whisk until well combined.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FXRg7XGYQmRsOq-17FjcgzqBq8l0%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2724-step-photo-_1.jpg&w=1440&q=85",
                       method_photo_file_name="step 2 picture name")
    s3 = Recipe_Method(id_recipe=1, method_step=3,
                       method_content="In a frying pan, heat vegetable oil over medium heat. Add sichuan peppercorns and dried ​​chili, fry for a minute, then add ginger, garlic and scallion. Fry until fragrant. Then add bell peppers and fry for approx. 2 min. Deglaze with the sauce, then let it simmer for approx. 2–3 min. until it’s thickened and glossy.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FltzE9YNoVqhuR0gTDnOvyk7DeSs%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2724-step-photo-_2.jpg&w=1440&q=85",
                       method_photo_file_name="step 3 picture name")
    s4 = Recipe_Method(id_recipe=1, method_step=4,
                       method_content="Remove the cauliflower from the oven, add to the sauce, and mix until the florets are completely coated. Garnish with the leftover scallions and roasted peanuts. Serve with cooked rice.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FjEutBz1C_9q-BSf8_5N5UTEXOBw%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2724-step-photo-_4.jpg&w=1440&q=85",
                       method_photo_file_name="step 4 picture name")

    # recipe 2
    s5 = Recipe_Method(id_recipe=2, method_step=1,
                       method_content="Hold the king oyster mushrooms on the stems, and tear them with a fork or with your hands lengthwise along the stem into fine strips. Tear the rest into chunks. In a large bowl, mix canola oil with garlic powder, paprika, cayenne pepper, and cumin. Season with salt and pepper. Add mushroom strips and mix to combine. "
                                      "Then add the mushroom mixture to a hot frying pan. Turn only after approx. 5 min. for some roasting aromas. Fry for another approx. 7 min. until mushrooms are soft and slightly browned.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F0DvPLao0qii6A4doinynKrptlFM%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2643-photo-step-1.jpg&w=1440&q=85",
                       method_photo_file_name="step 1 picture name")
    s6 = Recipe_Method(id_recipe=2, method_step=2,
                       method_content="Preheat oven to 200°C/400ºF with top/bottom heat. To make the marinade, whisk together the ketchup, Worcestershire sauce, brown sugar, and balsamic vinegar in a large bowl. Add the sautéed mushrooms to the marinade, and mix until evenly coated. Spread on a baking sheet lined with parchment paper. "
                                      "Bake in the oven for approx. 15 min., or until the edges are crisp and brown.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FDsORdzibmxfBG1xo4Xrc7JetMPI%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2643-photo-step-2.jpg&w=1440&q=85",
                       method_photo_file_name="step 2 picture name")
    s7 = Recipe_Method(id_recipe=2, method_step=3,
                       method_content="To make the coleslaw, slice the red cabbage and carrots into thin strips. Finely slice the scallions. In a large bowl, first mix the red cabbage with sesame oil, half of the mayonnaise, and white balsamic vinegar. Toss with your hands for about 1 min. until the cabbage gets a soft consistency. "
                                      "Then add the carrots and scallions, mix, and season with salt, pepper, and a little lime juice.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FDOidIszgJq1vRSZnRVWdI2iYvts%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2643-photo-step-3.jpg&w=1440&q=85",
                       method_photo_file_name="step 3 picture name")
    s8 = Recipe_Method(id_recipe=2, method_step=4,
                       method_content="Toast burger buns on the cut side spread each with remaining mayonnaise, and drizzle with a few drops of lime juice. Assemble with pulled mushrooms and coleslaw on top.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FJc7peU5VRsIl8rkcXAuQKwht5C8%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2643-photo-step-4.jpg&w=1440&q=85",
                       method_photo_file_name="step 4 picture name")

    # recipe 3
    s9 = Recipe_Method(id_recipe=3, method_step=1,
                       method_content="Preheat oven to 150°C/300°F. Bring a large pot of salted water to a boil. Remove kale leaves from the stem and tear into bite-sized pieces. Pluck basil leaves. Zest and juice lemon.",
                       method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fwb8CicHQpAIxk49-rDCXnT7AO9k%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2522-step-photo-_0.jpg&w=1440&q=85",
                       method_photo_file_name="step 1 picture name")
    s10 = Recipe_Method(id_recipe=3, method_step=2,
                        method_content="Add cashews to a baking sheet, transfer to the preheated oven, and roast for approx. 6–8 min. until slightly brown and fragrant. Add kale and whole garlic cloves to the boiling water and blanch for approx. 1 min., "
                                       "then use tongs to scoop out and transfer the kale and garlic to a bowl of ice cold water. Bring the same water in the pot back up to a boil.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fz1mul2-xNVqBpRmDIyBfrU9X81M%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2522-step-photo-_1.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s11 = Recipe_Method(id_recipe=3, method_step=3,
                        method_content="Once the water is boiling again, add pasta and cook until al dente according to package instructions. Reserve some of the pasta cooking water, then drain the pasta and set aside.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FQZ9xg_Xx28q2DhxZtXx7pX_c0L0%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2522-step-photo-_2.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s12 = Recipe_Method(id_recipe=3, method_step=4,
                        method_content="While the pasta is cooking, add toasted cashews, lemon zest and juice, and basil to a food processor (or large measuring jug, if using an immersion blender). Drain kale and garlic, pat dry, "
                                       "and add to the food processor along with the olive oil. Blend until smooth. Season to taste with salt, pepper, and a pinch of sugar, then blend again to combine. Add pesto to the drained pasta and toss well to combine, adding a splash of the reserved pasta water, if needed. T"
                                       "he pesto should be thick and saucy. Serve immediately, garnished with some extra lemon zest.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FSjeb6L345Vw1AQfoWpLwAgh5qrw%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2522-step-photo-_3.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 4
    s13 = Recipe_Method(id_recipe=4, method_step=1,
                        method_content="Thinly slice mushrooms. Mix sour cream and hot sauce together in a small bowl and set aside, adding more hot sauce to your taste.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FUKRQhwjCo33RD_dMh2p3hNkJ99M%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2547-step-photo-_0.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s14 = Recipe_Method(id_recipe=4, method_step=2,
                        method_content="Heat a frying pan over medium. Once hot, add some olive oil and butter to the pan. Once the butter is melted, add sliced mushrooms and cook, stirring occasionally, until the mushrooms start to brown and have released their moisture, approx. 6 min. "
                                       "Season with salt and pepper to taste, then remove and wipe out pan with a paper towel.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FlrKkydEC_j8i54rz4VE_JUVg158%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2547-step-photo-_1.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s15 = Recipe_Method(id_recipe=4, method_step=3,
                        method_content="Replace wiped out frying pan over medium-high heat. Add a tortilla, then transfer half the cheese over the tortilla evenly. Add half the mushrooms, then wait until the cheese melts and the tortilla is browned. "
                                       "Use a spatula to help you fold the tortilla over itself to create a half moon, press together lightly. Remove to a cutting board and repeat.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F121B2chvjeyp8UZPpnHP5DmJpk0%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2547-step-photo-_2.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s16 = Recipe_Method(id_recipe=4, method_step=4,
                        method_content="Slice quesadillas into triangular pieces (about four from each quesadilla) and serve with spicy sour cream, lime wedges, and pickled red onions, as desired. Garnish with cilantro.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FxVeGL1k2NBAMn0uQBjFFzpB_zVk%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2547-step-photo-_3.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 5
    s17 = Recipe_Method(id_recipe=5, method_step=1,
                        method_content="Preheat oven to 220°C/430°C. Chop peanuts and thinly slice scallions. Add miso paste and orange juice to a small bowl and whisk to combine. Set aside.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fkw-PhOEjFWVV8t_rKo02JruuTW4%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR1258-photo-step-1.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s18 = Recipe_Method(id_recipe=5, method_step=2,
                        method_content="Wash cauliflower and cut off the green parts. Cut into 1-cm/0.5-in. thick slices. Heat peanut oil in an ovenproof pan and fry cauliflower on both sides.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FIvox4Qt226yx9JVhGjk7WwMXT_Y%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR1258-photo-step-2.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s19 = Recipe_Method(id_recipe=5, method_step=3,
                        method_content="Remove cauliflower steak from the pan. Add mirin and orange miso mixture to the pan and let reduce. Transfer cauliflower steak back to the pan, transfer to the oven, and bake at 220°C/430°F for approx. 10 min.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F2N4oTRFmCB2PnCrA-8QAyrxz8LE%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR1258-photo-step-3.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s20 = Recipe_Method(id_recipe=5, method_step=4,
                        method_content="Serve cauliflower steaks on a plate and drizzle with the sauce. Sprinkle with some peanut oil and fleur de sel. Top with sliced scallions and chopped peanuts.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FYNYStm9CPvspK3YC0_qiABuh7b0%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR1258-photo-step-4.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 6
    s21 = Recipe_Method(id_recipe=6, method_step=1,
                        method_content="Clean Romanesco, remove stem and out leaves, and pluck florets. Peel onion and dice. Zest lemon, then halve and juice.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FOJcyRw7gmhX-IHPephwrsndwKlg%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR932-photo-step-1.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s22 = Recipe_Method(id_recipe=6, method_step=2,
                        method_content="Heat the olive oil in the pot over medium-high heat and sauté the onion for approx. 1 min. Reduce heat, add Romanesco, and fry for approx. 3 min. Add the bay leaf and turmeric, then add coconut milk and water. Add salt to taste and simmer for approx. 15 min.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FL9S04oVzc0rzofnxc83jWfmlUdg%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR932-photo-step-2.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s23 = Recipe_Method(id_recipe=6, method_step=3,
                        method_content="To make the pesto, pluck the mint leaves from the stems and roughly chop. Mix the mint with walnuts, olive oil, and lemon zest and purée. Add salt, which protects the bright green color of the mint. Season the pesto again with salt, sugar, and lemon juice to taste. Then set the pesto aside.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FxyC_vvLw4O73qbZPC1ZQvmft4XM%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR932-photo-step-3.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s24 = Recipe_Method(id_recipe=6, method_step=4,
                        method_content="Remove the soup from the stove and purée with a hand blender until smooth. Season with salt, pepper, and more lemon juice to taste and serve with walnut-mint pesto. Enjoy!",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F2FWHaMyswg9wM4Is1amU-VNgRj0%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR932-photo-step-4.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 7
    s25 = Recipe_Method(id_recipe=7, method_step=1,
                        method_content="Peel and dice carrots. Chop onion, garlic, ginger, and chili.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FGduuTgtLVfLwrVI8-m0XgMdQKQQ%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR888-photo-step-4x3-1.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s26 = Recipe_Method(id_recipe=7, method_step=2,
                        method_content="Heat the coconut oil in a large saucepan and sauté the onion, garlic, ginger, and chili over medium heat.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F0r-zh9v2xLC44LUgRTIpgjADBv8%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR888-photo-step-4x3-2.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s27 = Recipe_Method(id_recipe=7, method_step=3,
                        method_content="Add the diced carrots to the pan and briefly sauté before adding the vegetable stock and bringing to a boil. Reduce heat and leave to simmer for approx. 20 min., or until the carrots soften slightly.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FypSLMLS4goMbSMCeLPauCND3Kng%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR888-photo-step-4x3-3.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s28 = Recipe_Method(id_recipe=7, method_step=4,
                        method_content="Remove the soup from the heat and purée with a hand blender. Return to heat and add the miso paste and lime juice. Simmer for 2 min. more. Add a dollop of coconut milk to each bowl, garnish with cilantro, and season with salt and pepper. Enjoy!",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FQ8rlG0n2l4zN-UuSKE0cTnGh__c%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2FR888-photo-step-4x3-5.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 8
    s29 = Recipe_Method(id_recipe=8, method_step=1,
                        method_content="Whisk egg in a mixing bowl until foamy.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Ff1SQ_bEZFoj-VxjHa7i5ih45hlI%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F02_12_FluffigeButtermilchPancakes_step01.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s30 = Recipe_Method(id_recipe=8, method_step=2,
                        method_content="Add oil, maple syrup, and butter milk and continue whisking.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FpymLd5bTNe2hUhsG3f8vwAcUuYc%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F02_12_FluffigeButtermilchPancakes_step02.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s31 = Recipe_Method(id_recipe=8, method_step=3,
                        method_content="Mix flour, baking powder, and a pinch of salt in a separate bowl and then gently fold into the liquid butter milk mixture. Let stand for approx. 15 – 20 min.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FdiGLgcxQNjeNSchUlIawsUdMGr8%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F02_12_FluffigeButtermilchPancakes_step03.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s32 = Recipe_Method(id_recipe=8, method_step=4,
                        method_content="Drop batter into skillet and cook on medium heat until golden-brown (approx. 2 – 3 min. per side, with a diameter of approx. 7cm). Serve with homemade jam or powdered sugar.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FKsyYb1jMmf6NFyeizomhjXWYJDk%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F02_12_FluffigeButtermilchPancakes_step04.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 9
    s33 = Recipe_Method(id_recipe=9, method_step=1,
                        method_content="Beat butter and approx. a third of the sugar in a standing mixer or with a hand mixer until fluffy. Add eggs one after the other and mix until incorporated.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FYHp9L4lVoRUOHxZj4BfOPdfmiC0%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_05_FluffigeWaffelnMitApfelZimtChutney_step01.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s34 = Recipe_Method(id_recipe=9, method_step=2,
                        method_content="Add flour, baking powder, a pinch of salt, and milk. Continue to mix until a smooth batter forms. For the chutney, cut apples into fine cubes.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FTXTX6gFHsRAWrDsH155DviIoegI%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_05_FluffigeWaffelnMitApfelZimtChutney_step03.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s35 = Recipe_Method(id_recipe=9, method_step=3,
                        method_content="Caramelize the remaining sugar in a small saucepan. Deglaze with lemon juice and reduce until the caramel is velvety. Add apple juice to the caramel and reduce on medium-high heat for another 5 min.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FS0R5oe-gYW8OIlvYZ6OJJ9KT8CI%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_05_FluffigeWaffelnMitApfelZimtChutney_step05.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s36 = Recipe_Method(id_recipe=9, method_step=4,
                        method_content="Add apple pieces, cinnamon stick and a pinch of salt and allow to reduce on medium heat for approx. 5 - 10 min. until the fruit has softened. Meanwhile, heat the waffle iron and grease if necessary. Bake the waffles in the waffle iron until golden. Serve warm with icing sugar and apple chutney.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FJrQuq8FijMbOhr1i6DIY5mGXRKY%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_05_FluffigeWaffelnMitApfelZimtChutney_step08.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 10
    s37 = Recipe_Method(id_recipe=10, method_step=1,
                        method_content="Place ladyfingers into a freezer bag. Tightly seal bag and crush roughly with a rolling pin.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fcf-r2UWGQ_cX3s8nGtBYNPCCxVo%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_31_03_blueRedAndWhiteBerryTrifle_Step01.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s38 = Recipe_Method(id_recipe=10, method_step=2,
                        method_content="In a large bowl, mix together cream cheese, buttermilk, three-quarters of the confectioner’s sugar, and some lemon juice. Stir thoroughly until well-incorporated. Leave blueberries whole and set aside. Roughly chop mint. Quarter strawberries.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FV7egzvKG8PSFoiyrwhMS3sVHQAw%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_31_03_blueRedAndWhiteBerryTrifle_Step02.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s39 = Recipe_Method(id_recipe=10, method_step=3,
                        method_content="Using a hand blender, blend together one quarter of the strawberries with the remainder of the powdered sugar and the lemon juice until pureed. In a large bowl, add puree to quartered strawberries and mint. Stir well to combine.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2Fp2QcScmLkDhGBAtMDmoUlr4qRKg%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_31_03_blueRedAndWhiteBerryTrifle_Step03.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s40 = Recipe_Method(id_recipe=10, method_step=4,
                        method_content="Line the bottom of a separate large bowl with some of the ladyfinger pieces. Then, continue to layer the cake as follows: cream cheese mixture, strawberry puree, cream cheese mixture, ladyfinger crumbs, strawberry puree, and cream cheese mixture. Finally, garnish the trifle with an even layer of blueberries. Leave in the refrigerator for 1 h to rest before serving.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FiHDvWJAFnRuj5SyzXLoxsi4L-vw%3D%2F768x576%2Fimages.kitchenstories.io%2FrecipeStepImages%2F06_31_03_blueRedAndWhiteBerryTrifle_Step05.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 11
    s41 = Recipe_Method(id_recipe=11, method_step=1,
                        method_content="Thinly slice ginger. Roughly cut scallion to long sticks, saving some green part for styling. Cut the beef into bite-sized chunks. Add to a heavy-bottom pot (you can use a normal one if you don’t happen to have a cast iron one) and cover with cold water with 2 slices of ginger. Bring it to a boil over medium heat, cook for approx. 3 min. Drain and wash the foam from the meat if necessary, set aside. Rinse the pot and dry for the next step.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FcXh-7OHWsom9ZVXAMDR-lPFOm70%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2764-step-photo-_0.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s42 = Recipe_Method(id_recipe=11, method_step=2,
                        method_content="In the same pot, heat some vegetable oil over medium heat. Once warm, add the sugar, melt and let caramelise until golden. Then add the beef chunks, stir to coat the chunks in the melted sugar. Add the remaining ginger, scallion, chili bean paste and all the spices to the beef. Fry briefly until fragrant. Then add light and dark soy sauce.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FocU7ufKqnnYIpSh8yZyLzAt-LFg%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2764-step-photo-_1.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s43 = Recipe_Method(id_recipe=11, method_step=3,
                        method_content="Add the stock and the water to the pot and bring it to a simmer. Cook the beef with the lid on, over medium-low heat, stew for at least 45 min., or until the soup has reduced, and the beef is soft. You can also cook longer for up to 2 hr. for a more tender meat.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F2MH-3IHgFxt8fn4K-4dzweaOxkA%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2764-step-photo-_2.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s44 = Recipe_Method(id_recipe=11, method_step=4,
                        method_content="Approx. 10 min. before your beef is ready, quarter bok choy. Set up a pot of water to boil, add your noodles and cook according to instructions. At the end of cooking time, add bok choy, cook for approx. 1 min. Divide the noodles and bok choy in bowls, add some cooking water (about 1 ladle per bowl or as wished), then top up with the braised beef and the soup. Garnish with cilantro and scallion if desired.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FKnujiescIqz_WAoiLcgQxSTYgpc%3D%2F768x576%2Fimages.kitchenstories.io%2FwagtailOriginalImages%2FR2764-step-photo-_6.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe 12
    s45 = Recipe_Method(id_recipe=12, method_step=1,
                        method_content="Peel the orange (preferably a pretty sour one) and cut into pieces. Chop 2 onions in big pieces and crush 5 cloves of garlic. Add oil into a deep oven pan. Stuff the chicken with garlic, onion and orange. Add salt, pepper and grill in the oven for about 1h or until it’s ready on 175 degrees Celsius. Add aluminium foil if needed to prevent burning the surface. Let cool for about 30 min - 1h.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F1qm_PaFJDLVNHJJM0o-lo6inHws%3D%2F768x576%2Fimages.kitchenstories.io%2FcommunityImages%2F7ac4fd82bfa49258c772ad60d8a914a8_944909e7-5187-4124-99e3-8f6e6f282802.jpg&w=1440&q=85",
                        method_photo_file_name="step 1 picture name")
    s46 = Recipe_Method(id_recipe=12, method_step=2,
                        method_content="Cut the chicken and save all the pieces for future dishes. Save the liquid from the bottom of the pan as well! Roast the chicken hull (including bones) on 200 degrees Celsius for about 20 minutes.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F1qm_PaFJDLVNHJJM0o-lo6inHws%3D%2F768x576%2Fimages.kitchenstories.io%2FcommunityImages%2F7ac4fd82bfa49258c772ad60d8a914a8_944909e7-5187-4124-99e3-8f6e6f282802.jpg&w=1440&q=85",
                        method_photo_file_name="step 2 picture name")
    s47 = Recipe_Method(id_recipe=12, method_step=3,
                        method_content="Chop 3 onions, 3 carrots and the celery stalks. Smash 4 garlic cloves. Fry it in 25g butter for about 5 min. Add the roasted chicken hull along with the chicken fat from the bottom of the oven pan. Let it cook with a lid for about 15 min on medium temp. Add 2 litres of water and salt and leave on low temp without a lid for about 2h.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2F1qm_PaFJDLVNHJJM0o-lo6inHws%3D%2F768x576%2Fimages.kitchenstories.io%2FcommunityImages%2F7ac4fd82bfa49258c772ad60d8a914a8_944909e7-5187-4124-99e3-8f6e6f282802.jpg&w=1440&q=85",
                        method_photo_file_name="step 3 picture name")
    s48 = Recipe_Method(id_recipe=12, method_step=4,
                        method_content="Time to start cooking the actual soup; chop the shallots in fine pieces. Smash 3 garlic cloves and chop them up as well. Fry it in sesame oil or other preferred oil until golden. Add the other spices (except cayenne) ground coriander, ground ginger, chopped chilli, juice from the lime, agave syrup and the stalks from the cilantro. Add some of the chicken stock that have been cooking for 2h. Save the rest of the liquid in your fridge for future dishes.",
                        method_photo="https://www.kitchenstories.com/_next/image?url=https%3A%2F%2Fimages.services.kitchenstories.io%2FZj8go6cFyo0_uOJcDDztBMper4w%3D%2F768x576%2Fimages.kitchenstories.io%2FcommunityImages%2F7ac4fd82bfa49258c772ad60d8a914a8_96925b45-e862-4033-aaa3-491dd8fe33e7.jpg&w=1440&q=85",
                        method_photo_file_name="step 4 picture name")

    # recipe comment
    # recipe 1
    c1 = Recipe_Comment(id_recipe=1, comment_username="Monika", comment_time="2022-06-12 21:46:21",
                        comment_content="I can only recommend this dish! Extremely delicious! I used 2 pickled Thai chilies, which I removed after cooking. The sharpness was just right. Instead of black rice vinegar, I used light rice vinegar. The taste of the sauce is simply brilliant")
    c2 = Recipe_Comment(id_recipe=1, comment_username="Daniel Risch", comment_time="2022-10-25 12:16:30",
                        comment_content="Easy to prepare Tastes delicious. The sauce is awesome can I enjoy any other Asian dishes")
    c3 = Recipe_Comment(id_recipe=1, comment_username="Sabine", comment_time="2022-3-21 15:16:30",
                        comment_content="Super delicious. It was easy to cook")

    # recipe 2
    c4 = Recipe_Comment(id_recipe=2, comment_username="Paulina Bechtgold", comment_time="2022-03-16 15:16:30",
                        comment_content="We are such a fan of burgers — really great recipe! These were our first burgers & since then we've been making less sesame oil, the specified amount of vinegar and a little more mayonnaise on the red cabbage. As a result, it sticks better to red cabbage.")
    c5 = Recipe_Comment(id_recipe=2, comment_username="peter", comment_time="2022-06-12 21:46:21",
                        comment_content="It was super delicious. I served the coleslaw separately. And pita rolls are taken")
    c6 = Recipe_Comment(id_recipe=2, comment_username="Kitana T", comment_time="2022-10-25 12:16:30",
                        comment_content="It's very tasty and pretty straight forward and simple to make.")

    # recipe 3
    c7 = Recipe_Comment(id_recipe=3, comment_username="Valya Gavar", comment_time="2022-06-12 21:46:21",
                        comment_content="Great way to eat more of delicious kale very summery and refreshing")
    c8 = Recipe_Comment(id_recipe=3, comment_username="leseratte69", comment_time="2022-10-25 12:16:30",
                        comment_content="I've eaten a lot of kale, but this one is definitely the tastiest!")
    c9 = Recipe_Comment(id_recipe=3, comment_username="Irene Hubertz", comment_time="2022-9-15 15:16:30",
                        comment_content="Very good")

    # recipe 4
    c10 = Recipe_Comment(id_recipe=4, comment_username="Matthew Fedorov", comment_time="2022-01-03 15:16:30",
                         comment_content="Looks great! ")
    c11 = Recipe_Comment(id_recipe=4, comment_username="Renee", comment_time="2022-03-16 21:46:21",
                         comment_content="I’m going to have to try this. My favourite Quesadilla is actually chicken and old age cheese onions do sound great though")
    c12 = Recipe_Comment(id_recipe=4, comment_username="Hallie Tischendorf", comment_time="2022-6-15 12:16:30",
                         comment_content="Tastes amazing! (apologies for the poor presentation)")

    # recipe 5
    c13 = Recipe_Comment(id_recipe=5, comment_username="Leoleoolé", comment_time="2022-01-03 12:16:30",
                         comment_content="Delicious!. I didn't have peanuts, but there was a lot of coriander with it and I made a few chilli flakes in the sauce")
    c14 = Recipe_Comment(id_recipe=5, comment_username="Michaela Pohl", comment_time="2022-09-26 21:46:21",
                         comment_content="The idea with the miso orange sauce is wonderful. A really tasty dish!", )
    c15 = Recipe_Comment(id_recipe=5, comment_username="Freddy", comment_time="2022-1-21 15:16:30",
                         comment_content="Fresh oranges came on top for me!")

    # recipe 6
    c16 = Recipe_Comment(id_recipe=6, comment_username="Marcin Sokolowski", comment_time="2022-06-12 12:16:30",
                         comment_content="Very refreshing. With strong taste of lemon and mint. With my variation I added a little bit of nutmeg, a cream cheese about six triangles. And made some tosties from brown bread.")
    c17 = Recipe_Comment(id_recipe=6, comment_username="Allegra Wappler", comment_time="2022-09-26 15:16:30",
                         comment_content="Very tasty and fast.")
    c18 = Recipe_Comment(id_recipe=6, comment_username="Katrin Barben", comment_time="2022-3-15 21:46:21",
                         comment_content="A wonderful soup!")

    # recipe 7
    c19 = Recipe_Comment(id_recipe=7, comment_username="Dominik Steimer", comment_time="2022-03-12 12:16:30",
                         comment_content="Delicious! Highly Recommended.")
    c20 = Recipe_Comment(id_recipe=7, comment_username="Darlene Jones", comment_time="2022-07-13 12:16:30",
                         comment_content="Added one more garlic and used sumbal oelek paste and a dash of red pepper flakes. It was delish!!!")
    c21 = Recipe_Comment(id_recipe=7, comment_username="Jen", comment_time="2022-06-14 12:16:30",
                         comment_content="Was so tasty - excellent recipe")

    # recipe 8
    c22 = Recipe_Comment(id_recipe=8, comment_username="Dominik Steimer", comment_time="2022-03-12 12:16:30",
                         comment_content="Delicious! Highly Recommended.")

    # recipe 9
    c23 = Recipe_Comment(id_recipe=9, comment_username="Hero Sirawich", comment_time="2022-03-12 12:16:30",
                         comment_content="It’s so good, I like it!")
    c24 = Recipe_Comment(id_recipe=9, comment_username="kirschmond", comment_time="2022-06-12 12:16:30",
                         comment_content="Super delicious and very fluffy waffles")

    # recipe 10
    c25 = Recipe_Comment(id_recipe=10, comment_username="WoHieber", comment_time="2022-05-12 12:16:30",
                         comment_content="Mega delicious.")

    # recipe 11
    c26 = Recipe_Comment(id_recipe=11, comment_username="Aley Goldchains", comment_time="2022-01-12 12:16:30",
                         comment_content="Hey, I loved really loved this dish")
    c27 = Recipe_Comment(id_recipe=11, comment_username="Carolin", comment_time="2022-06-12 12:16:30",
                         comment_content="Hello, where do I get the beef broth from? ")
    c28 = Recipe_Comment(id_recipe=11, comment_username="Ralf Schmidt", comment_time="2022-03-12 12:16:30",
                         comment_content="Super delicious and the spiciness is right!")

    # recipe 12
    c29 = Recipe_Comment(id_recipe=12, comment_username="kiiler ida", comment_time="2022-06-12 12:16:30",
                         comment_content="Took soooo long, but tasted great!")
    c30 = Recipe_Comment(id_recipe=12, comment_username="Delacour Matt", comment_time="2022-12-12 12:16:30",
                         comment_content="Was so tasty - excellent recipe")

    # recipe rating
    # rating 1
    t1 = Recipe_Rating(id_recipe=1, rating_time="2022-06-12 13:16:30", rating_username="Delicia", rating="3")
    t2 = Recipe_Rating(id_recipe=1, rating_time="2022-06-13 13:16:30", rating_username="Ying Cheng", rating="3")
    t3 = Recipe_Rating(id_recipe=1, rating_time="2022-06-14 14:16:30", rating_username="Dylan", rating="2")

    # rating 2
    t4 = Recipe_Rating(id_recipe=2, rating_time="2022-06-12 12:16:30", rating_username="Ying Cheng", rating="4")
    t5 = Recipe_Rating(id_recipe=2, rating_time="2022-06-14 14:16:30", rating_username="Dylan", rating="2")
    t6 = Recipe_Rating(id_recipe=2, rating_time="2022-06-16 16:16:30", rating_username="Devan Grimsrud", rating="4")

    # rating 3
    t7 = Recipe_Rating(id_recipe=3, rating_time="2022-06-12 12:16:30", rating_username="Delicia", rating="4")
    t8 = Recipe_Rating(id_recipe=3, rating_time="2022-06-13 13:16:30", rating_username="Ying Cheng", rating="2")

    # rating 4
    t9 = Recipe_Rating(id_recipe=4, rating_time="2022-06-12 12:16:30", rating_username="Delicia", rating="1")
    t10 = Recipe_Rating(id_recipe=4, rating_time="2022-06-13 13:16:30", rating_username="Ying Cheng", rating="3")

    # rating 5
    t11 = Recipe_Rating(id_recipe=5, rating_time="2022-06-12 12:16:30", rating_username="Jackson Yi", rating="2")

    # rating 6
    t12 = Recipe_Rating(id_recipe=6, rating_time="2022-06-12 12:16:30", rating_username="Delicia", rating="3")

    # rating 7
    t13 = Recipe_Rating(id_recipe=7, rating_time="2022-06-14 14:16:30", rating_username="Jackson Yi", rating="2")
    t14 = Recipe_Rating(id_recipe=7, rating_time="2022-06-12 12:16:30", rating_username="Kris Li", rating="3")
    t15 = Recipe_Rating(id_recipe=7, rating_time="2022-06-16 16:16:30", rating_username="Devan Grimsrud", rating="4")

    # rating 8
    t16 = Recipe_Rating(id_recipe=8, rating_time="2022-06-16 16:16:30", rating_username="Devan Grimsrud", rating="4")

    # rating 9
    t17 = Recipe_Rating(id_recipe=9, rating_time="2022-06-16 16:16:30", rating_username="Candy Tian", rating="2")

    # rating 10
    t18 = Recipe_Rating(id_recipe=10, rating_time="2022-06-15 15:16:30", rating_username="Kris Li", rating="5")
    t19 = Recipe_Rating(id_recipe=10, rating_time="2022-06-16 16:16:30", rating_username="Devan Grimsrud", rating="4")

    # rating 11
    t20 = Recipe_Rating(id_recipe=11, rating_time="2022-06-16 16:16:30", rating_username="Adam", rating="3")
    t21 = Recipe_Rating(id_recipe=11, rating_time="2022-09-30 16:16:30", rating_username="Jackson Yi", rating="5")
    t22 = Recipe_Rating(id_recipe=11, rating_time="2022-10-16 16:16:30", rating_username="Candy Tian", rating="2")

    # rating 12
    t23 = Recipe_Rating(id_recipe=12, rating_time="2022-06-16 16:16:30", rating_username="Adam", rating="5")

    db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,
                        i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20,
                        i21, i22, i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39,
                        i40, i41, i42, i43, i44, i45, i46, i47, i48, i49, i50, i51, i52, i53, i54, i55, i56, i57, i58,
                        i59, i60, i61, i62, i63, i64, i65, i66, i67, i68, i69, i70, i71, i72, i73, i74, i75, i76, i77,
                        i78, i79, i80, i81, i82, i83, i84, i85, i86, i87, i88, i89, i90, i91, i92, i93, i94, i95, i96,
                        i97, i98, i99, i100, i101, i102, i103, i104, i105, i106, i107, i108, i109, i110, i111, i112,
                        i113, i114, i115, i116,
                        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10,
                        s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29,
                        s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47, s48,
                        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21,
                        c22, c23, c24, c25, c26, c27, c28, c29, c30,
                        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,
                        t22, t23])
                        
    db.session.commit()