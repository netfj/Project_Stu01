#coding:utf-8
import SQLiteClass

dbt = SQLiteClass.dbt('TestGoods.db')

dbt.CreateTable('goods',[
'goods_id Integer PRIMARY KEY autoincrement',
  'goods_sn text',
  'cat_id  Integer',
  'brand_id  Integer',
  'goods_name text',
  'shop_price NUMERIC',
  'market_price NUMERIC',
  'goods_number Integer NOT NULL DEFAULT 1',
  'click_count Integer',
  'goods_weight NUMERIC',
  'goods_brief text',
  'goods_desc text',
  'thumb_img text',
  'goods_img text',
  'ori_img text',
  'is_on_sale Integer  NOT NULL DEFAULT 1',
  'is_delete Integer',
  'is_best Integer NOT NULL DEFAULT 0',
  'is_new Integer NOT NULL DEFAULT 0',
  'is_hot Integer NOT NULL DEFAULT 0',
  'add_time Integer',
  'last_update Integer '
])

dbt.InsertValueMulti_old('goods',[('*'),(1,'BL2012121939587',2,0,'两扣双开衩平驳头斜兜男士西服套装3312/纯藏青色人字纹/羊毛+涤纶',799.00,1598.00,1,0,0.000,'','','data/images/201212/19/thumb_aifwnt.JPG','data/images/201212/19/goods_aifwnt.JPG','data/images/201212/19/aifwnt.JPG',1,0,0,1,0,1355915283,0),(2,'BL2012121913673',2,0,'纯羊毛一粒扣枪驳领纯黑西服套装',999.00,1325.00,1,0,0.000,'','','data/images/201212/19/thumb_z2gd86.JPG','data/images/201212/19/goods_z2gd86.JPG','data/images/201212/19/z2gd86.JPG',1,0,0,0,0,1355915493,0),(3,'BL2012121919874',2,0,'两扣平驳领棕色格纹男士休闲单西D6959',1490.00,1643.00,1,0,0.000,'','','data/images/201212/19/thumb_dx9ghq.JPG','data/images/201212/19/goods_dx9ghq.JPG','data/images/201212/19/dx9ghq.JPG',1,0,0,0,0,1355915572,0),(4,'BL2012121970923',3,0,'蓝黑竖条纹男士休闲衬衫',199.00,238.00,1,0,0.000,'','','data/images/201212/19/thumb_juir8s.JPG','data/images/201212/19/goods_juir8s.JPG','data/images/201212/19/juir8s.JPG',1,0,0,0,0,1355915656,0),(5,'BL2012121980647',3,0,'蓝底提花咖色竖条纹修身正装衬衫',199.00,234.00,1,0,0.000,'','','data/images/201212/19/thumb_rad3wq.JPG','data/images/201212/19/goods_rad3wq.JPG','data/images/201212/19/rad3wq.JPG',1,0,0,0,0,1355915689,0),(6,'BL2012121956217',3,0,'男士短袖衬衫A52D/纯白暗竖纹/莫代尔棉',45.00,54.00,1,0,0.000,'','','data/images/201212/19/thumb_3fckzt.jpg','data/images/201212/19/goods_3fckzt.jpg','data/images/201212/19/3fckzt.jpg',1,0,0,0,0,1355915726,0),(7,'BL2012121936338',5,0,'枪驳大领面后开叉短款两扣女士正装',567.00,1324.00,1,0,0.000,'','','data/images/201212/19/thumb_wcri9z.JPG','data/images/201212/19/goods_wcri9z.JPG','data/images/201212/19/wcri9z.JPG',1,0,0,0,0,1355915834,0),(8,'BL2012121994403',5,0,'泡泡袖后领色丁拼接平驳领一扣女士正装套裤/黑色',482.00,897.00,1,0,0.000,'','','data/images/201212/19/thumb_5tsyhu.JPG','data/images/201212/19/goods_5tsyhu.JPG','data/images/201212/19/5tsyhu.JPG',1,0,0,0,0,1355915895,0),(9,'BL2012121977239',5,0,'本白压褶下摆短袖套裙',318.00,564.00,1,0,0.000,'','','data/images/201212/19/thumb_ay86zh.JPG','data/images/201212/19/goods_ay86zh.JPG','data/images/201212/19/ay86zh.JPG',1,0,0,0,0,1355915936,0),(10,'BL2012121941490',5,0,'枪驳大领面1扣女士正装/亮咖色',499.00,675.00,1,0,0.000,'','','data/images/201212/19/thumb_n29dmp.JPG','data/images/201212/19/goods_n29dmp.JPG','data/images/201212/19/n29dmp.JPG',1,0,0,0,0,1355915993,0),(11,'BL2012121985783',6,0,'纯白斜条棉涤女士衬衫',42.00,67.00,1,0,0.000,'','','data/images/201212/19/thumb_byadc8.JPG','data/images/201212/19/goods_byadc8.JPG','data/images/201212/19/byadc8.JPG',1,0,0,0,0,1355916069,0),(12,'BL2012121952838',6,0,'女士长袖衬衫165/蓝条纹/莫代尔棉V领花边',99.00,134.00,1,0,0.000,'','','data/images/201212/19/thumb_2mhjt4.JPG','data/images/201212/19/goods_2mhjt4.JPG','data/images/201212/19/2mhjt4.JPG',1,0,0,0,0,1355916106,0),(13,'BL2012121982746',6,0,'白色暗竖纹V领莫代尔棉衬衫',89.00,156.00,1,0,0.000,'','','data/images/201212/19/thumb_fys85v.JPG','data/images/201212/19/goods_fys85v.JPG','data/images/201212/19/fys85v.JPG',1,0,0,0,0,1355916157,0),(14,'BL2012121992429',8,0,'男士系带正装鞋/黑色/牛皮',150.00,250.00,1,0,0.000,'','','data/images/201212/19/thumb_yvwnc9.JPG','data/images/201212/19/goods_yvwnc9.JPG','data/images/201212/19/yvwnc9.JPG',1,0,0,0,0,1355916281,0),(15,'BL2012121971035',8,0,'滑轮添奴男士系带正装鞋/牛皮',150.00,250.00,1,0,0.000,'','','data/images/201212/19/thumb_dh2yxm.JPG','data/images/201212/19/goods_dh2yxm.JPG','data/images/201212/19/dh2yxm.JPG',1,0,0,0,0,1355916549,0),(16,'BL2012121977793',8,0,'全牛皮小圆头正装鞋',199.00,234.00,1,0,0.000,'','','data/images/201212/19/thumb_iu5xgq.JPG','data/images/201212/19/goods_iu5xgq.JPG','data/images/201212/19/iu5xgq.JPG',1,0,0,0,0,1355916612,0),(17,'BL2012121952414',7,0,'鞋面三扣装饰胎牛皮带绒中跟踝靴/黑色',299.00,399.00,1,0,0.000,'','','data/images/201212/19/thumb_i7pqy8.JPG','data/images/201212/19/goods_i7pqy8.JPG','data/images/201212/19/i7pqy8.JPG',1,0,0,0,0,1355916746,0),(18,'BL2012121957666',9,0,'简约中跟女士正装鞋黑色',199.00,399.00,1,0,0.000,'','','data/images/201212/19/thumb_fsuh7j.JPG','data/images/201212/19/goods_fsuh7j.JPG','data/images/201212/19/fsuh7j.JPG',1,0,0,0,0,1355916792,0),(19,'BL2012121917277',9,0,'单侧镶钻漆皮中跟正装鞋/黑色',145.00,234.00,1,0,0.000,'','','data/images/201212/19/thumb_uigxw5.JPG','data/images/201212/19/goods_uigxw5.JPG','data/images/201212/19/uigxw5.JPG',1,0,0,0,0,1355916829,0),(20,'BL2012121993042',11,0,'深蓝纯色领带',89.00,139.00,1,0,0.000,'','','data/images/201212/19/thumb_cbnrqe.JPG','data/images/201212/19/goods_cbnrqe.JPG','data/images/201212/19/cbnrqe.JPG',1,0,0,0,0,1355916948,0),(21,'BL2012121965862',11,0,'100%桑蚕丝天蓝底黑斜纹领带',128.00,234.00,1,0,0.000,'','','data/images/201212/19/thumb_uc9n7f.JPG','data/images/201212/19/goods_uc9n7f.JPG','data/images/201212/19/uc9n7f.JPG',1,0,0,0,0,1355916979,0),(22,'BL2012121940360',11,0,'100%桑蚕丝灰黑斜条纹领带',128.00,234.00,1,0,0.000,'','','data/images/201212/19/thumb_m5qd2j.JPG','data/images/201212/19/goods_m5qd2j.JPG','data/images/201212/19/m5qd2j.JPG',1,0,0,0,0,1355917010,0),(23,'BL2012121939272',12,0,'不锈钢自动扣荔枝纹牛皮正装腰带',69.00,129.00,1,0,0.000,'','','data/images/201212/19/thumb_kixvwy.JPG','data/images/201212/19/goods_kixvwy.JPG','data/images/201212/19/kixvwy.JPG',1,0,0,0,0,1355917090,0),(24,'BL2012121926113',12,0,'黑色烤漆不锈钢自动扣细纹牛皮正装腰带',89.00,169.00,1,0,0.000,'','','data/images/201212/19/thumb_avkfd4.JPG','data/images/201212/19/goods_avkfd4.JPG','data/images/201212/19/avkfd4.JPG',1,0,0,0,0,1355917125,0),(25,'BL2012121943041',12,0,'银色不锈钢针扣头层小牛皮二层同色皮底正装腰带',99.00,169.00,1,0,0.000,'','','data/images/201212/19/thumb_nv7cas.JPG','data/images/201212/19/goods_nv7cas.JPG','data/images/201212/19/nv7cas.JPG',1,0,0,0,0,1355917162,0)])

dbt.CreateTable('category',[
  'cat_id Integer PRIMARY KEY autoincrement',
  'cat_name text',
  'intro text',
  'parent_id IntegerNOT NULL DEFAULT 0'
])


dbt.InsterExecute("INSERT INTO 'category' VALUES (1,'男士正装','男士正装',0),(2,'西装','西装',1),(3,'衬衫','衬衫',1),(4,'女士正装','女士正装',0),(5,'套装','套装',4),(6,'衬衫','衬衫',4),(7,'正装鞋','正装鞋',0),(8,'男士皮鞋','男士皮鞋',7),(9,'女士皮鞋','女士皮鞋',7),(10,'配饰','配饰',0),(11,'领带','领带',10),(12,'皮带','皮带',10);")
