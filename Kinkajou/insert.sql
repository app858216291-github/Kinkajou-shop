-- --------------------------------------------------------
-- 主机:                           rm-m5e86q52h5lpu678evo.mysql.rds.aliyuncs.com
-- 服务器版本:                        5.7.25-log - Source distribution
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 shop 的数据库结构
CREATE DATABASE IF NOT EXISTS `shop` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `shop`;

-- 导出  表 shop.address 结构
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `mobile` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `area` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  `orderId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=738 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.address 的数据：~497 rows (大约)
DELETE FROM `address`;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` (`id`, `create_time`, `update_time`, `remark`, `status`, `receiver`, `mobile`, `address`, `area`, `default`, `userId`, `orderId`) VALUES
	(732, '2021-07-15 13:36:54', '2021-07-15 13:36:54', NULL, 0, NULL, '13774514086', '北京市北京市东城区', '1', NULL, NULL, 714),
	(733, '2021-08-16 21:27:36', '2021-08-16 21:27:36', NULL, 0, '还', '18818818808', '北京市北京市东城区', '很好', 0, 258, NULL),
	(734, '2021-08-16 21:27:40', '2021-08-16 21:27:40', NULL, 0, NULL, '18818818808', '北京市北京市东城区', '很好', NULL, NULL, 715),
	(735, '2021-08-20 08:43:19', '2021-08-20 08:43:19', NULL, 0, '22', '13635636586', '北京市北京市东城区', '版本', 0, 262, NULL),
	(736, '2021-10-14 22:06:17', '2021-10-14 22:06:17', NULL, 0, '11', '15803583488', '北京市北京市东城区', '11', 0, 333, NULL),
	(737, '2021-10-14 22:06:21', '2021-10-14 22:06:21', NULL, 0, NULL, '15803583488', '北京市北京市东城区', '11', NULL, NULL, 716);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;

-- 导出  表 shop.admin__user 结构
CREATE TABLE IF NOT EXISTS `admin__user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  shop.admin__user 的数据：~0 rows (大约)
DELETE FROM `admin__user`;
/*!40000 ALTER TABLE `admin__user` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin__user` ENABLE KEYS */;

-- 导出  表 shop.after_sales 结构
CREATE TABLE IF NOT EXISTS `after_sales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `orderId` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  `replay` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.after_sales 的数据：~5 rows (大约)
DELETE FROM `after_sales`;
/*!40000 ALTER TABLE `after_sales` DISABLE KEYS */;
INSERT INTO `after_sales` (`id`, `create_time`, `update_time`, `remark`, `status`, `orderId`, `type`, `desc`, `replay`) VALUES
	(1, '2021-04-24 12:30:24', '2021-04-24 12:30:24', NULL, 0, NULL, 0, 'ii', NULL),
	(2, '2021-04-24 12:31:24', '2021-04-24 12:31:24', NULL, 0, NULL, 0, '4444', NULL),
	(3, '2021-04-24 12:38:15', '2021-04-24 12:38:15', NULL, 0, 515, 0, '33', NULL),
	(4, '2021-05-05 23:21:31', '2021-05-05 23:21:31', NULL, 0, 557, 0, '退款', NULL),
	(5, '2021-05-05 23:21:32', '2021-05-05 23:21:32', NULL, 0, 557, 0, '退款', NULL);
/*!40000 ALTER TABLE `after_sales` ENABLE KEYS */;

-- 导出  表 shop.brown_his 结构
CREATE TABLE IF NOT EXISTS `brown_his` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2203 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.brown_his 的数据：~1,269 rows (大约)
DELETE FROM `brown_his`;
/*!40000 ALTER TABLE `brown_his` DISABLE KEYS */;
INSERT INTO `brown_his` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `userid`) VALUES
	(277, '2019-10-03 10:27:18', '2019-10-03 10:27:18', NULL, 0, 435, NULL),
	(278, '2019-10-03 10:27:22', '2019-10-03 10:27:22', NULL, 0, 437, NULL),
	(2202, '2021-10-22 18:39:41', '2021-10-22 18:39:41', NULL, 0, 11, NULL);
/*!40000 ALTER TABLE `brown_his` ENABLE KEYS */;

-- 导出  表 shop.car 结构
CREATE TABLE IF NOT EXISTS `car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `mount` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `propid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.car 的数据：~5 rows (大约)
DELETE FROM `car`;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `mount`, `userid`, `propid`) VALUES
	(119, '2021-07-01 21:13:59', '2021-07-01 21:13:59', NULL, 0, 0, 1, 103, 0),
	(127, '2021-07-05 23:15:47', '2021-07-05 23:15:47', NULL, 0, 0, 1, 109, 154),
	(147, '2021-09-28 21:57:31', '2021-10-07 07:02:03', NULL, 0, 22, 3, 321, 0),
	(148, '2021-10-07 07:02:21', '2021-10-07 07:02:21', NULL, 0, 681, 1, 321, 0),
	(149, '2021-10-07 07:03:49', '2021-10-07 07:03:49', NULL, 0, 6, 1, 321, 157);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;

-- 导出  表 shop.category 结构
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `picture` varchar(1024) DEFAULT NULL,
  `hasChild` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.category 的数据：~12 rows (大约)
DELETE FROM `category`;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` (`id`, `create_time`, `update_time`, `remark`, `status`, `cid`, `pid`, `name`, `picture`, `hasChild`) VALUES
	(5, '2021-03-24 19:44:59', '2021-03-24 20:06:36', NULL, 0, 105, 0, '建兰', NULL, NULL),
	(6, '2021-03-24 19:45:17', '2021-03-24 20:06:47', NULL, 0, 101, 0, '春兰', NULL, NULL),
	(7, '2021-03-24 19:47:00', '2021-03-24 20:06:54', NULL, 0, 109, 0, '蕙兰', NULL, NULL),
	(11, '2021-03-24 20:17:10', '2021-04-08 23:41:59', NULL, 0, 244, 105, '建兰', NULL, NULL),
	(12, '2021-03-24 20:17:25', '2021-03-24 20:17:25', NULL, 0, 245, 101, '春兰', NULL, NULL),
	(13, '2021-03-24 20:17:37', '2021-03-24 20:17:37', NULL, 0, 246, 109, '蕙兰', NULL, NULL),
	(15, '2021-04-13 08:11:36', '2021-04-13 08:11:36', NULL, 0, 268, 0, '兰花基质', NULL, NULL),
	(16, '2021-04-13 08:11:51', '2021-04-16 13:27:32', NULL, 0, 269, 268, '兰花基质', NULL, NULL),
	(18, '2021-04-13 08:12:32', '2021-04-13 08:12:32', NULL, 0, 271, 0, '兰花盆', NULL, NULL),
	(19, '2021-04-13 08:12:53', '2021-04-13 08:12:53', NULL, 0, 272, 0, '配件', NULL, NULL),
	(20, '2021-04-13 08:14:23', '2021-04-16 13:27:10', NULL, 0, 273, 271, '兰花盆', NULL, NULL),
	(23, '2021-04-13 08:15:04', '2021-04-13 08:15:04', NULL, 0, 276, 272, '配件', NULL, NULL);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;

-- 导出  表 shop.dict_config 结构
CREATE TABLE IF NOT EXISTS `dict_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `key` int(11) DEFAULT NULL,
  `keyStr` varchar(64) DEFAULT NULL,
  `value` varchar(128) DEFAULT NULL,
  `desc` varchar(512) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.dict_config 的数据：~5 rows (大约)
DELETE FROM `dict_config`;
/*!40000 ALTER TABLE `dict_config` DISABLE KEYS */;
INSERT INTO `dict_config` (`id`, `create_time`, `update_time`, `remark`, `status`, `key`, `keyStr`, `value`, `desc`, `name`) VALUES
	(1, '2021-05-08 17:04:49', '2021-05-08 17:15:12', NULL, 0, 1, NULL, '待付款', NULL, 'orderstatus'),
	(2, '2021-05-08 17:09:40', '2021-05-08 17:15:33', NULL, 0, 2, NULL, '待收货', NULL, 'orderstatus'),
	(3, '2021-05-08 17:11:13', '2021-05-08 17:15:59', NULL, 0, 3, NULL, '待评价', NULL, 'orderstatus'),
	(4, '2021-05-08 17:16:14', '2021-05-08 17:16:39', NULL, 0, 6, NULL, '订单完成', NULL, 'orderstatus'),
	(5, '2021-05-08 17:16:25', '2021-05-08 17:16:42', NULL, 0, 9, NULL, '订单关闭', NULL, 'orderstatus');
/*!40000 ALTER TABLE `dict_config` ENABLE KEYS */;

-- 导出  表 shop.haopin 结构
CREATE TABLE IF NOT EXISTS `haopin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `mobile` varchar(32) DEFAULT NULL,
  `orderid` varchar(64) DEFAULT NULL,
  `pictures` varchar(2048) DEFAULT NULL,
  `awardid` int(11) DEFAULT NULL,
  `award` varchar(1024) DEFAULT NULL,
  `zhifubao` varchar(128) DEFAULT NULL,
  `zhifubaoName` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  shop.haopin 的数据：~0 rows (大约)
DELETE FROM `haopin`;
/*!40000 ALTER TABLE `haopin` DISABLE KEYS */;
/*!40000 ALTER TABLE `haopin` ENABLE KEYS */;

-- 导出  表 shop.images 结构
CREATE TABLE IF NOT EXISTS `images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  `yongtu` varchar(512) DEFAULT NULL,
  `pic` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.images 的数据：~8 rows (大约)
DELETE FROM `images`;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `url`, `yongtu`, `pic`) VALUES
	(1, '2019-09-25 23:24:27', '2021-05-13 08:25:27', NULL, 0, 'banner', '/pages/product/list', '轮播图', 'http://admin.heshihuan.cn/fileServer/common/branner.jpg'),
	(2, '2019-09-25 23:26:25', '2021-03-31 17:50:00', NULL, 0, '图片2', 'www.google.com', '测试', ',https://pyshop.oss-cn-beijing.aliyuncs.com/produc'),
	(4, '2019-10-09 10:50:07', '2021-03-31 17:50:12', NULL, 0, 'ada', 'www.yahoo.com', 'sdfas', ',https://pyshop.oss-cn-beijing.aliyuncs.com/produc'),
	(5, '2021-05-07 08:02:29', '2021-05-13 08:25:35', NULL, 0, 'banner', '/pages/product/list', NULL, 'http://admin.heshihuan.cn/fileServer/common/brannder2.jpg'),
	(6, '2021-05-07 08:03:02', '2021-05-12 08:11:38', NULL, 0, 'banner-t', NULL, NULL, 'http://admin.heshihuan.cn/fileServer/common/banner4.jpg'),
	(7, '2021-05-07 09:45:40', '2021-05-13 08:25:39', NULL, 0, 'ad', '/pages/product/list', '广告图', 'http://admin.heshihuan.cn/fileServer/common/ad1.jpg'),
	(8, '2021-05-12 08:14:53', '2021-05-12 08:16:30', NULL, 0, 'ad-t', 'www.baidu.com', '广告图', 'http://admin.heshihuan.cn/fileServer/common/ad2.jpg'),
	(9, '2021-05-20 13:58:08', '2021-05-20 13:58:46', NULL, 0, 'company_banner', NULL, '轮播图', '公司网站轮播图');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;

-- 导出  表 shop.net_other_bussiness 结构
CREATE TABLE IF NOT EXISTS `net_other_bussiness` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `title` varchar(512) DEFAULT NULL,
  `categoryId` int(11) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  `desc` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net_other_bussiness 的数据：~2 rows (大约)
DELETE FROM `net_other_bussiness`;
/*!40000 ALTER TABLE `net_other_bussiness` DISABLE KEYS */;
INSERT INTO `net_other_bussiness` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `title`, `categoryId`, `url`, `pic`, `desc`) VALUES
	(1, '2021-06-01 20:59:07', '2021-06-20 16:35:42', NULL, 0, '中华橱柜网', '中华橱柜网是一家专业从事互联网信息服务业应用软件开发的高新企业，                             目前已发展成为国内橱柜行业垂直专业网站开发商。                         ', 1, 'index.html', '202106201635417573.jpg', ''),
	(2, '2021-06-01 21:00:50', '2021-06-01 21:00:50', NULL, 0, '塑料花盆', '塑料花盆塑料花盆塑料花盆塑料花盆塑料花盆塑料花盆塑料花盆', 2, 'index.html', '202106012100498548.jpg', '');
/*!40000 ALTER TABLE `net_other_bussiness` ENABLE KEYS */;

-- 导出  表 shop.net_product 结构
CREATE TABLE IF NOT EXISTS `net_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `categoryId` int(11) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  `desc` varchar(2048) DEFAULT NULL,
  `style` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net_product 的数据：~0 rows (大约)
DELETE FROM `net_product`;
/*!40000 ALTER TABLE `net_product` DISABLE KEYS */;
INSERT INTO `net_product` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `title`, `categoryId`, `pic`, `desc`, `style`) VALUES
	(1, '2021-05-31 13:14:03', '2021-06-01 12:39:53', NULL, 0, '衣帽柜', '简约版本', 2, '202105311314415645.jpg', '<h2>产品参数</h2>\r\n\r\n<p><strong>企业使命:</strong>为消费者提供高品质家居生活整体决方案</p>\r\n\r\n<p><br />\r\n<strong>企业原景:</strong>致力于成为柔性定制家居领域领导品牌</p>\r\n\r\n<p><br />\r\n<strong>公司价值观</strong>:勇于承担责任,以敬畏之心服务户,以无畏之心超越自我,感恩奉献,正直守信</p>\r\n\r\n<p><br />\r\n<strong>企业理念:</strong>以用户需求为导向,坚持品质卓越,服务创新,实现企业持续发展</p>\r\n\r\n<p><br />\r\n<strong>企业精神:</strong>传承匠心精神,勤谨敬业,追求品质卓越,精益求精马克森行为准则</p>\r\n\r\n<p><br />\r\n第一条顾客利益至高无上<br />\r\n第二条:服务为本,一切以顾需求为中心<br />\r\n第三条:细节为王!追求产品极致的决心不可动摇<br />\r\n第四条:创新为赢,永远站在行业的最前沿<br />\r\n第五条:合作共生,所有合作伙件的利益就是我们的益<br />\r\n第六条:协同创适,群体的价值比个体价值的忘和还要高<br />\r\n企业责任:创造和谐人居环填,而社服务大众</p>\r\n\r\n<p><br />\r\n<strong>企业责任:创造和谐人居环境,贡献社会,服务大众</strong></p>\r\n', '简约版本');
/*!40000 ALTER TABLE `net_product` ENABLE KEYS */;

-- 导出  表 shop.net__category 结构
CREATE TABLE IF NOT EXISTS `net__category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `keyid` int(11) DEFAULT NULL,
  `keyname` varchar(128) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__category 的数据：~0 rows (大约)
DELETE FROM `net__category`;
/*!40000 ALTER TABLE `net__category` DISABLE KEYS */;
INSERT INTO `net__category` (`id`, `create_time`, `update_time`, `remark`, `status`, `keyid`, `keyname`, `pid`, `type`) VALUES
	(1, '2020-01-03 09:49:49', '2020-01-03 09:49:49', NULL, 0, 0, '类别1', 0, 0);
/*!40000 ALTER TABLE `net__category` ENABLE KEYS */;

-- 导出  表 shop.net__company_info 结构
CREATE TABLE IF NOT EXISTS `net__company_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `introduce` varchar(2048) DEFAULT NULL,
  `culture` varchar(2048) DEFAULT NULL,
  `yongtuCompany` varchar(512) DEFAULT NULL,
  `yongtuculture` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__company_info 的数据：~1 rows (大约)
DELETE FROM `net__company_info`;
/*!40000 ALTER TABLE `net__company_info` DISABLE KEYS */;
INSERT INTO `net__company_info` (`id`, `create_time`, `update_time`, `remark`, `status`, `introduce`, `culture`, `yongtuCompany`, `yongtuculture`) VALUES
	(1, '2020-01-01 11:20:15', '2021-05-28 08:28:01', NULL, -2, '<h2>马克森简介</h2>\r\n\r\n<p><strong>马克森木业（滁州）</strong></p>\r\n<p><strong>有限公司</strong>，全屋臻定制创导者，国内首家推出&ldquo;柔性定制5.0系统&rdquo;的大型木业企业。公司成立于1996年，先后投资4.7亿元，拥有130亩现代化智能生产基地。马克森木业率先在行业内实现产业升级，重金打造国内领先的全屋臻定制&ldquo;柔性生产服务系统&rdquo;。从德国原装引进豪迈生产设备，并花巨资开发数字化柔性定制管理系统，实现从销售到生产的数据化管理，马克森&ldquo;柔性定制5.0系统&rdquo;，先后荣获多项国际专利，开创式的全屋臻定制解决方案引领行业发展方向。 马克森&ldquo;坚持多思考30%的定制细节&rdquo;服务理念，20年匠心品质，先后荣获&ldquo;中国橱柜十大品牌&rdquo;、&ldquo;中国衣柜十大品牌&rdquo;、&ldquo;全国十佳放心地板&rdquo;、&ldquo;安徽名牌产品&rdquo;、&ldquo;安徽省诚信企业&rdquo;、&ldquo;安徽省高新技术企业&rdquo;等殊荣。先后通过&ldquo;中国环境标志十环认证&rdquo;、&ldquo;欧盟CE认证&rdquo;、&ldquo; ISO9001质量管理体系认证&rdquo;、&ldquo; ISO14001环境体系认证&rdquo;等国内国际专业机构认证，在国内外市场拥有较高的市场影响力。</p>\r\n', '<h2>企业文化</h2>\r\n\r\n<p><strong>企业使命:</strong>为消费者提供高品质家居生活整体决方案<br />\r\n<strong>企业原景:</strong>致力于成为柔性定制家居领域领导品牌<br />\r\n<strong>公司价值观</strong>:勇于承担责任,以敬畏之心服务户,以无畏之心超越自我,感恩奉献,正直守信<br />\r\n<strong>企业理念:</strong>以用户需求为导向,坚持品质卓越,服务创新,实现企业持续发展<br />\r\n<strong>企业精神:</strong>传承匠心精神,勤谨敬业,追求品质卓越,精益求精马克森行为准则<br />\r\n第一条顾客利益至高无上<br />\r\n第二条:服务为本,一切以顾需求为中心<br />\r\n第三条:细节为王!追求产品极致的决心不可动摇<br />\r\n第四条:创新为赢,永远站在行业的最前沿<br />\r\n第五条:合作共生,所有合作伙件的利益就是我们的益<br />\r\n第六条:协同创适,群体的价值比个体价值的忘和还要高<br />\r\n企业责任:创造和谐人居环填,而社服务大众<br />\r\n<strong>企业责任:创造和谐人居环境,贡献社会,服务大众</strong></p>\r\n', '202105201755491530.jpg', '202105201755505361.jpg');
/*!40000 ALTER TABLE `net__company_info` ENABLE KEYS */;

-- 导出  表 shop.net__contact 结构
CREATE TABLE IF NOT EXISTS `net__contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  `zh_company` varchar(521) DEFAULT NULL,
  `en_company` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `kf_phone` varchar(128) DEFAULT NULL,
  `mobilephone` varchar(128) DEFAULT NULL,
  `x` varchar(32) DEFAULT NULL,
  `y` varchar(32) DEFAULT NULL,
  `logo` varchar(256) DEFAULT NULL,
  `weixin` varchar(256) DEFAULT NULL,
  `province` varchar(32) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__contact 的数据：~1 rows (大约)
DELETE FROM `net__contact`;
/*!40000 ALTER TABLE `net__contact` DISABLE KEYS */;
INSERT INTO `net__contact` (`id`, `create_time`, `update_time`, `remark`, `status`, `pic`, `zh_company`, `en_company`, `email`, `phone`, `kf_phone`, `mobilephone`, `x`, `y`, `logo`, `weixin`, `province`, `city`, `address`) VALUES
	(1, '2021-05-24 14:24:32', '2021-05-26 08:52:16', NULL, 0, '2', '华东生产基地:马克森木业(滁州)有限公司', 'MUCHSEE WOOD( CHUZHOU ) CO.,LTD', '370377860@qq.com', '400-801-6666', '0596-7670702', NULL, NULL, NULL, '202105260852152922.png', '202105260852152245.jpg', '福建', '厦门', '滁州市经济技术开发区花山东路1999号');
/*!40000 ALTER TABLE `net__contact` ENABLE KEYS */;

-- 导出  表 shop.net__honour 结构
CREATE TABLE IF NOT EXISTS `net__honour` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `time` varchar(128) DEFAULT NULL,
  `content` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__honour 的数据：~8 rows (大约)
DELETE FROM `net__honour`;
/*!40000 ALTER TABLE `net__honour` DISABLE KEYS */;
INSERT INTO `net__honour` (`id`, `create_time`, `update_time`, `remark`, `status`, `time`, `content`) VALUES
	(1, '2020-01-03 09:33:24', '2021-05-21 09:06:20', NULL, 0, '2005年9月17日', '“马克森地板”荣获中国林产工业协会颁发的“中国地板行业市场影响力”优秀品牌'),
	(2, '2021-05-21 09:06:32', '2021-05-21 09:06:43', NULL, 0, '2007年9月17日', '“马克森地板”荣获中国林产工业协会颁发的“中国地板行业市场影响力”优秀品牌'),
	(3, '2021-05-21 09:06:49', '2021-05-21 09:07:04', NULL, 0, '2009年8月14日', '安徽省质量技术监督局、安徽省名牌战略推进委员会授与“马克森牌”地板“安徽名牌产品”称号'),
	(4, '2021-05-21 09:43:50', '2021-05-21 09:44:07', NULL, 0, '2011年4月15日', '安徽省工商行政管理局授予马克森牌强化木地板“安徽省著名商标”荣誉称号'),
	(5, '2021-05-21 09:44:15', '2021-05-21 09:44:42', NULL, 0, '2013年8月27日', '荣获滁州市“重合同守信用明星企业”殊荣'),
	(6, '2021-05-21 09:44:43', '2021-05-21 09:44:55', NULL, 0, '2015年7月05日', '春洲集团推出第一代锁扣免胶地板，被业内专家誉为地板科技 “明日之星”'),
	(7, '2021-05-21 09:44:56', '2021-05-21 09:45:07', NULL, 0, '2016年9月12日', '荣获安徽省技术监督局颁发 “安徽省质量奖”荣誉称号'),
	(8, '2021-05-21 09:45:08', '2021-05-21 09:45:22', NULL, 0, '2017年2月27日', '通过GB/T19001-2008/ISO9001：2008质量管理体系认证；');
/*!40000 ALTER TABLE `net__honour` ENABLE KEYS */;

-- 导出  表 shop.net__index 结构
CREATE TABLE IF NOT EXISTS `net__index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `brand` varchar(2048) DEFAULT NULL,
  `brandImage` varchar(2048) DEFAULT NULL,
  `culture` varchar(2048) DEFAULT NULL,
  `cultureImage` varchar(512) DEFAULT NULL,
  `progress` varchar(512) DEFAULT NULL,
  `progressImage` varchar(512) DEFAULT NULL,
  `footer` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__index 的数据：~1 rows (大约)
DELETE FROM `net__index`;
/*!40000 ALTER TABLE `net__index` DISABLE KEYS */;
INSERT INTO `net__index` (`id`, `create_time`, `update_time`, `remark`, `status`, `brand`, `brandImage`, `culture`, `cultureImage`, `progress`, `progressImage`, `footer`) VALUES
	(1, '2021-05-29 12:53:42', '2021-06-20 13:32:44', NULL, 0, '<h3><a href="profuile.html">马克2森木业（滁州）有限公司</a></h3>\r\n<!--公司介绍-->\r\n\r\n<p>马克森木业（滁州）有限公司，全屋臻定制创导者，国内首家推出&ldquo;柔性定制5.0系统&rdquo;的大型木业企业。公司成立于1996年，先后投资4.7亿元， 拥有130亩现代化智能生产基地。马克森木业率先在行业内实现产业升级，重金打造国内领先的全屋臻定制&ldquo;柔性生产服务系统&rdquo;。从德国原装引进豪迈生产设备，并花巨资开发数字化柔性定制管理系统， 实现从销售到生产的数据化管理，马克森&ldquo;柔性定制5.0系统&rdquo;，先后荣获多项国际专利，开创式的全屋臻定制解决方案引领行业发展方向。</p>\r\n\r\n<p>马克森&ldquo;坚持多思考30%的定制细节&rdquo;服务理念，20年匠心品质，先后荣获&ldquo;中国橱柜十大品牌&rdquo;、&ldquo;中国衣柜十大品牌&rdquo;、&ldquo;全国十佳放心地板&rdquo;、&ldquo;安徽名牌产品&rdquo;、&ldquo;安徽省诚信企业&rdquo;、&ldquo;安徽省高新技术企业&rdquo;等殊荣。先后通过 &ldquo;中国环境标志十环认证&rdquo;、&ldquo;欧盟CE认证&rdquo;、&ldquo; ISO9001质量管理体系认证&rdquo;、&ldquo; ISO14001环境体系认证&rdquo;等国内国际专业机构认证，在国内外市场拥有较高的市场影响力。</p>\r\n', '202105300928577694.jpg', '<h3><a href="about.html">马克森文化</a></h3>\r\n\r\n<p><a href=""><img alt="" src="http://0.rc.xiniu.com/g2/M00/34/AB/CgAGfFoKPCuAOg6xAATVqYkvkT8424.jpg" /></a></p>\r\n\r\n<p>企业使命:为消费者提供高品质家居生活整体解决方案</p>\r\n\r\n<p>企业愿景:致力于成为柔性定制家居领域领导品牌</p>\r\n\r\n<p>企业理念:以用户需求为导向，坚持品质卓越，服务创新，实现企业持续发展</p>\r\n\r\n<p>企业精神：传承匠心精神，勤谨敬业，追求品质卓越，精益求精</p>\r\n\r\n<p>付出是收获：一份耕耘，一份收获。</p>\r\n\r\n<p>...</p>\r\n', '2', '<h3><a href="about.html">马克森历程</a></h3>\r\n\r\n<ul>\r\n	<li>1996年 王春洲先生在响应香港回归祖国的号召，在中国大陆投资2.3亿成立&ldquo;马克森集团&rdquo;，投资兴建大型地板生产基地和木制品研发中心。</li>\r\n	<li>2000年 &ldquo;春洲奥德&rdquo;地板启动国内销售渠道，并迅速占领北京、上海、西安、南京、郑州等一线市场。</li>\r\n	<li>2003年 年首批获得ISO9001：2000质量管理体系认证，推出静音安眠缓冲地板，开启静音地板先河，并成功打入俄罗斯市场。</li>\r\n	<li>2006年 安徽省工商行政管理局授予马克森牌强化木地板&ldquo;安徽省著名商标&rdquo;荣誉称号</li>\r\n</ul>\r\n', NULL, '<footer style="margin-top: 0;" id="footer">	<div class="footer-top link">	    <!--友情链接-->	    <div class="container">	        友情链接：	        <a href="http://www.jomoo.com.cn/">马克森英文网</a>	        <a href="http://www.jieju.cn/">智能家居</a>	        <a href="http://www.chinaweiyu.com/">中华橱柜网</a>	        <a href="http://www.wyw.cn/">中厨网</a>	        <a href="http://www.wyw.cn/">优信二手车</a>	        <a href="http://www.wyw.cn/">落阳地产</a>	        <a href="http://www.hegii.com/">汽车之家</a>	        <a href="https://shop68294732.taobao.com/?spm=a230r.7195193.1997079397.204.cYt8e7">马克森天猫商城</a>	    </div>	</div>	<!--备案号-->	<div class="footer-button">	    <div class="container">	        <p>服务热线：13774514086 在线QQ：370377860</p>	        <p>增值电信业务经营许可证：湘B2-20100052 福建径里农业发展公司 | 闽ICP备15045692号 | 售后服务热线: 13774514086</p>	        <!--百度分享-->	        <div class="bdsharebuttonbox">	            <a href="#" class="bds_more" data-cmd="more"></a>	            <a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a>	            <a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>	            <a href="#" class="bds_renren" data-cmd="renren" title="分享到人人网"></a>	            <a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>	        </div>	    </div>	</div> \r\n</footer>');
/*!40000 ALTER TABLE `net__index` ENABLE KEYS */;

-- 导出  表 shop.net__index__images 结构
CREATE TABLE IF NOT EXISTS `net__index__images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  `yongtu` varchar(512) DEFAULT NULL,
  `pic` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__index__images 的数据：~2 rows (大约)
DELETE FROM `net__index__images`;
/*!40000 ALTER TABLE `net__index__images` DISABLE KEYS */;
INSERT INTO `net__index__images` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `url`, `yongtu`, `pic`) VALUES
	(1, '2021-05-29 14:04:54', '2021-05-30 00:10:09', NULL, 0, 'banner', 'www.baidu.com', '首页轮播', '202105300010086113.png'),
	(2, '2021-05-30 00:10:31', '2021-05-30 00:10:31', NULL, 0, 'banner', 'www.baid.com', '首页轮播图', '202105300010301646.png');
/*!40000 ALTER TABLE `net__index__images` ENABLE KEYS */;

-- 导出  表 shop.net__join 结构
CREATE TABLE IF NOT EXISTS `net__join` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `mobile` varchar(521) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `condition` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__join 的数据：~5 rows (大约)
DELETE FROM `net__join`;
/*!40000 ALTER TABLE `net__join` DISABLE KEYS */;
INSERT INTO `net__join` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `mobile`, `email`, `condition`) VALUES
	(1, '2021-06-03 08:06:10', '2021-06-03 08:06:10', NULL, 0, NULL, NULL, 'q@qq.comadvice=2', NULL),
	(2, '2021-06-03 08:09:54', '2021-06-03 08:09:54', NULL, 0, 'a', '13774514086', 'ww@qq.comcondition=2', NULL),
	(3, '2021-06-03 08:11:26', '2021-06-03 08:11:26', NULL, 0, 'as', '13774514086', 'q@aa.comcondition=bbb', NULL),
	(4, '2021-06-03 16:17:37', '2021-06-03 16:17:37', NULL, 0, 'a', '13774514086', 'ww@qq.comcondition=2', NULL),
	(5, '2021-06-03 17:10:01', '2021-06-03 17:10:01', NULL, 0, 'a', '13774514086', 'ww@qq.comcondition=2', NULL);
/*!40000 ALTER TABLE `net__join` ENABLE KEYS */;

-- 导出  表 shop.net__join__page 结构
CREATE TABLE IF NOT EXISTS `net__join__page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `banner` varchar(512) DEFAULT NULL,
  `market_left` varchar(521) DEFAULT NULL,
  `market_rigth` varchar(521) DEFAULT NULL,
  `qiye_left` varchar(512) DEFAULT NULL,
  `qiye_right` varchar(512) DEFAULT NULL,
  `zhaoshang_left` varchar(512) DEFAULT NULL,
  `zhaoshang_center` varchar(512) DEFAULT NULL,
  `zhaoshang_right` varchar(512) DEFAULT NULL,
  `join_left` varchar(512) DEFAULT NULL,
  `join_right` varchar(512) DEFAULT NULL,
  `product_left` varchar(512) DEFAULT NULL,
  `product_right` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__join__page 的数据：~1 rows (大约)
DELETE FROM `net__join__page`;
/*!40000 ALTER TABLE `net__join__page` DISABLE KEYS */;
INSERT INTO `net__join__page` (`id`, `create_time`, `update_time`, `remark`, `status`, `banner`, `market_left`, `market_rigth`, `qiye_left`, `qiye_right`, `zhaoshang_left`, `zhaoshang_center`, `zhaoshang_right`, `join_left`, `join_right`, `product_left`, `product_right`) VALUES
	(1, '2021-05-30 10:07:43', '2021-05-30 10:37:17', NULL, 0, '202105301007429483.jpg', '<img src="img/join/main-1_03.gif" alt="">\r\n                <h5>市场分析：</h5>\r\n                <p>\r\n                    中国的政治经济环境稳定，使得中国房地产业发展，进而强力地拉动了橱柜行业高速发展。\r\n                    中国经济发展的成效体现在消费者购买力上，消费者购买力水平不断提高。目前建材领域的多个行业正面临“洗牌”，如地板行业，家具行业。陶瓷橱柜正经历这样的过程。\r\n                    国内产品“根基不稳”。许多企业都是着重于产品质量和营销渠道。虽设计已不逊于国外品牌。但是品牌意识不足，在品牌宣传和自身形象提升上还较为薄弱。\r\n                </p>', '<img src="img/join/main-2_05.gif" alt="">', '<img src="img/join/main-2le_10_01.gif" alt="">\r\n                <h5>企业介绍：</h5>\r\n                <p>\r\n                    滁州马克森有限公司是一家集设计、研发、生产、销售于一体的综合性专业制造橱柜的企业。\r\n                    公司拥有精准的橱柜生产线、科学的木板生产线和国内先进的环保无尘油漆房、标准亚克力座便器生产线、淋浴屏风生产线(广东中山分公司)、五金龙头、挂件生产线(广东开平分公司)。\r\n                </p>', ' <img src="img/join/main-2rig_10.gif" alt="">', '<img src="img/join/main-3le1_13.gif" alt="">\r\n                <img src="img/join/main-3le2_13.gif" alt="">', '<h5>店面筹备期：</h5>\r\n                <p>市场调研的指导、实地考察、店址评估、投资分析。</p>\r\n                <h5>店面运营期：</h5>\r\n                <p>组织形象策划、营销策略支持、平面与展示支持；</p>\r\n                <p>完善的售后体系支持；</p>\r\n                <p>科学的物流支持；</p>\r\n                <p>大型活动支持。</p>\r\n                <h5>售后无忧计划：</h5>\r\n                <p>快速反应：公司专门有外出售后解决专员；\r\n                </p><p>即时解决：对于大部分售后问题，现场鉴定，现场解决；</p>\r\n                <p>先行赔付：对于部分紧急售后处理，提供先行提供配件。</p>', '<img src="img/join/main-3righ_14.gif" alt="">', '<img src="img/join/main-4le_19.gif" alt="">', '<img src="img/join/main-4righ_22.gif" alt="">\r\n                <h4>加盟条件</h4>\r\n                <p>\r\n\r\n                    橱柜、建材行业的操作者;当地市场的知名人士;有志于在建材、家具行业发展的成功人士。\r\n                    战略合作方式：城市区域代理制\r\n                    欢迎有志于建材行业的人士加入尚高大家庭，共谋双赢!\r\n                    国内代理经销条件\r\n                    地区范围：中国大陆指定区域\r\n                    1.认同尚高品牌文化，具有工作热忱的公民;\r\n                    2.身体健康，信用良好，注重互动关系，善于沟通;\r\n                    3.在当地有较强的人脉关系和市场运作能力;\r\n                    4.资金实力较雄厚，有一定行业从业经验;\r\n                    5.有较好的', '<img src="img/join/main-5lr_27.gif" alt="">', '<img src="img/join/main-5rig_29.gif" alt="">');
/*!40000 ALTER TABLE `net__join__page` ENABLE KEYS */;

-- 导出  表 shop.net__message_board 结构
CREATE TABLE IF NOT EXISTS `net__message_board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `mobile` varchar(521) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `advice` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__message_board 的数据：~2 rows (大约)
DELETE FROM `net__message_board`;
/*!40000 ALTER TABLE `net__message_board` DISABLE KEYS */;
INSERT INTO `net__message_board` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `mobile`, `email`, `advice`) VALUES
	(1, '2021-05-24 17:06:13', '2021-05-24 17:06:17', NULL, 0, '333', NULL, NULL, NULL),
	(2, '2021-05-27 08:11:25', '2021-05-27 08:11:25', NULL, 0, NULL, NULL, '2@qq.comadvice=2', NULL);
/*!40000 ALTER TABLE `net__message_board` ENABLE KEYS */;

-- 导出  表 shop.net__news 结构
CREATE TABLE IF NOT EXISTS `net__news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `date` varchar(128) DEFAULT NULL,
  `content` varchar(1024) DEFAULT NULL,
  `author` varchar(512) DEFAULT NULL,
  `pic` varchar(256) DEFAULT NULL,
  `category` tinyint(4) DEFAULT NULL,
  `introduction` varchar(1024) DEFAULT NULL,
  `index` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__news 的数据：~1 rows (大约)
DELETE FROM `net__news`;
/*!40000 ALTER TABLE `net__news` DISABLE KEYS */;
INSERT INTO `net__news` (`id`, `create_time`, `update_time`, `remark`, `status`, `title`, `date`, `content`, `author`, `pic`, `category`, `introduction`, `index`) VALUES
	(1, '2020-01-03 09:19:18', '2021-06-01 13:32:03', NULL, 0, '筑梦启航|2018马克森全屋臻定制合肥运营中心年会圆满结束', '2017-06-14', '<p>&nbsp;</p>\r\n\r\n<h2>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 秘鲁修正新冠病例统计数据后，人均死亡率全球最高</h2>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&emsp;&emsp;南美洲国家秘鲁5月31日对其累计新冠死亡病例数据做出修正，从原来的69342人上调至180764人，这使该国成为人均新冠死亡率最高的国家。</p>\r\n\r\n<p>&nbsp;近几个月来，秘鲁新冠感染者面临氧气短缺困境。人民视觉 &nbsp;资料图近几个月来，秘鲁新冠感染者面临氧气短缺困境。人民视觉 &nbsp;资料图</p>\r\n\r\n<p>&emsp;&emsp;据法新社报道，秘鲁政府在咨询卫生专家团的意见后，发现有大量未被纳入统计的新冠死亡病例数据。经调整后，秘鲁现在是世界上人均新冠死亡率最高的国家，</p>\r\n\r\n<p>&emsp;&emsp;每100万居民中就有5484人死于新冠。</p>\r\n\r\n<p>&emsp;&emsp;据悉，秘鲁总人口约3300万，据此前的数据显示，秘鲁每100万居民有2103人因感染新冠去世，位居第13位。</p>\r\n\r\n<p>&emsp;&emsp;法新社援引专家团报告指出，此前采用的统计方法低估了新冠死亡人数。而现有的方法不仅包括新冠病毒检测呈阳性的人，还考虑到了&ldquo;与确诊病例有流行病学联系&rdquo;的&ldquo;潜在&rdquo;病例。</p>\r\n\r\n<p>&emsp;&emsp;据美国约翰斯&middot;霍普金斯大学统计数据显示，截至当地时间5月31日，秘鲁累计新冠确诊人数已超过194万例。近几个月来，新冠感染者面临氧气短缺困境。</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>点击进入专题：</p>\r\n\r\n<p>全球多国爆发新冠肺炎疫情</p>\r\n\r\n<p>责任编辑：武晓东 SN241</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n', '作者', '202105302324393198.jpg', 2, '<p>南美洲国家秘鲁5月31日对其累计新冠死亡病例数据做出修正，从原来的69342人上调至180764人，这使该国成为人均新冠死亡率最高的国家</p>\r\n', 1);
/*!40000 ALTER TABLE `net__news` ENABLE KEYS */;

-- 导出  表 shop.net__news__category 结构
CREATE TABLE IF NOT EXISTS `net__news__category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__news__category 的数据：~3 rows (大约)
DELETE FROM `net__news__category`;
/*!40000 ALTER TABLE `net__news__category` DISABLE KEYS */;
INSERT INTO `net__news__category` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `desc`) VALUES
	(1, '2021-05-30 22:36:12', '2021-05-30 22:36:12', NULL, 0, '法标资讯', NULL),
	(2, '2021-05-30 22:41:15', '2021-06-17 13:50:34', NULL, 0, '产品资讯3', NULL),
	(3, '2021-05-30 22:45:33', '2021-05-30 23:10:08', NULL, 0, '媒体来访', NULL);
/*!40000 ALTER TABLE `net__news__category` ENABLE KEYS */;

-- 导出  表 shop.net__product_info 结构
CREATE TABLE IF NOT EXISTS `net__product_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `title` varchar(1024) DEFAULT NULL,
  `picture` varchar(512) DEFAULT NULL,
  `buy_url` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__product_info 的数据：~0 rows (大约)
DELETE FROM `net__product_info`;
/*!40000 ALTER TABLE `net__product_info` DISABLE KEYS */;
INSERT INTO `net__product_info` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `title`, `picture`, `buy_url`) VALUES
	(1, '2020-01-03 09:41:09', '2020-01-03 09:41:09', NULL, 0, '产品', '标题', ',https://pyshop.oss-cn-beijing.aliyuncs.com/product/202001030941088072.jpg', 'www.baidu.com');
/*!40000 ALTER TABLE `net__product_info` ENABLE KEYS */;

-- 导出  表 shop.net__product__category__child 结构
CREATE TABLE IF NOT EXISTS `net__product__category__child` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  `parentId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__product__category__child 的数据：~4 rows (大约)
DELETE FROM `net__product__category__child`;
/*!40000 ALTER TABLE `net__product__category__child` DISABLE KEYS */;
INSERT INTO `net__product__category__child` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `desc`, `parentId`) VALUES
	(1, '2021-05-31 13:12:07', '2021-05-31 13:12:07', NULL, 0, '格力衣柜', NULL, 1),
	(2, '2021-05-31 13:12:14', '2021-05-31 13:12:14', NULL, 0, '美的衣柜', NULL, 1),
	(3, '2021-05-31 13:12:31', '2021-05-31 13:12:31', NULL, 0, '正方形桌子', NULL, 2),
	(4, '2021-05-31 13:12:49', '2021-05-31 13:12:49', NULL, 0, '八脚桌', NULL, 2);
/*!40000 ALTER TABLE `net__product__category__child` ENABLE KEYS */;

-- 导出  表 shop.net__product__category__parent 结构
CREATE TABLE IF NOT EXISTS `net__product__category__parent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__product__category__parent 的数据：~2 rows (大约)
DELETE FROM `net__product__category__parent`;
/*!40000 ALTER TABLE `net__product__category__parent` DISABLE KEYS */;
INSERT INTO `net__product__category__parent` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `desc`) VALUES
	(1, '2021-05-31 13:11:39', '2021-05-31 13:11:39', NULL, 0, '衣柜', NULL),
	(2, '2021-05-31 13:11:46', '2021-05-31 13:11:46', NULL, 0, '桌子', NULL);
/*!40000 ALTER TABLE `net__product__category__parent` ENABLE KEYS */;

-- 导出  表 shop.net__product__style 结构
CREATE TABLE IF NOT EXISTS `net__product__style` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `desc` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  shop.net__product__style 的数据：~0 rows (大约)
DELETE FROM `net__product__style`;
/*!40000 ALTER TABLE `net__product__style` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__product__style` ENABLE KEYS */;

-- 导出  表 shop.order 结构
CREATE TABLE IF NOT EXISTS `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `addressId` int(11) DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `mobile` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `area` varchar(64) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `pruductPriceCount` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `yunfei` float DEFAULT NULL,
  `orderRemark` varchar(1024) DEFAULT NULL,
  `mount` float DEFAULT NULL,
  `orderStatus` int(255) DEFAULT '0',
  `orderNo` varchar(128) DEFAULT NULL,
  `logisticsNo` varchar(64) DEFAULT NULL,
  `orderChangeStatus` int(11) DEFAULT '0',
  `needHelp` int(11) DEFAULT '0',
  `logisticsType` int(11) DEFAULT '99',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=717 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.order 的数据：~312 rows (大约)
DELETE FROM `order`;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` (`id`, `create_time`, `update_time`, `remark`, `status`, `addressId`, `receiver`, `mobile`, `address`, `area`, `userid`, `pruductPriceCount`, `discount`, `yunfei`, `orderRemark`, `mount`, `orderStatus`, `orderNo`, `logisticsNo`, `orderChangeStatus`, `needHelp`, `logisticsType`) VALUES
	(405, '2021-03-06 22:26:11', '2021-07-12 19:55:33', NULL, 0, NULL, NULL, NULL, NULL, NULL, 24, 12, NULL, NULL, '""', 90, 5, '20210306222610', '5467', 0, 0, 4),
	(714, '2021-07-15 13:36:53', '2021-07-15 13:38:52', NULL, 0, 695, NULL, NULL, NULL, NULL, 146, NULL, NULL, NULL, '""', 16, 2, '20210715133653', NULL, 0, 0, NULL),
	(715, '2021-08-16 21:27:40', '2021-08-16 21:27:40', NULL, 0, 733, NULL, NULL, NULL, NULL, 258, NULL, NULL, NULL, '""', 121, 1, '20210816212739', NULL, 0, 0, NULL),
	(716, '2021-10-14 22:06:21', '2021-10-14 22:06:21', NULL, 0, 736, NULL, NULL, NULL, NULL, 333, NULL, NULL, NULL, '""', 121, 1, '20211014220620', NULL, 0, 0, NULL);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;

-- 导出  视图 shop.order_v 结构
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `order_v` (
	`id` INT(11) NOT NULL,
	`userid` INT(11) NULL,
	`addressId` INT(11) NULL,
	`create_time` DATETIME NULL,
	`update_time` DATETIME NULL,
	`pruductPriceCount` FLOAT NULL,
	`discount` FLOAT NULL,
	`yunfei` FLOAT NULL,
	`status` INT(11) NULL,
	`remark` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`orderRemark` VARCHAR(1024) NULL COLLATE 'utf8_general_ci',
	`orderChangeStatus` INT(11) NULL,
	`orderStatus` INT(255) NULL,
	`mount` FLOAT NULL,
	`orderNo` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`logisticsNo` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`needHelp` INT(11) NULL,
	`logisticsType` INT(11) NULL,
	`name` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`username` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`nickname` VARCHAR(255) NULL COLLATE 'utf8_general_ci',
	`mobile` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`receiver` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`address` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`area` VARCHAR(64) NULL COLLATE 'utf8_general_ci'
) ENGINE=MyISAM;

-- 导出  表 shop.pay_record 结构
CREATE TABLE IF NOT EXISTS `pay_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `tradeNo` varchar(64) DEFAULT NULL,
  `totalFee` varchar(64) DEFAULT NULL,
  `transactionId` varchar(64) DEFAULT NULL,
  `attach` varchar(64) DEFAULT NULL,
  `returnstring` varchar(4086) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=283 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.pay_record 的数据：~24 rows (大约)
DELETE FROM `pay_record`;
/*!40000 ALTER TABLE `pay_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay_record` ENABLE KEYS */;

-- 导出  表 shop.product 结构
CREATE TABLE IF NOT EXISTS `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `image800` varchar(512) DEFAULT NULL,
  `image400` varchar(512) DEFAULT NULL,
  `image200` varchar(512) DEFAULT NULL,
  `image100` varchar(512) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `sales` int(11) DEFAULT NULL,
  `store` int(11) DEFAULT NULL,
  `detail` varchar(2048) DEFAULT NULL,
  `size` varchar(64) DEFAULT NULL,
  `color` varchar(64) DEFAULT NULL,
  `category` varchar(16) DEFAULT NULL,
  `main_image` varchar(4096) DEFAULT NULL,
  `detail_image` varchar(4096) DEFAULT NULL,
  `orderId` int(10) unsigned DEFAULT '0',
  `brownCount` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `productid` int(10) unsigned DEFAULT NULL,
  `propid` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=693 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.product 的数据：~12 rows (大约)
DELETE FROM `product`;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` (`id`, `create_time`, `update_time`, `remark`, `status`, `title`, `image800`, `image400`, `image200`, `image100`, `price`, `sales`, `store`, `detail`, `size`, `color`, `category`, `main_image`, `detail_image`, `orderId`, `brownCount`, `number`, `productid`, `propid`) VALUES
	(6, NULL, '2021-05-22 08:59:27', NULL, 0, '兰花 富山奇蝶 建兰', NULL, NULL, NULL, NULL, 100, 61, 100, NULL, '不含盆', '一苗', '244', '202104251304259182.jpg', '<div class="main-wrap  J_TRegion" id="J_MainWrap">\r\n                                <div class="sub-wrap" id="J_SubWrap">\r\n                                \r\n	<div id="J_PublicWelfare" class="tb-welfare-detail"><div class="charityTreasure"><div class="imgBox"><span><img src="https://img.alicdn.com/tfs/TB1RiGQfEY1gK0jSZFCXXcwqXXa-120-90.jpg_120x90.jpg" alt=""></span></div><div class="infoBox"><p class="brief">该商品参与了公益宝贝计划，卖家承诺每笔成交将为<strong>助力脱贫乡村医疗计划</strong>捐赠<strong>0.02元</strong>。该商品已累积捐赠<strong>654笔</strong>。</p><p class="use"><span class="field">善款用途简介：</span>该项目由阿里巴巴公益联合爱德基金会共同发起，源于2014年4月爱德基金会上线的乡村医疗计划，已在全国偏远地区建设了80所卫生室、开展了46个...<a href="http://amityfoundation.taobao.com/p/rd866075.htm" target="_blank">了解详情&gt;&gt;</a></p></div></div></div>\r\n\r\n<div id="attributes" class="attributes">\r\n    \r\n\r\n    \r\n\r\n    \r\n\r\n\r\n    \r\n\r\n    \r\n\r\n    <!-- attributes div start -->\r\n    \r\n        <ul class="attributes-list">\r\n\r\n        \r\n            <li title="长春兰园">品牌:&nbsp;长春兰园</li>\r\n            \r\n            <li title="吸甲醛 净化空气 美观">功能:&nbsp;吸甲醛 净化空气 美观</li>\r\n            \r\n            <li title="办公桌 茶几 书房 卧室 客厅">适用空间:&nbsp;办公桌 茶几 书房 卧室 客厅</li>\r\n            \r\n            <li title="艳阳红2苗连体（促销）限购5件 富山奇碟2苗连体（中苗） 富山奇碟6苗连体（开花壮苗） 富山奇碟8苗连体（开花壮苗） 朱德素2苗连体（促销） 朱德素6苗连体 青山玉泉2苗连体（促销） 青山玉泉6苗连体 铁骨素心2苗连体 铁骨素心6苗连体【当年开花】 高山春色2苗连体 高山春色3苗连体 高山春色6苗连体 东方红神荷3苗连体 小神童6苗左右 小神童8苗左右 十三太保3苗连体 十三太保2苗连体 福隆2苗连体 曲巧2苗连体 曲巧3苗连体 青龙剑5苗连体 琥珀麻壳素3苗连体【当年开花】 琥珀麻壳素6苗连体【当年开花】">颜色分类:&nbsp;艳阳红2苗连体（促销）限购5件 富山奇碟2苗连体（中苗） 富山奇碟6苗连体（开花壮苗） 富山奇碟8苗连体（开花壮苗） 朱德素2苗连体（促销） 朱德素6苗连体 青山玉泉2苗连体（促销） 青山玉泉6苗连体 铁骨素心2苗连体 铁骨素心6苗连体【当年开花】 高山春色2苗连体 高山春色3苗连体 高山春色6苗连体 东方红神荷3苗连体 小神童6苗左右 小神童8苗左右 十三太保3苗连体 十三太保2苗连体 福隆2苗连体 曲巧2苗连体 曲巧3苗连体 青龙剑5苗连体 琥珀麻壳素3苗连体【当年开花】 琥珀麻壳素6苗连体【当年开花】</li>\r\n            \r\n            <li title="不含盆">是否含花盆:&nbsp;不含盆</li>\r\n            \r\n            <li title="草本花卉">植物类别:&nbsp;草本花卉</li>\r\n            \r\n            <li title="夏季 秋季">开花季节:&nbsp;夏季 秋季</li>\r\n            \r\n            <li title="建兰">植物品种:&nbsp;建兰</li>\r\n            \r\n            <li title="非常容易">难易程度:&nbsp;非常容易</li>\r\n            \r\n            <li title="否">是否带花苞/花箭:&nbsp;否</li>\r\n            \r\n        \r\n        </ul>\r\n    \r\n\r\n\r\n    \r\n\r\n\r\n        \r\n   \r\n</div>\r\n\r\n\r\n\r\n    \r\n\r\n        \r\n    \r\n<div id="service" data-item-id="580691604055" style="display: none;"></div><div id="tad_second_area" class="tad-stage" data-spm="4"></div><div id="description" class="J_DetailSection tshop-psm ke-post">\r\n    \r\n    <div id="J_DivItemDesc" class="content"><div class="_350_desc_hd_wrapper"><a name="350ShareMask"></a></div><div class="_350_desc_bd"><div style="width: 750.0px;height: 11973.0px;overflow: hidden;"><div style="width: 750.0px;height: 11973.0px;overflow: hidden;"><img height="960" src="https://img.alicdn.com/imgextra/i3/2011720328/O1CN01qjiiyn1EIGaekC3rh_!!2011720328.jpg" style="display: block;" width="750"><img height="253" src="https://img.alicdn.com/imgextra/i1/2011720328/O1CN01reqvS11EIGad2icqq_!!2011720328.jpg" style="display: block;" width="750"><img height="337" src="https://img.alicdn.com/imgextra/i1/2011720328/O1CN01b97Qwx1EIGabjIRq8_!!2011720328.jpg" style="display: block;" width="750"><img height="608" src="https://img.alicdn.com/imgextra/i4/2011720328/O1CN01Zz5g4A1EIGagCmKRk_!!2011720328.jpg" style="display: block;" width="750"><img height="960" src="https://img.alicdn.com/imgextra/i2/2011720328/O1CN010VVuQq1EIGaX42Lpt_!!2011720328.jpg" class="" style="display: block;" width="750"><img height="960" src="https://img.alicdn.com/imgextra/i2/2011720328/O1CN01f1p5yK1EIGaZ5cnbK_!!2011720328.jpg" class="" style="display: block;" width="750"><img height="960" src="https://img.alicdn.com/imgextra/i1/2011720328/O1CN01YEm59C1EIGaaYtEoC_!!2011720328.jpg" class="" style="display: block;" width="750"><img height="960" src="https://img.alicdn.com/imgextra/i4/2011720328/O1CN01strckb1EIGaX44hJM_!!2011720328.jpg" class="" style="display: block;" width="750"><img height="960" src="https://img.alicdn.com/imgextra/i3/2011720328/O1CN01f10EbD1EIGaV8JIKg_!!2011720328.jpg" class="" style="display: block;" width="750"><img height="960" src="https://img.alicd', 0, 22, 1, 6, NULL),
	(11, NULL, '2021-04-16 20:26:15', NULL, 0, '兰花 春兰宋梅', '202104131305054661.jpg', '202104131305067051.jpg', NULL, NULL, 90, 61, 1000, NULL, '不含盆', '3苗', '245', '202104131305028758.jpg', '<p><img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020219660.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020252742.jpg.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020225540.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020298640.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020219660.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020219660.jpg" style="height:642px; width:750px" />\r\n<img alt="" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/201907092020219660.jpg" style="height:642px; width:750px" />\r\n</p>', 0, NULL, 2, 11, NULL),
	(22, NULL, '2021-04-25 13:08:52', NULL, 0, ' 蕙兰 大一品 浓香', NULL, NULL, NULL, NULL, 20, 88, 99, NULL, '不含盆', '2苗', '246', '202104251308514606.jpg', '', 0, NULL, 1, 22, NULL),
	(554, '2019-10-09 14:32:06', '2021-06-07 23:33:54', NULL, 0, '兰花 建兰 八宝奇珍', '202105111605546317.jpg', '202105111605581961.jpg', '202105111606018960.jpg', NULL, 30, 0, 10, NULL, NULL, NULL, '244', '202105111605525400.jpg', '', 0, NULL, 100, NULL, NULL),
	(556, '2019-10-10 15:35:17', '2021-07-07 21:21:22', NULL, 0, '建兰 白雪', NULL, NULL, NULL, NULL, 22, 0, 97, NULL, NULL, NULL, '244', '202104251305285197.jpg', '', 0, NULL, 22, 556, NULL),
	(681, '2021-02-08 11:26:43', '2021-06-07 23:32:53', NULL, 0, '兰花专用盆', NULL, NULL, NULL, NULL, 11, 0, 1, NULL, NULL, NULL, '273', '202104251311181223.jpg', '', 0, NULL, NULL, NULL, NULL),
	(685, '2021-04-13 13:07:29', '2021-07-14 23:16:14', NULL, 0, '兰花 建兰 香妃', '202104131307273907.jpg', NULL, NULL, NULL, 12, 0, 1, NULL, NULL, NULL, '244', '202104131307256112.jpg', '', 0, NULL, NULL, NULL, NULL),
	(686, '2021-04-25 13:05:48', '2021-07-07 23:36:02', NULL, 0, '玉娇', NULL, NULL, NULL, NULL, 18, 0, 0, NULL, '1', '带盆', '244', '202104251305479351.jpg', '', 0, NULL, NULL, NULL, NULL),
	(687, '2021-04-25 13:06:30', '2021-07-06 15:49:09', NULL, 0, '大凤素', NULL, NULL, NULL, NULL, 16, 0, 0, NULL, '1', '绿色', '244', '202104251306295193.jpg', '', 0, 1, NULL, NULL, NULL),
	(688, '2021-04-25 13:06:53', '2021-07-15 13:38:53', NULL, 0, '金荷', NULL, NULL, NULL, NULL, 16, 0, 0, NULL, '1', '1', '244', '202104251306528104.jpg', '', 0, 1, NULL, NULL, NULL),
	(691, '2021-08-18 13:19:59', '2021-08-18 13:19:59', NULL, 0, 'python爬虫代做数据挖掘脚本定制数据分析数据采集数据代爬虫接单', '202108181319564834.jpg', '202108181319578068.jpg', NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, '244', '202108181319553625.jpg', '<img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/python%E8%84%9A%E6%9C%AC/%E8%AF%A6%E6%83%85/1.jpg" style="height:276px; width:790px" />\r\n<img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/python%E8%84%9A%E6%9C%AC/%E8%AF%A6%E6%83%85/2.jpg" style="height:276px; width:790px" />\r\n<img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/python%E8%84%9A%E6%9C%AC/%E8%AF%A6%E6%83%85/3.jpg" style="height:276px; width:790px" />\r\n<img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/python%E8%84%9A%E6%9C%AC/%E8%AF%A6%E6%83%85/4.jpg" style="height:276px; width:790px" />\r\n<img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/python%E8%84%9A%E6%9C%AC/%E8%AF%A6%E6%83%85/5.jpg" style="height:276px; width:790px" />\r\n\r\n', 0, NULL, NULL, NULL, NULL),
	(692, '2021-08-18 22:43:02', '2021-08-18 22:43:02', NULL, 0, '网站建设制作商城模板一条龙全包网页设计企业做网站搭建等服务', '202108182242552602.jpg', '202108182242576457.jpg', '202108182242592016.jpg', '202108182243005812.jpg', NULL, 0, NULL, NULL, NULL, NULL, '244', '202108182242512617.jpg', '<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/1.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/2.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/3.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/4.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/5.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/6.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/7.jpg" style="height:1042px; width:780px" /></p>\r\n<p><img alt="" src="http://admin.heshihuan.cn/fileServer/product/IT_Product/%E7%BD%91%E7%AB%99/8.jpg" style="height:1042px; width:780px" /></p>\r\n', 0, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- 导出  视图 shop.product_order_v 结构
-- 创建临时表以解决视图依赖性错误
CREATE TABLE `product_order_v` (
	`id` INT(11) NOT NULL,
	`productid` INT(11) NULL,
	`orderid` INT(11) NULL,
	`mount` INT(11) NULL,
	`basename` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`funame` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`title` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`main_image` VARCHAR(4096) NULL COLLATE 'utf8_general_ci',
	`propid` INT(11) NULL,
	`image800` VARCHAR(512) NULL COLLATE 'utf8_general_ci',
	`image400` VARCHAR(512) NULL COLLATE 'utf8_general_ci',
	`image200` VARCHAR(512) NULL COLLATE 'utf8_general_ci',
	`image100` VARCHAR(512) NULL COLLATE 'utf8_general_ci',
	`price` FLOAT NULL,
	`size` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`color` VARCHAR(64) NULL COLLATE 'utf8_general_ci',
	`create_time` DATETIME NULL,
	`update_time` DATETIME NULL,
	`remark` VARCHAR(128) NULL COLLATE 'utf8_general_ci',
	`status` INT(11) NULL
) ENGINE=MyISAM;

-- 导出  表 shop.product__order 结构
CREATE TABLE IF NOT EXISTS `product__order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `propid` int(11) DEFAULT NULL,
  `mount` int(11) DEFAULT NULL,
  `basename` varchar(128) DEFAULT NULL,
  `funame` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=313 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.product__order 的数据：~312 rows (大约)
DELETE FROM `product__order`;
/*!40000 ALTER TABLE `product__order` DISABLE KEYS */;
INSERT INTO `product__order` (`id`, `create_time`, `update_time`, `remark`, `status`, `orderid`, `productid`, `propid`, `mount`, `basename`, `funame`) VALUES
	(1, '2021-03-06 20:44:20', '2021-03-06 20:44:20', NULL, 0, 397, 11, 31, 60, NULL, NULL),
	(2, '2021-03-06 22:22:27', '2021-03-06 22:22:27', NULL, 0, 404, NULL, 31, 2, NULL, NULL),
	(3, '2021-03-06 22:26:11', '2021-03-06 22:26:11', NULL, 0, 405, NULL, 32, 1, NULL, NULL),
	(4, '2021-03-06 22:28:44', '2021-03-06 22:28:44', NULL, 0, 406, NULL, 26, 3, NULL, NULL),
	(5, '2021-03-06 22:31:35', '2021-03-06 22:31:35', NULL, 0, 407, NULL, 22, 1, NULL, NULL),
	(6, '2021-03-06 22:33:35', '2021-03-06 22:33:35', NULL, 0, 409, 22, 22, 2, NULL, NULL),
	(7, '2021-03-06 22:33:35', '2021-03-06 22:33:35', NULL, 0, 409, 11, 31, 2, NULL, NULL),
	(8, '2021-03-06 22:33:40', '2021-03-06 22:33:40', NULL, 0, 410, 22, 22, 2, NULL, NULL),
	(9, '2021-03-06 22:33:40', '2021-03-06 22:33:40', NULL, 0, 410, 11, 31, 2, NULL, NULL),
	(10, '2021-03-06 23:08:39', '2021-03-06 23:08:39', NULL, 0, 411, 33, 0, 30, NULL, NULL),
	(11, '2021-03-06 23:27:16', '2021-03-06 23:27:16', NULL, 0, 412, 33, 0, 30, NULL, NULL),
	(12, '2021-03-06 23:28:10', '2021-03-06 23:28:10', NULL, 0, 413, 33, 0, 1, NULL, NULL),
	(13, '2021-03-06 23:46:15', '2021-03-06 23:46:15', NULL, 0, 414, 11, 32, 2, NULL, NULL),
	(14, '2021-03-06 23:50:21', '2021-03-06 23:50:21', NULL, 0, 415, 11, 32, 2, NULL, NULL),
	(15, '2021-03-06 23:57:07', '2021-03-06 23:57:07', NULL, 0, 416, 22, 0, 2, NULL, NULL),
	(16, '2021-03-07 01:15:43', '2021-03-07 01:15:43', NULL, 0, 417, 33, 0, 2, NULL, NULL),
	(17, '2021-03-07 01:29:23', '2021-03-07 01:29:23', NULL, 0, 418, 33, 0, 1, NULL, NULL),
	(18, '2021-03-07 01:30:12', '2021-03-07 01:30:12', NULL, 0, 419, 33, 0, 1, NULL, NULL),
	(19, '2021-03-07 01:31:09', '2021-03-07 01:31:09', NULL, 0, 420, 33, 0, 1, NULL, NULL),
	(20, '2021-03-07 01:35:49', '2021-03-07 01:35:49', NULL, 0, 421, 33, 0, 1, NULL, NULL),
	(21, '2021-03-07 01:35:54', '2021-03-07 01:35:54', NULL, 0, 422, 33, 0, 1, NULL, NULL),
	(22, '2021-03-07 09:16:48', '2021-03-07 09:16:48', NULL, 0, 424, 554, 0, 2, NULL, NULL),
	(23, '2021-03-08 19:25:06', '2021-03-08 19:25:06', NULL, 0, 425, 11, 31, 1, NULL, NULL),
	(24, '2021-03-08 19:30:54', '2021-03-08 19:30:54', NULL, 0, 426, 33, 0, 1, NULL, NULL),
	(25, '2021-03-08 19:34:30', '2021-03-08 19:34:30', NULL, 0, 427, 11, 30, 1, NULL, NULL),
	(26, '2021-03-08 19:49:53', '2021-03-08 19:49:53', NULL, 0, 428, 11, 30, 1, NULL, NULL),
	(27, '2021-03-08 19:59:26', '2021-03-08 19:59:26', NULL, 0, 429, 11, 30, 1, NULL, NULL),
	(28, '2021-03-08 20:15:39', '2021-03-08 20:15:39', NULL, 0, 430, 11, 30, 1, NULL, NULL),
	(29, '2021-03-08 20:32:50', '2021-03-08 20:32:50', NULL, 0, 431, 6, 25, 1, NULL, NULL),
	(30, '2021-03-08 20:35:27', '2021-03-08 20:35:27', NULL, 0, 432, 6, 25, 1, NULL, NULL),
	(31, '2021-03-08 20:42:27', '2021-03-08 20:42:27', NULL, 0, 433, 11, 30, 1, NULL, NULL),
	(32, '2021-03-08 20:43:28', '2021-03-08 20:43:28', NULL, 0, 434, 11, 30, 1, NULL, NULL),
	(33, '2021-03-08 21:58:30', '2021-03-08 21:58:30', NULL, 0, 435, 11, 30, 1, NULL, NULL),
	(34, '2021-03-08 22:21:10', '2021-03-08 22:21:10', NULL, 0, 436, 33, 0, 1, NULL, NULL),
	(35, '2021-03-08 22:30:10', '2021-03-08 22:30:10', NULL, 0, 437, 11, 30, 1, NULL, NULL),
	(36, '2021-03-08 22:34:16', '2021-03-08 22:34:16', NULL, 0, 438, 22, 0, 1, NULL, NULL),
	(37, '2021-03-08 22:37:03', '2021-03-08 22:37:03', NULL, 0, 439, 22, 0, 1, NULL, NULL),
	(38, '2021-03-08 22:47:50', '2021-03-08 22:47:50', NULL, 0, 440, 22, 0, 1, NULL, NULL),
	(39, '2021-03-08 23:04:39', '2021-03-08 23:04:39', NULL, 0, 441, 11, 30, 1, NULL, NULL),
	(40, '2021-03-08 23:11:37', '2021-03-08 23:11:37', NULL, 0, 442, 11, 30, 1, NULL, NULL),
	(41, '2021-03-08 23:39:55', '2021-03-08 23:39:55', NULL, 0, 443, 11, 30, 1, NULL, NULL),
	(42, '2021-03-08 23:41:14', '2021-03-08 23:41:14', NULL, 0, 444, 22, 0, 3, NULL, NULL),
	(43, '2021-03-08 23:44:48', '2021-03-08 23:44:48', NULL, 0, 445, 22, 0, 2, NULL, NULL),
	(44, '2021-03-08 23:58:02', '2021-03-08 23:58:02', NULL, 0, 446, 436, 0, 1, NULL, NULL),
	(45, '2021-03-08 23:59:00', '2021-03-08 23:59:00', NULL, 0, 447, 6, 25, 1, NULL, NULL),
	(46, '2021-03-09 00:16:04', '2021-03-09 00:16:04', NULL, 0, 448, 6, 26, 1, NULL, NULL),
	(47, '2021-03-09 00:16:39', '2021-03-09 00:16:39', NULL, 0, 449, 6, 26, 1, NULL, NULL),
	(48, '2021-03-09 00:24:59', '2021-03-09 00:24:59', NULL, 0, 450, 11, 30, 1, NULL, NULL),
	(49, '2021-03-09 00:25:17', '2021-03-09 00:25:17', NULL, 0, 451, 11, 30, 1, NULL, NULL),
	(50, '2021-03-09 00:26:21', '2021-03-09 00:26:21', NULL, 0, 452, 11, 30, 1, NULL, NULL),
	(51, '2021-03-09 00:26:22', '2021-03-09 00:26:22', NULL, 0, 453, 11, 30, 1, NULL, NULL),
	(52, '2021-03-09 00:33:25', '2021-03-09 00:33:25', NULL, 0, 454, 6, 26, 1, NULL, NULL),
	(53, '2021-03-09 00:49:25', '2021-03-09 00:49:25', NULL, 0, 455, 6, 25, 1, NULL, NULL),
	(54, '2021-03-09 00:54:36', '2021-03-09 00:54:36', NULL, 0, 456, 22, 0, 1, NULL, NULL),
	(55, '2021-03-09 01:00:47', '2021-03-09 01:00:47', NULL, 0, 457, 11, 30, 1, NULL, NULL),
	(56, '2021-03-09 01:09:21', '2021-03-09 01:09:21', NULL, 0, 458, 33, 0, 1, NULL, NULL),
	(57, '2021-03-09 01:10:35', '2021-03-09 01:10:35', NULL, 0, 459, 33, 0, 1, NULL, NULL),
	(58, '2021-03-09 01:15:05', '2021-03-09 01:15:05', NULL, 0, 460, 11, 30, 1, NULL, NULL),
	(59, '2021-03-09 01:20:28', '2021-03-09 01:20:28', NULL, 0, 461, 11, 30, 1, NULL, NULL),
	(60, '2021-03-09 20:41:33', '2021-03-09 20:41:33', NULL, 0, 462, 11, 30, 1, NULL, NULL),
	(61, '2021-03-09 20:46:55', '2021-03-09 20:46:55', NULL, 0, 463, 33, 0, 1, NULL, NULL),
	(62, '2021-03-09 20:55:15', '2021-03-09 20:55:15', NULL, 0, 464, 11, 30, 1, NULL, NULL),
	(63, '2021-03-09 20:55:49', '2021-03-09 20:55:49', NULL, 0, 465, 33, 0, 1, NULL, NULL),
	(64, '2021-03-09 20:57:06', '2021-03-09 20:57:06', NULL, 0, 466, 22, 0, 1, NULL, NULL),
	(65, '2021-03-09 20:57:08', '2021-03-09 20:57:08', NULL, 0, 467, 22, 0, 1, NULL, NULL),
	(66, '2021-03-09 22:47:45', '2021-03-09 22:47:45', NULL, 0, 468, 11, 30, 1, NULL, NULL),
	(67, '2021-03-09 22:49:44', '2021-03-09 22:49:44', NULL, 0, 469, 11, 30, 1, NULL, NULL),
	(68, '2021-03-09 22:49:45', '2021-03-09 22:49:45', NULL, 0, 470, 11, 30, 1, NULL, NULL),
	(69, '2021-03-09 22:50:44', '2021-03-09 22:50:44', NULL, 0, 471, 11, 30, 1, NULL, NULL),
	(70, '2021-03-09 22:50:46', '2021-03-09 22:50:46', NULL, 0, 472, 11, 30, 1, NULL, NULL),
	(71, '2021-03-09 22:52:40', '2021-03-09 22:52:40', NULL, 0, 473, 11, 30, 1, NULL, NULL),
	(72, '2021-03-09 22:52:43', '2021-03-09 22:52:43', NULL, 0, 474, 11, 30, 1, NULL, NULL),
	(73, '2021-03-09 22:54:56', '2021-03-09 22:54:56', NULL, 0, 475, 11, 30, 1, NULL, NULL),
	(74, '2021-03-09 23:07:05', '2021-03-09 23:07:05', NULL, 0, 476, 6, 25, 1, NULL, NULL),
	(75, '2021-03-09 23:11:41', '2021-03-09 23:11:41', NULL, 0, 477, 6, 25, 1, NULL, NULL),
	(76, '2021-03-09 23:17:43', '2021-03-09 23:17:43', NULL, 0, 478, 11, 30, 1, NULL, NULL),
	(77, '2021-03-09 23:19:37', '2021-03-09 23:19:37', NULL, 0, 479, 33, 0, 1, NULL, NULL),
	(78, '2021-03-09 23:25:27', '2021-03-09 23:25:27', NULL, 0, 480, 11, 30, 1, NULL, NULL),
	(79, '2021-03-09 23:34:15', '2021-03-09 23:34:15', NULL, 0, 481, 6, 25, 1, NULL, NULL),
	(80, '2021-03-09 23:47:17', '2021-03-09 23:47:17', NULL, 0, 482, 11, 30, 1, NULL, NULL),
	(81, '2021-03-09 23:48:00', '2021-03-09 23:48:00', NULL, 0, 483, 11, 30, 1, NULL, NULL),
	(82, '2021-03-10 00:04:40', '2021-03-10 00:04:40', NULL, 0, 484, 11, 30, 1, NULL, NULL),
	(83, '2021-03-10 00:08:39', '2021-03-10 00:08:39', NULL, 0, 485, 33, 0, 1, NULL, NULL),
	(84, '2021-03-10 00:09:16', '2021-03-10 00:09:16', NULL, 0, 486, 33, 0, 1, NULL, NULL),
	(85, '2021-03-10 00:12:05', '2021-03-10 00:12:05', NULL, 0, 487, 33, 0, 1, NULL, NULL),
	(86, '2021-03-10 00:16:33', '2021-03-10 00:16:33', NULL, 0, 488, 11, 30, 1, NULL, NULL),
	(87, '2021-03-10 00:17:02', '2021-03-10 00:17:02', NULL, 0, 489, 6, 25, 1, NULL, NULL),
	(88, '2021-03-10 00:17:38', '2021-03-10 00:17:38', NULL, 0, 490, 11, 30, 1, NULL, NULL),
	(89, '2021-03-10 00:21:59', '2021-03-10 00:21:59', NULL, 0, 491, 11, 30, 1, NULL, NULL),
	(90, '2021-03-10 00:23:03', '2021-03-10 00:23:03', NULL, 0, 492, 11, 30, 1, NULL, NULL),
	(91, '2021-03-10 00:25:19', '2021-03-10 00:25:19', NULL, 0, 493, 11, 30, 1, NULL, NULL),
	(92, '2021-03-10 00:25:37', '2021-03-10 00:25:37', NULL, 0, 494, 11, 30, 1, NULL, NULL),
	(93, '2021-03-10 00:28:38', '2021-03-10 00:28:38', NULL, 0, 495, 6, 25, 1, NULL, NULL),
	(94, '2021-03-10 00:32:56', '2021-03-10 00:32:56', NULL, 0, 496, 11, 30, 1, NULL, NULL),
	(95, '2021-03-10 00:53:09', '2021-03-10 00:53:09', NULL, 0, 497, 6, 25, 3, NULL, NULL),
	(96, '2021-03-10 00:54:33', '2021-03-10 00:54:33', NULL, 0, 498, 6, 25, 2, NULL, NULL),
	(97, '2021-03-10 00:55:22', '2021-03-10 00:55:22', NULL, 0, 499, 6, 25, 1, NULL, NULL),
	(98, '2021-03-10 00:55:41', '2021-03-10 00:55:41', NULL, 0, 500, 6, 25, 1, NULL, NULL),
	(99, '2021-03-10 00:58:37', '2021-03-10 00:58:37', NULL, 0, 501, 6, 25, 1, NULL, NULL),
	(100, '2021-03-10 01:03:20', '2021-03-10 01:03:20', NULL, 0, 502, 11, 30, 1, NULL, NULL),
	(101, '2021-03-10 01:03:42', '2021-03-10 01:03:42', NULL, 0, 503, 6, 25, 1, NULL, NULL),
	(102, '2021-03-10 01:03:43', '2021-03-10 01:03:43', NULL, 0, 504, 6, 25, 1, NULL, NULL),
	(103, '2021-03-10 07:29:04', '2021-03-10 07:29:04', NULL, 0, 505, 11, 30, 1, NULL, NULL),
	(104, '2021-03-11 09:59:55', '2021-03-11 09:59:55', NULL, 0, 506, 11, 30, 1, NULL, NULL),
	(105, '2021-03-12 20:51:30', '2021-03-12 20:51:30', NULL, 0, 507, 11, 30, 1, NULL, NULL),
	(106, '2021-03-12 21:08:59', '2021-03-12 21:08:59', NULL, 0, 508, 6, 25, 1, NULL, NULL),
	(107, '2021-03-12 21:12:55', '2021-03-12 21:12:55', NULL, 0, 509, 11, 30, 1, NULL, NULL),
	(108, '2021-03-12 21:19:32', '2021-03-12 21:19:32', NULL, 0, 510, 6, 25, 1, NULL, NULL),
	(109, '2021-03-12 21:28:42', '2021-03-12 21:28:42', NULL, 0, 511, 11, 30, 1, NULL, NULL),
	(110, '2021-03-12 21:39:05', '2021-03-12 21:39:05', NULL, 0, 512, 6, 25, 1, NULL, NULL),
	(111, '2021-03-12 21:49:32', '2021-03-12 21:49:32', NULL, 0, 513, 554, 0, 1, NULL, NULL),
	(112, '2021-03-12 21:50:35', '2021-03-12 21:50:35', NULL, 0, 514, 556, 0, 1, NULL, NULL),
	(113, '2021-03-12 21:50:36', '2021-03-12 21:50:36', NULL, 0, 515, 556, 0, 1, NULL, NULL),
	(114, '2021-03-12 22:35:09', '2021-03-12 22:35:09', NULL, 0, 516, 11, 30, 1, NULL, NULL),
	(115, '2021-03-12 23:00:20', '2021-03-12 23:00:20', NULL, 0, 517, 11, 30, 1, NULL, NULL),
	(116, '2021-03-12 23:05:23', '2021-03-12 23:05:23', NULL, 0, 518, 33, 0, 2, NULL, NULL),
	(117, '2021-03-19 12:57:00', '2021-03-19 12:57:00', NULL, 0, 519, 11, 96, 1, NULL, NULL),
	(118, '2021-03-20 08:38:27', '2021-03-20 08:38:27', NULL, 0, 520, 11, 147, 2, NULL, NULL),
	(119, '2021-03-20 08:43:43', '2021-03-20 08:43:43', NULL, 0, 521, 22, 0, 1, NULL, NULL),
	(120, '2021-03-20 08:53:04', '2021-03-20 08:53:04', NULL, 0, 522, 11, 144, 1, NULL, NULL),
	(121, '2021-03-20 08:57:04', '2021-03-20 08:57:04', NULL, 0, 523, 11, 144, 1, NULL, NULL),
	(122, '2021-03-20 09:10:59', '2021-03-20 09:10:59', NULL, 0, 524, 11, 144, 1, NULL, NULL),
	(123, '2021-03-20 09:19:12', '2021-03-20 09:19:12', NULL, 0, 525, 11, 144, 1, NULL, NULL),
	(124, '2021-03-20 19:32:50', '2021-03-20 19:32:50', NULL, 0, 526, 11, 148, 1, NULL, NULL),
	(125, '2021-03-20 19:34:42', '2021-03-20 19:34:42', NULL, 0, 527, 11, 144, 1, NULL, NULL),
	(126, '2021-03-21 00:59:35', '2021-03-21 00:59:35', NULL, 0, 528, 11, 146, 1, NULL, NULL),
	(127, '2021-03-21 01:01:12', '2021-03-21 01:01:12', NULL, 0, 529, 11, 146, 1, NULL, NULL),
	(128, '2021-03-21 01:05:05', '2021-03-21 01:05:05', NULL, 0, 530, 11, 146, 1, NULL, NULL),
	(129, '2021-03-21 01:05:58', '2021-03-21 01:05:58', NULL, 0, 531, 11, 144, 1, NULL, NULL),
	(130, '2021-03-21 01:29:26', '2021-03-21 01:29:26', NULL, 0, 532, 11, 145, 1, NULL, NULL),
	(131, '2021-03-21 01:29:40', '2021-03-21 01:29:40', NULL, 0, 533, 11, 144, 1, NULL, NULL),
	(132, '2021-03-21 01:37:30', '2021-03-21 01:37:30', NULL, 0, 534, 11, 144, 1, NULL, NULL),
	(133, '2021-03-21 01:43:59', '2021-03-21 01:43:59', NULL, 0, 535, 11, 144, 1, NULL, NULL),
	(134, '2021-03-21 01:44:43', '2021-03-21 01:44:43', NULL, 0, 536, 11, 144, 1, NULL, NULL),
	(135, '2021-03-21 01:49:36', '2021-03-21 01:49:36', NULL, 0, 537, 11, 144, 1, NULL, NULL),
	(136, '2021-03-21 01:53:54', '2021-03-21 01:53:54', NULL, 0, 538, 11, 144, 1, NULL, NULL),
	(137, '2021-03-21 01:57:43', '2021-03-21 01:57:43', NULL, 0, 539, 11, 147, 1, NULL, NULL),
	(138, '2021-03-21 02:04:05', '2021-03-21 02:04:05', NULL, 0, 540, 11, 144, 1, NULL, NULL),
	(139, '2021-03-21 02:04:35', '2021-03-21 02:04:35', NULL, 0, 541, 11, 144, 2, NULL, NULL),
	(140, '2021-03-21 02:11:54', '2021-03-21 02:11:54', NULL, 0, 542, 11, 144, 3, NULL, NULL),
	(141, '2021-03-21 02:13:01', '2021-03-21 02:13:01', NULL, 0, 543, 6, 26, 2, NULL, NULL),
	(142, '2021-03-21 02:15:56', '2021-03-21 02:15:56', NULL, 0, 544, 6, 26, 1, NULL, NULL),
	(143, '2021-03-21 02:16:18', '2021-03-21 02:16:18', NULL, 0, 545, 11, 146, 1, NULL, NULL),
	(144, '2021-03-21 02:16:34', '2021-03-21 02:16:34', NULL, 0, 546, 11, 144, 1, NULL, NULL),
	(145, '2021-03-21 02:17:02', '2021-03-21 02:17:02', NULL, 0, 547, 11, 149, 2, NULL, NULL),
	(146, '2021-03-21 02:24:53', '2021-03-21 02:24:53', NULL, 0, 548, 11, 144, 1, NULL, NULL),
	(147, '2021-03-21 12:49:20', '2021-03-21 12:49:20', NULL, 0, 549, 11, 144, 1, NULL, NULL),
	(148, '2021-03-21 16:18:20', '2021-03-21 16:18:20', NULL, 0, 550, 11, 144, 1, NULL, NULL),
	(149, '2021-03-21 21:24:28', '2021-03-21 21:24:28', NULL, 0, 551, 11, 144, 1, NULL, NULL),
	(150, '2021-03-21 21:24:41', '2021-03-21 21:24:41', NULL, 0, 552, 11, 146, 1, NULL, NULL),
	(151, '2021-04-16 20:50:17', '2021-04-16 20:50:17', NULL, 0, 553, 11, 144, 1, NULL, NULL),
	(152, '2021-05-03 15:05:18', '2021-05-03 15:05:18', NULL, 0, 554, 11, 144, 1, NULL, NULL),
	(153, '2021-05-03 15:06:57', '2021-05-03 15:06:57', NULL, 0, 555, 11, 144, 1, NULL, NULL),
	(154, '2021-05-03 15:10:33', '2021-05-03 15:10:33', NULL, 0, 556, 686, 0, 1, NULL, NULL),
	(155, '2021-05-03 17:41:26', '2021-05-03 17:41:26', NULL, 0, 557, 556, 0, 1, NULL, NULL),
	(156, '2021-05-03 17:42:25', '2021-05-03 17:42:25', NULL, 0, 558, 686, 0, 2, NULL, NULL),
	(157, '2021-05-04 08:55:43', '2021-05-04 08:55:43', NULL, 0, 559, 556, 0, 1, NULL, NULL),
	(158, '2021-05-04 09:17:04', '2021-05-04 09:17:04', NULL, 0, 560, 11, 144, 1, NULL, NULL),
	(159, '2021-05-04 09:21:46', '2021-05-04 09:21:46', NULL, 0, 561, 556, 0, 1, NULL, NULL),
	(160, '2021-05-05 23:10:42', '2021-05-05 23:10:42', NULL, 0, 562, 22, 0, 1, NULL, NULL),
	(161, '2021-05-11 16:56:39', '2021-05-11 16:56:39', NULL, 0, 563, 11, 148, 1, NULL, NULL),
	(162, '2021-05-12 08:12:38', '2021-05-12 08:12:38', NULL, 0, 564, 6, 155, 1, NULL, NULL),
	(163, '2021-05-17 11:54:14', '2021-05-17 11:54:14', NULL, 0, 565, 6, 154, 1, NULL, NULL),
	(164, '2021-05-20 23:02:41', '2021-05-20 23:02:41', NULL, 0, 566, 686, 0, 1, NULL, NULL),
	(165, '2021-05-31 12:25:37', '2021-05-31 12:25:37', NULL, 0, 567, 11, 148, 2, NULL, NULL),
	(166, '2021-06-02 13:18:11', '2021-06-02 13:18:11', NULL, 0, 568, 554, 0, 1, NULL, NULL),
	(167, '2021-06-02 13:19:38', '2021-06-02 13:19:38', NULL, 0, 569, 11, 144, 1, NULL, NULL),
	(168, '2021-06-02 13:45:12', '2021-06-02 13:45:12', NULL, 0, 570, 11, 144, 1, NULL, NULL),
	(169, '2021-06-02 23:23:28', '2021-06-02 23:23:28', NULL, 0, 571, 6, 154, 1, NULL, NULL),
	(170, '2021-06-02 23:23:58', '2021-06-02 23:23:58', NULL, 0, 572, 554, 0, 1, NULL, NULL),
	(171, '2021-06-02 23:24:31', '2021-06-02 23:24:31', NULL, 0, 573, 6, 154, 1, NULL, NULL),
	(172, '2021-06-09 13:51:15', '2021-06-09 13:51:15', NULL, 0, 574, 11, 144, 1, NULL, NULL),
	(173, '2021-06-09 13:51:54', '2021-06-09 13:51:54', NULL, 0, 575, 22, 0, 1, NULL, NULL),
	(174, '2021-06-10 08:06:41', '2021-06-10 08:06:41', NULL, 0, 576, 11, 149, 1, NULL, NULL),
	(175, '2021-06-10 13:04:59', '2021-06-10 13:04:59', NULL, 0, 577, 11, 149, 1, NULL, NULL),
	(176, '2021-06-10 13:13:32', '2021-06-10 13:13:32', NULL, 0, 578, 11, 144, 1, NULL, NULL),
	(177, '2021-06-10 13:13:49', '2021-06-10 13:13:49', NULL, 0, 579, 11, 144, 1, NULL, NULL),
	(178, '2021-06-10 13:18:06', '2021-06-10 13:18:06', NULL, 0, 580, 11, 144, 1, NULL, NULL),
	(179, '2021-06-10 13:19:40', '2021-06-10 13:19:40', NULL, 0, 581, 11, 144, 1, NULL, NULL),
	(180, '2021-06-10 13:20:49', '2021-06-10 13:20:49', NULL, 0, 582, 11, 144, 1, NULL, NULL),
	(181, '2021-06-10 13:21:11', '2021-06-10 13:21:11', NULL, 0, 583, 11, 144, 1, NULL, NULL),
	(182, '2021-06-10 13:22:57', '2021-06-10 13:22:57', NULL, 0, 584, 11, 144, 1, NULL, NULL),
	(183, '2021-06-10 13:23:38', '2021-06-10 13:23:38', NULL, 0, 585, 11, 144, 1, NULL, NULL),
	(184, '2021-06-10 13:24:57', '2021-06-10 13:24:57', NULL, 0, 586, 11, 144, 1, NULL, NULL),
	(185, '2021-06-10 13:26:32', '2021-06-10 13:26:32', NULL, 0, 587, 11, 146, 1, NULL, NULL),
	(186, '2021-06-10 13:29:42', '2021-06-10 13:29:42', NULL, 0, 588, 11, 146, 1, NULL, NULL),
	(187, '2021-06-15 23:52:57', '2021-06-15 23:52:57', NULL, 0, 589, 22, 0, 1, NULL, NULL),
	(188, '2021-06-17 19:42:02', '2021-06-17 19:42:02', NULL, 0, 590, 554, 0, 1, NULL, NULL),
	(189, '2021-06-17 19:43:47', '2021-06-17 19:43:47', NULL, 0, 591, 554, 0, 1, NULL, NULL),
	(190, '2021-06-17 19:44:32', '2021-06-17 19:44:32', NULL, 0, 592, 556, 0, 1, NULL, NULL),
	(191, '2021-06-17 19:46:36', '2021-06-17 19:46:36', NULL, 0, 593, 556, 0, 1, NULL, NULL),
	(192, '2021-06-17 19:47:14', '2021-06-17 19:47:14', NULL, 0, 594, 556, 0, 1, NULL, NULL),
	(193, '2021-06-17 19:49:43', '2021-06-17 19:49:43', NULL, 0, 595, 22, 0, 1, NULL, NULL),
	(194, '2021-06-17 19:56:56', '2021-06-17 19:56:56', NULL, 0, 596, 556, 0, 1, NULL, NULL),
	(195, '2021-06-17 19:59:04', '2021-06-17 19:59:04', NULL, 0, 597, 556, 0, 1, NULL, NULL),
	(196, '2021-06-17 23:06:20', '2021-06-17 23:06:20', NULL, 0, 598, 22, 0, 1, NULL, NULL),
	(197, '2021-06-17 23:10:37', '2021-06-17 23:10:37', NULL, 0, 599, 22, 0, 1, NULL, NULL),
	(198, '2021-06-17 23:12:59', '2021-06-17 23:12:59', NULL, 0, 600, 22, 0, 1, NULL, NULL),
	(199, '2021-06-17 23:13:35', '2021-06-17 23:13:35', NULL, 0, 601, 22, 0, 1, NULL, NULL),
	(200, '2021-06-17 23:14:15', '2021-06-17 23:14:15', NULL, 0, 602, 556, 0, 1, NULL, NULL),
	(201, '2021-06-17 23:14:51', '2021-06-17 23:14:51', NULL, 0, 603, 556, 0, 1, NULL, NULL),
	(202, '2021-06-17 23:18:04', '2021-06-17 23:18:04', NULL, 0, 604, 22, 0, 1, NULL, NULL),
	(203, '2021-06-17 23:31:19', '2021-06-17 23:31:19', NULL, 0, 605, 556, 0, 1, NULL, NULL),
	(204, '2021-06-17 23:42:30', '2021-06-17 23:42:30', NULL, 0, 606, 22, 0, 1, NULL, NULL),
	(205, '2021-06-17 23:48:54', '2021-06-17 23:48:54', NULL, 0, 607, 22, 0, 1, NULL, NULL),
	(206, '2021-06-17 23:55:13', '2021-06-17 23:55:13', NULL, 0, 608, 22, 0, 1, NULL, NULL),
	(207, '2021-06-17 23:56:19', '2021-06-17 23:56:19', NULL, 0, 609, 22, 0, 1, NULL, NULL),
	(208, '2021-06-17 23:57:20', '2021-06-17 23:57:20', NULL, 0, 610, 22, 0, 1, NULL, NULL),
	(209, '2021-06-18 00:00:39', '2021-06-18 00:00:39', NULL, 0, 611, 22, 0, 1, NULL, NULL),
	(210, '2021-06-18 00:02:55', '2021-06-18 00:02:55', NULL, 0, 612, 22, 0, 1, NULL, NULL),
	(211, '2021-06-29 23:19:59', '2021-06-29 23:19:59', NULL, 0, 613, 686, 0, 1, NULL, NULL),
	(212, '2021-06-29 23:20:32', '2021-06-29 23:20:32', NULL, 0, 614, 686, 0, 1, NULL, NULL),
	(213, '2021-06-29 23:21:22', '2021-06-29 23:21:22', NULL, 0, 615, 554, 0, 1, NULL, NULL),
	(214, '2021-06-30 13:08:01', '2021-06-30 13:08:01', NULL, 0, 616, 11, 144, 1, NULL, NULL),
	(215, '2021-06-30 13:08:47', '2021-06-30 13:08:47', NULL, 0, 617, 554, 0, 1, NULL, NULL),
	(216, '2021-06-30 13:15:27', '2021-06-30 13:15:27', NULL, 0, 618, 554, 0, 1, NULL, NULL),
	(217, '2021-06-30 13:15:48', '2021-06-30 13:15:48', NULL, 0, 619, 554, 0, 1, NULL, NULL),
	(218, '2021-06-30 13:16:12', '2021-06-30 13:16:12', NULL, 0, 620, 554, 0, 1, NULL, NULL),
	(219, '2021-06-30 13:17:31', '2021-06-30 13:17:31', NULL, 0, 621, 686, 0, 1, NULL, NULL),
	(220, '2021-06-30 13:18:04', '2021-06-30 13:18:04', NULL, 0, 622, 686, 0, 1, NULL, NULL),
	(221, '2021-06-30 13:22:55', '2021-06-30 13:22:55', NULL, 0, 623, 556, 0, 1, NULL, NULL),
	(222, '2021-06-30 13:33:57', '2021-06-30 13:33:57', NULL, 0, 624, 556, 0, 1, NULL, NULL),
	(223, '2021-06-30 13:35:52', '2021-06-30 13:35:52', NULL, 0, 625, 556, 0, 1, NULL, NULL),
	(224, '2021-06-30 13:44:17', '2021-06-30 13:44:17', NULL, 0, 626, 556, 0, 1, NULL, NULL),
	(225, '2021-06-30 13:45:12', '2021-06-30 13:45:12', NULL, 0, 627, 556, 0, 1, NULL, NULL),
	(226, '2021-06-30 13:50:56', '2021-06-30 13:50:56', NULL, 0, 628, 556, 0, 1, NULL, NULL),
	(227, '2021-06-30 13:51:43', '2021-06-30 13:51:43', NULL, 0, 629, 556, 0, 1, NULL, NULL),
	(228, '2021-06-30 13:54:32', '2021-06-30 13:54:32', NULL, 0, 630, 556, 0, 1, NULL, NULL),
	(229, '2021-06-30 14:46:29', '2021-06-30 14:46:29', NULL, 0, 631, 556, 0, 1, NULL, NULL),
	(230, '2021-06-30 14:55:04', '2021-06-30 14:55:04', NULL, 0, 632, 556, 0, 1, NULL, NULL),
	(231, '2021-06-30 20:47:19', '2021-06-30 20:47:19', NULL, 0, 633, 556, 0, 1, NULL, NULL),
	(232, '2021-06-30 20:48:08', '2021-06-30 20:48:08', NULL, 0, 634, 556, 0, 1, NULL, NULL),
	(233, '2021-06-30 20:51:23', '2021-06-30 20:51:23', NULL, 0, 635, 556, 0, 1, NULL, NULL),
	(234, '2021-06-30 21:26:45', '2021-06-30 21:26:45', NULL, 0, 636, 556, 0, 1, NULL, NULL),
	(235, '2021-06-30 21:37:36', '2021-06-30 21:37:36', NULL, 0, 637, 556, 0, 1, NULL, NULL),
	(236, '2021-06-30 21:38:58', '2021-06-30 21:38:58', NULL, 0, 638, 556, 0, 1, NULL, NULL),
	(237, '2021-06-30 21:46:50', '2021-06-30 21:46:50', NULL, 0, 639, 556, 0, 1, NULL, NULL),
	(238, '2021-06-30 22:16:41', '2021-06-30 22:16:41', NULL, 0, 640, 556, 0, 1, NULL, NULL),
	(239, '2021-06-30 22:17:54', '2021-06-30 22:17:54', NULL, 0, 641, 556, 0, 1, NULL, NULL),
	(240, '2021-06-30 22:28:44', '2021-06-30 22:28:44', NULL, 0, 642, 556, 0, 1, NULL, NULL),
	(241, '2021-06-30 22:46:19', '2021-06-30 22:46:19', NULL, 0, 643, 556, 0, 1, NULL, NULL),
	(242, '2021-06-30 22:54:14', '2021-06-30 22:54:14', NULL, 0, 644, 556, 0, 1, NULL, NULL),
	(243, '2021-06-30 23:03:53', '2021-06-30 23:03:53', NULL, 0, 645, 556, 0, 1, NULL, NULL),
	(244, '2021-06-30 23:05:54', '2021-06-30 23:05:54', NULL, 0, 646, 556, 0, 1, NULL, NULL),
	(245, '2021-06-30 23:22:10', '2021-06-30 23:22:10', NULL, 0, 647, 556, 0, 1, NULL, NULL),
	(246, '2021-06-30 23:26:08', '2021-06-30 23:26:08', NULL, 0, 648, 556, 0, 1, NULL, NULL),
	(247, '2021-06-30 23:34:08', '2021-06-30 23:34:08', NULL, 0, 649, 556, 0, 1, NULL, NULL),
	(248, '2021-06-30 23:45:21', '2021-06-30 23:45:21', NULL, 0, 650, 556, 0, 1, NULL, NULL),
	(249, '2021-06-30 23:48:38', '2021-06-30 23:48:38', NULL, 0, 651, 556, 0, 1, NULL, NULL),
	(250, '2021-06-30 23:49:57', '2021-06-30 23:49:57', NULL, 0, 652, 556, 0, 1, NULL, NULL),
	(251, '2021-06-30 23:51:18', '2021-06-30 23:51:18', NULL, 0, 653, 556, 0, 1, NULL, NULL),
	(252, '2021-06-30 23:54:11', '2021-06-30 23:54:11', NULL, 0, 654, 556, 0, 1, NULL, NULL),
	(253, '2021-06-30 23:56:50', '2021-06-30 23:56:50', NULL, 0, 655, 556, 0, 1, NULL, NULL),
	(254, '2021-07-01 00:00:15', '2021-07-01 00:00:15', NULL, 0, 656, 556, 0, 1, NULL, NULL),
	(255, '2021-07-01 00:02:15', '2021-07-01 00:02:15', NULL, 0, 657, 556, 0, 1, NULL, NULL),
	(256, '2021-07-01 00:04:09', '2021-07-01 00:04:09', NULL, 0, 658, 556, 0, 1, NULL, NULL),
	(257, '2021-07-01 00:14:02', '2021-07-01 00:14:02', NULL, 0, 659, 556, 0, 1, NULL, NULL),
	(258, '2021-07-01 00:15:55', '2021-07-01 00:15:55', NULL, 0, 660, 556, 0, 1, NULL, NULL),
	(259, '2021-07-01 00:19:12', '2021-07-01 00:19:12', NULL, 0, 661, 556, 0, 1, NULL, NULL),
	(260, '2021-07-01 00:22:03', '2021-07-01 00:22:03', NULL, 0, 662, 556, 0, 1, NULL, NULL),
	(261, '2021-07-01 00:22:52', '2021-07-01 00:22:52', NULL, 0, 663, 556, 0, 1, NULL, NULL),
	(262, '2021-07-01 00:24:06', '2021-07-01 00:24:06', NULL, 0, 664, 556, 0, 1, NULL, NULL),
	(263, '2021-07-01 12:49:22', '2021-07-01 12:49:22', NULL, 0, 665, 556, 0, 1, NULL, NULL),
	(264, '2021-07-01 13:27:42', '2021-07-01 13:27:42', NULL, 0, 666, 11, 149, 1, NULL, NULL),
	(265, '2021-07-01 13:27:52', '2021-07-01 13:27:52', NULL, 0, 667, 11, 149, 1, NULL, NULL),
	(266, '2021-07-05 23:11:50', '2021-07-05 23:11:50', NULL, 0, 669, 6, 154, 1, NULL, NULL),
	(267, '2021-07-05 23:16:29', '2021-07-05 23:16:29', NULL, 0, 670, 6, 154, 1, NULL, NULL),
	(268, '2021-07-05 23:17:51', '2021-07-05 23:17:51', NULL, 0, 671, 6, 154, 1, NULL, NULL),
	(269, '2021-07-05 23:18:31', '2021-07-05 23:18:31', NULL, 0, 672, 6, 155, 1, NULL, NULL),
	(270, '2021-07-06 08:18:52', '2021-07-06 08:18:52', NULL, 0, 673, 556, 0, 1, NULL, NULL),
	(271, '2021-07-07 20:30:18', '2021-07-07 20:30:18', NULL, 0, 674, 556, 0, 1, NULL, NULL),
	(272, '2021-07-07 20:32:22', '2021-07-07 20:32:22', NULL, 0, 675, 556, 0, 1, NULL, NULL),
	(273, '2021-07-07 21:19:59', '2021-07-07 21:19:59', NULL, 0, 676, 556, 0, 1, NULL, NULL),
	(274, '2021-07-07 21:21:15', '2021-07-07 21:21:15', NULL, 0, 677, 556, 0, 1, NULL, NULL),
	(275, '2021-07-07 23:35:55', '2021-07-07 23:35:55', NULL, 0, 678, 686, 0, 1, NULL, NULL),
	(276, '2021-07-07 23:38:24', '2021-07-07 23:38:24', NULL, 0, 679, 556, 0, 1, NULL, NULL),
	(277, '2021-07-07 23:40:05', '2021-07-07 23:40:05', NULL, 0, 680, 556, 0, 1, NULL, NULL),
	(278, '2021-07-07 23:42:55', '2021-07-07 23:42:55', NULL, 0, 681, 556, 0, 1, NULL, NULL),
	(279, '2021-07-07 23:43:42', '2021-07-07 23:43:42', NULL, 0, 682, 556, 0, 1, NULL, NULL),
	(280, '2021-07-12 20:46:19', '2021-07-12 20:46:19', NULL, 0, 683, 556, 160, 1, NULL, NULL),
	(281, '2021-07-12 22:08:42', '2021-07-12 22:08:42', NULL, 0, 684, 556, 161, 1, NULL, NULL),
	(282, '2021-07-13 09:06:00', '2021-07-13 09:06:00', NULL, 0, 685, 556, 161, 1, NULL, NULL),
	(283, '2021-07-13 09:18:41', '2021-07-13 09:18:41', NULL, 0, 686, 22, 0, 1, NULL, NULL),
	(284, '2021-07-13 09:19:51', '2021-07-13 09:19:51', NULL, 0, 687, 22, 0, 1, NULL, NULL),
	(285, '2021-07-14 18:54:02', '2021-07-14 18:54:02', NULL, 0, 688, 556, 160, 1, NULL, NULL),
	(286, '2021-07-14 18:54:12', '2021-07-14 18:54:12', NULL, 0, 689, 556, 161, 1, NULL, NULL),
	(287, '2021-07-14 20:59:07', '2021-07-14 20:59:07', NULL, 0, 690, 556, 161, 1, NULL, NULL),
	(288, '2021-07-14 20:59:40', '2021-07-14 20:59:40', NULL, 0, 691, 556, 161, 1, NULL, NULL),
	(289, '2021-07-14 21:35:54', '2021-07-14 21:35:54', NULL, 0, 692, 556, 162, 1, NULL, NULL),
	(290, '2021-07-14 21:36:57', '2021-07-14 21:36:57', NULL, 0, 693, 556, 162, 1, NULL, NULL),
	(291, '2021-07-14 21:39:03', '2021-07-14 21:39:03', NULL, 0, 694, 556, 162, 1, NULL, NULL),
	(292, '2021-07-14 21:42:00', '2021-07-14 21:42:00', NULL, 0, 695, 556, 162, 1, NULL, NULL),
	(293, '2021-07-14 21:42:36', '2021-07-14 21:42:36', NULL, 0, 696, 556, 162, 1, NULL, NULL),
	(294, '2021-07-14 21:44:24', '2021-07-14 21:44:24', NULL, 0, 697, 556, 162, 1, NULL, NULL),
	(295, '2021-07-14 21:46:06', '2021-07-14 21:46:06', NULL, 0, 698, 556, 162, 1, NULL, NULL),
	(296, '2021-07-14 21:48:23', '2021-07-14 21:48:23', NULL, 0, 699, 556, 162, 1, NULL, NULL),
	(297, '2021-07-14 21:52:43', '2021-07-14 21:52:43', NULL, 0, 700, 556, 162, 1, NULL, NULL),
	(298, '2021-07-14 21:53:47', '2021-07-14 21:53:47', NULL, 0, 701, 556, 162, 1, NULL, NULL),
	(299, '2021-07-14 21:55:47', '2021-07-14 21:55:47', NULL, 0, 702, 556, 162, 1, NULL, NULL),
	(300, '2021-07-14 21:59:48', '2021-07-14 21:59:48', NULL, 0, 703, 556, 162, 1, NULL, NULL),
	(301, '2021-07-14 22:07:06', '2021-07-14 22:07:06', NULL, 0, 705, 556, 162, 1, NULL, NULL),
	(302, '2021-07-14 22:37:12', '2021-07-14 22:37:12', NULL, 0, 706, 556, 164, 2, NULL, NULL),
	(303, '2021-07-14 23:07:55', '2021-07-14 23:07:55', NULL, 0, 707, 556, 164, 1, NULL, NULL),
	(304, '2021-07-14 23:13:54', '2021-07-14 23:13:54', NULL, 0, 708, 685, 0, 1, NULL, NULL),
	(305, '2021-07-15 07:46:10', '2021-07-15 07:46:10', NULL, 0, 709, 556, 164, 1, NULL, NULL),
	(306, '2021-07-15 13:29:54', '2021-07-15 13:29:54', NULL, 0, 710, 554, 0, 1, NULL, NULL),
	(307, '2021-07-15 13:33:33', '2021-07-15 13:33:33', NULL, 0, 711, 685, 0, 1, NULL, NULL),
	(308, '2021-07-15 13:34:34', '2021-07-15 13:34:34', NULL, 0, 712, 685, 0, 1, NULL, NULL),
	(309, '2021-07-15 13:35:39', '2021-07-15 13:35:39', NULL, 0, 713, 688, 0, 1, NULL, NULL),
	(310, '2021-07-15 13:36:54', '2021-07-15 13:36:54', NULL, 0, 714, 688, 0, 1, NULL, NULL),
	(311, '2021-08-16 21:27:40', '2021-08-16 21:27:40', NULL, 0, 715, 11, 144, 1, NULL, NULL),
	(312, '2021-10-14 22:06:21', '2021-10-14 22:06:21', NULL, 0, 716, 11, 144, 1, NULL, NULL);
/*!40000 ALTER TABLE `product__order` ENABLE KEYS */;

-- 导出  表 shop.pyshop_constant 结构
CREATE TABLE IF NOT EXISTS `pyshop_constant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `key` varchar(64) DEFAULT NULL,
  `value` varchar(128) DEFAULT NULL,
  `des` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.pyshop_constant 的数据：~7 rows (大约)
DELETE FROM `pyshop_constant`;
/*!40000 ALTER TABLE `pyshop_constant` DISABLE KEYS */;
INSERT INTO `pyshop_constant` (`id`, `create_time`, `update_time`, `remark`, `status`, `key`, `value`, `des`) VALUES
	(1, NULL, NULL, NULL, 0, 'serviceUrl', 'http://h5.heshihuan.cn/api', NULL),
	(2, NULL, NULL, NULL, NULL, 'localUrl', 'http://127.0.0.1:5000', NULL),
	(3, NULL, NULL, NULL, NULL, 'tempUrl', 'http://h5.heshihuan.cn/api', NULL),
	(4, '2021-06-02 13:40:48', '2021-07-07 20:26:14', NULL, 0, 'pay_ratio', '1', '支付比例，1代表分为单位，10代表角为单位，100代表元为单位'),
	(5, '2021-07-12 21:47:45', '2021-07-12 21:47:45', NULL, 0, 'notify_email', '370377860@qq.com', '提醒的邮箱，多个用逗号隔开'),
	(6, '2021-07-16 12:40:06', '2021-07-16 13:12:25', NULL, 0, 'blacklist', '61.151.207.158', '系统黑名单：拦截这些ip，不让访问系统'),
	(7, '2021-07-16 12:44:04', '2021-08-05 11:59:28', NULL, 0, 'isSendEmail', '2', '是否发送邮件，1为发送，2为不发送');
/*!40000 ALTER TABLE `pyshop_constant` ENABLE KEYS */;

-- 导出  表 shop.pzhoa__work_flow 结构
CREATE TABLE IF NOT EXISTS `pzhoa__work_flow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `workflowId` int(11) DEFAULT NULL,
  `flowName` varchar(128) DEFAULT NULL,
  `system` varchar(32) DEFAULT NULL,
  `canSync` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.pzhoa__work_flow 的数据：~20 rows (大约)
DELETE FROM `pzhoa__work_flow`;
/*!40000 ALTER TABLE `pzhoa__work_flow` DISABLE KEYS */;
INSERT INTO `pzhoa__work_flow` (`id`, `create_time`, `update_time`, `remark`, `status`, `workflowId`, `flowName`, `system`, `canSync`) VALUES
	(1, '2021-07-15 08:35:48', '2021-07-15 08:35:52', NULL, 0, 74521, 'DJRS-加班申请单(中午)', 'pzhhzp', 0),
	(2, '2021-07-15 08:36:00', '2021-07-15 08:42:35', NULL, 0, 43021, NULL, 'pzhhzp', 0),
	(3, '2021-07-15 08:36:09', '2021-07-15 08:42:44', NULL, 0, 42522, NULL, 'pzhhzp', 0),
	(4, '2021-07-15 08:36:16', '2021-07-15 08:42:56', NULL, 0, 64021, NULL, 'pzhhzp', 0),
	(5, '2021-07-15 08:36:23', '2021-07-15 08:43:00', NULL, 0, 69021, NULL, 'pzhhzp', 0),
	(6, '2021-07-15 08:36:31', '2021-07-15 08:43:03', NULL, 0, 68521, NULL, 'pzhhzp', 0),
	(7, '2021-07-15 08:36:37', '2021-07-15 08:43:07', NULL, 0, 59521, NULL, 'pzhhzp', 0),
	(8, '2021-07-15 08:36:42', '2021-07-16 13:26:37', '主管节点需要填内容', 0, 57521, 'QG-2.4部门月度考核', 'pzhhzp', 0),
	(9, '2021-07-15 08:36:48', '2021-07-15 08:43:16', NULL, 0, 18522, NULL, 'pzhhzp', 0),
	(10, '2021-07-15 08:37:09', '2021-07-15 08:43:20', NULL, 0, 26522, NULL, 'pzhhzp', 0),
	(11, '2021-07-15 08:37:24', '2021-07-15 08:43:24', NULL, 0, 32522, NULL, 'pzhhzp', 0),
	(12, '2021-07-15 08:41:28', '2021-07-15 08:43:34', NULL, 0, 27021, NULL, 'pzhhzp', 0),
	(13, '2021-07-15 08:41:37', '2021-07-15 08:43:48', NULL, 0, 38521, NULL, 'pzhhzp', 0),
	(14, '2021-07-15 08:41:44', '2021-07-15 08:43:52', NULL, 0, 62021, NULL, 'pzhhzp', 0),
	(15, '2021-07-15 08:41:50', '2021-07-15 08:43:59', NULL, 0, 51521, NULL, 'pzhhzp', 0),
	(16, '2021-07-15 08:42:01', '2021-07-15 08:44:04', NULL, 0, 52021, NULL, 'pzhhzp', 0),
	(17, '2021-07-15 08:42:16', '2021-07-15 08:44:09', NULL, 0, 44522, NULL, 'pzhhzp', 0),
	(18, '2021-07-15 08:42:24', '2021-07-15 08:44:15', NULL, 0, 56521, NULL, 'pzhhzp', 0),
	(19, '2021-07-15 15:08:18', '2021-07-15 15:08:18', NULL, 0, 47021, 'CC-车辆维修申请单', 'pzhhzp', 0),
	(20, '2021-07-23 11:33:09', '2021-07-23 11:33:09', NULL, 0, 104521, 'ERP领料单', 'pzhhzp', 0);
/*!40000 ALTER TABLE `pzhoa__work_flow` ENABLE KEYS */;

-- 导出  表 shop.pzh_constant 结构
CREATE TABLE IF NOT EXISTS `pzh_constant` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `erpVersion` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.pzh_constant 的数据：~0 rows (大约)
DELETE FROM `pzh_constant`;
/*!40000 ALTER TABLE `pzh_constant` DISABLE KEYS */;
INSERT INTO `pzh_constant` (`create_time`, `update_time`, `remark`, `status`, `id`, `erpVersion`) VALUES
	(NULL, NULL, NULL, 1, 1, '20210219');
/*!40000 ALTER TABLE `pzh_constant` ENABLE KEYS */;

-- 导出  表 shop.quant__recommend_stock 结构
CREATE TABLE IF NOT EXISTS `quant__recommend_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `code` varchar(32) DEFAULT NULL,
  `codeName` varchar(64) DEFAULT NULL,
  `date` varchar(512) DEFAULT NULL,
  `roa` float DEFAULT NULL,
  `PER` float DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `nextday` float DEFAULT NULL,
  `nextday2` float DEFAULT NULL,
  `nextday3` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=405 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.quant__recommend_stock 的数据：~275 rows (大约)
DELETE FROM `quant__recommend_stock`;
/*!40000 ALTER TABLE `quant__recommend_stock` DISABLE KEYS */;
INSERT INTO `quant__recommend_stock` (`id`, `create_time`, `update_time`, `remark`, `status`, `code`, `codeName`, `date`, `roa`, `PER`, `size`, `price`, `nextday`, `nextday2`, `nextday3`) VALUES
	(130, '2021-10-14 13:06:49', '2021-10-14 16:23:59', NULL, -2, '000002.SZ', '万科A', '2021-10-14', 0, 0, 100, 21.54, NULL, NULL, NULL),
	(131, '2021-10-14 13:06:49', '2021-10-14 13:14:42', NULL, -2, '000002.SZ', '万科A', '2021-10-14', 0, 0, 100, 21.54, NULL, NULL, NULL),
	(132, '2021-10-14 13:06:50', '2021-10-14 13:14:43', NULL, -2, '000423.SZ', '东阿阿胶', '2021-10-14', 0, 0, 100, 35.77, NULL, NULL, NULL),
/*!40000 ALTER TABLE `quant__recommend_stock` ENABLE KEYS */;

-- 导出  表 shop.rate 结构
CREATE TABLE IF NOT EXISTS `rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `userid` varchar(32) DEFAULT NULL,
  `rate` int(11) DEFAULT NULL,
  `describeRate` int(11) DEFAULT NULL,
  `logisticsRate` int(11) DEFAULT NULL,
  `serviceRate` int(11) DEFAULT NULL,
  `evaluate` varchar(256) DEFAULT NULL,
  `content` varchar(2048) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL,
  `award` varchar(1024) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `propid` int(11) DEFAULT NULL,
  `basename` varchar(128) DEFAULT NULL,
  `funame` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.rate 的数据：~10 rows (大约)
DELETE FROM `rate`;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` (`id`, `create_time`, `update_time`, `remark`, `status`, `userid`, `rate`, `describeRate`, `logisticsRate`, `serviceRate`, `evaluate`, `content`, `orderid`, `award`, `productid`, `propid`, `basename`, `funame`) VALUES
	(47, '2021-03-03 23:06:30', '2021-03-03 23:06:30', NULL, 0, '24', NULL, 5, 5, 5, '好牛逼的感觉，是不是小程序、App、移动端都互通了？', NULL, 383, NULL, 6, 32, NULL, NULL),
	(48, '2021-03-03 23:06:36', '2021-03-03 23:06:36', NULL, 0, '24', NULL, 5, 5, 5, '很强大，厉害了我的uni-app!', NULL, 383, NULL, 6, 32, NULL, NULL),
	(49, '2021-03-03 23:06:37', '2021-03-03 23:06:37', NULL, 0, '24', NULL, 5, 5, 5, '支持国产，支持DCloud!', NULL, 383, NULL, 6, 32, NULL, NULL),
	(50, '2021-03-03 23:07:00', '2021-03-03 23:07:00', NULL, 0, '24', NULL, 5, 5, 5, '花很好', NULL, 383, NULL, 6, 32, NULL, NULL),
	(51, '2021-03-04 00:18:51', '2021-03-04 00:18:51', NULL, 0, '24', NULL, 2, 4, 4, '好东西', NULL, NULL, NULL, NULL, 32, NULL, NULL),
	(52, '2021-03-04 23:12:45', '2021-03-04 23:12:45', NULL, 0, '24', NULL, 3, 5, 5, '宋梅非常好，我很喜欢', NULL, 393, NULL, 11, 32, NULL, NULL),
	(53, '2021-03-07 00:01:04', '2021-03-07 00:01:04', NULL, 0, '24', NULL, 5, 5, 5, '大一品的评价', NULL, 416, NULL, 22, 0, NULL, NULL),
	(54, '2021-03-07 09:17:11', '2021-03-07 09:17:11', NULL, 0, '24', NULL, 4, 5, 5, '八宝奇珍评价', NULL, 424, NULL, 554, 0, NULL, NULL),
	(55, '2021-03-20 08:39:11', '2021-03-20 08:39:11', NULL, 0, '24', NULL, 3, 2, 4, '很好，很强大', NULL, 520, NULL, 11, 147, NULL, NULL),
	(56, '2021-03-21 21:25:12', '2021-03-21 21:25:12', NULL, 0, '50', NULL, 4, 5, 5, '很好的花。超级喜欢', NULL, 552, NULL, 11, 146, NULL, NULL),
	(57, '2021-07-12 20:46:58', '2021-07-12 20:46:58', NULL, 0, '146', NULL, 4, 5, 5, '', NULL, 677, NULL, 556, 0, NULL, NULL),
	(58, '2021-07-12 20:47:14', '2021-07-12 20:47:14', NULL, 0, '146', NULL, 3, 5, 5, '好东西', NULL, 678, NULL, 686, 0, NULL, NULL);
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;

-- 导出  表 shop.request_log 结构
CREATE TABLE IF NOT EXISTS `request_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `key` varchar(1024) DEFAULT NULL,
  `ip` varchar(128) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.request_log 的数据：~21 rows (大约)
DELETE FROM `request_log`;
/*!40000 ALTER TABLE `request_log` DISABLE KEYS */;
INSERT INTO `request_log` (`id`, `create_time`, `update_time`, `remark`, `status`, `key`, `ip`, `type`, `content`) VALUES
	(1, '2021-10-09 17:35:38', '2021-10-09 17:35:38', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/common/model/add/?modelName=Quant_RecommendStock&code=123&codeName=3456 error info: module \'model.netModels\' has no attribute \'Quant_RecommendStock\''),
	(2, '2021-10-09 17:36:18', '2021-10-09 17:36:18', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/common/model/add/?modelName=Quant_RecommendStock&code=123&codeName=3456 error info: module \'model.netModels\' has no attribute \'Quant_RecommendStock\''),
	(3, '2021-10-09 17:44:54', '2021-10-09 17:44:54', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/common/model/add/?modelName=Quant_RecommendStock&code=123&codeName=3456 error info: module \'model.netModels\' has no attribute \'Quant_RecommendStock\''),
	(4, '2021-10-09 17:46:23', '2021-10-09 17:46:23', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/common/model/add/?modelName=Quant_RecommendStock&code=123&codeName=3456 error info: module \'model.netModels\' has no attribute \'Quant_RecommendStock\''),
	(5, '2021-10-09 17:46:45', '2021-10-09 17:46:45', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/common/model/add/?modelName=Quant_RecommendStock&code=123&codeName=3456 error info: module \'model.netModels\' has no attribute \'Quant_RecommendStock\''),
	(6, '2021-10-14 17:50:30', '2021-10-14 17:50:30', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stock_date?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(7, '2021-10-14 17:51:06', '2021-10-14 17:51:06', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stock_date?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(8, '2021-10-14 17:53:33', '2021-10-14 17:53:33', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stock_date?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(9, '2021-10-14 17:56:04', '2021-10-14 17:56:04', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(10, '2021-10-14 17:57:20', '2021-10-14 17:57:20', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(11, '2021-10-14 17:58:33', '2021-10-14 17:58:33', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate?date=2021-08-09 error info: stockData() missing 1 required positional argument: \'date\''),
	(12, '2021-10-14 18:06:34', '2021-10-14 18:06:34', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate%3D%272%27 error info: 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'),
	(13, '2021-10-14 18:06:41', '2021-10-14 18:06:41', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate%3D5 error info: 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'),
	(14, '2021-10-15 08:52:04', '2021-10-15 08:52:04', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate error info: local variable \'quant\' referenced before assignment'),
	(15, '2021-10-15 10:46:21', '2021-10-15 10:46:21', NULL, 0, 'k-shop系统异常提醒', '370377860@qq.com', NULL, '[\'127.0.0.1\'] http://127.0.0.1:4999/timer/stockDate?startdate=2021-10-14&enddate=2021-10-15 error info: 找不到标的000002.SZ'),
	(16, '2021-10-18 16:01:29', '2021-10-18 16:01:29', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗触发交易'),
	(17, '2021-10-18 16:05:57', '2021-10-18 16:05:57', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗触发交易'),
	(18, '2021-10-18 16:09:46', '2021-10-18 16:09:46', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗价格为：50.05'),
	(19, '2021-10-18 16:26:48', '2021-10-18 16:26:48', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗价格为：50.05'),
	(20, '2021-10-18 16:43:52', '2021-10-18 16:43:52', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗价格为：50.05'),
	(21, '2021-10-18 17:00:56', '2021-10-18 17:00:56', NULL, 0, '量化提醒', '370377860@qq.com', NULL, '恒瑞医疗价格为：50.05');
/*!40000 ALTER TABLE `request_log` ENABLE KEYS */;

-- 导出  表 shop.skufirst 结构
CREATE TABLE IF NOT EXISTS `skufirst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` varchar(32) DEFAULT NULL,
  `baseid` int(11) DEFAULT NULL,
  `basename` varchar(128) DEFAULT NULL,
  `fuid` int(11) DEFAULT NULL,
  `funame` varchar(128) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.skufirst 的数据：~8 rows (大约)
DELETE FROM `skufirst`;
/*!40000 ALTER TABLE `skufirst` DISABLE KEYS */;
INSERT INTO `skufirst` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `baseid`, `basename`, `fuid`, `funame`, `pic`) VALUES
	(2, '2019-08-24 16:28:15', '2019-08-24 16:28:15', NULL, 0, '123', 2, '颜色', 2, '颜色', NULL),
	(3, '2019-08-24 18:12:25', '2019-08-24 18:12:25', NULL, 0, '5', 0, '无选择', 0, '无选择', NULL),
	(8, '2019-09-30 23:35:45', '2019-09-30 23:35:45', NULL, 0, '0', 1, '数量', 4, '是否含盆', NULL),
	(14, '2021-03-01 12:48:34', '2021-03-01 12:48:34', NULL, 0, '44', 0, '无选择', 0, '无选择', NULL),
	(16, '2021-03-01 12:49:57', '2021-03-01 12:49:57', NULL, 0, '681', 0, '无选择', 0, '无选择', NULL),
	(38, '2021-03-19 21:27:27', '2021-03-19 21:27:27', NULL, 0, '11', 1, '苗数', 2, '是否含盆', NULL),
	(43, '2021-07-12 19:57:08', '2021-07-12 19:57:08', NULL, 0, '6', 1, '苗数', 2, '含盆', NULL),
	(46, '2021-07-14 22:23:15', '2021-07-14 22:23:15', NULL, 0, '556', 1, '颜色', 2, '是否含盆', NULL);
/*!40000 ALTER TABLE `skufirst` ENABLE KEYS */;

-- 导出  表 shop.skusecond 结构
CREATE TABLE IF NOT EXISTS `skusecond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` varchar(32) DEFAULT NULL,
  `propertyid` int(11) DEFAULT NULL,
  `propertyname` varchar(128) DEFAULT NULL,
  `firstid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=192 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.skusecond 的数据：~28 rows (大约)
DELETE FROM `skusecond`;
/*!40000 ALTER TABLE `skusecond` DISABLE KEYS */;
INSERT INTO `skusecond` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `propertyid`, `propertyname`, `firstid`) VALUES
	(4, '2019-08-24 16:28:09', '2019-08-24 16:28:09', NULL, 0, '123', 11, '一苗', 2),
	(5, '2019-08-24 16:28:15', '2019-08-24 16:28:15', NULL, 0, '123', 41, '含盆', 2),
	(6, '2019-08-24 16:28:15', '2019-08-24 16:28:15', NULL, 0, '123', 42, '不含盆', 2),
	(7, '2019-08-24 18:12:24', '2019-08-24 18:12:24', NULL, 0, '5', 11, '一苗', 0),
	(8, '2019-08-24 18:12:25', '2019-08-24 18:12:25', NULL, 0, '5', 12, '2苗', 0),
	(9, '2019-08-24 18:12:25', '2019-08-24 18:12:25', NULL, 0, '5', 41, '含盆', 0),
	(25, '2019-09-30 23:35:43', '2019-09-30 23:35:43', NULL, 0, '0', 11, '一苗', 1),
	(26, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 12, '2苗', 1),
	(27, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 13, '3苗', 1),
	(28, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 14, '4苗', 1),
	(29, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 15, '5苗', 1),
	(30, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 42, '不含盆', 4),
	(48, '2021-03-01 12:48:33', '2021-03-01 12:48:33', NULL, 0, '44', 11, '一苗', 0),
	(49, '2021-03-01 12:48:33', '2021-03-01 12:48:33', NULL, 0, '44', 41, '含盆', 0),
	(52, '2021-03-01 12:49:57', '2021-03-01 12:49:57', NULL, 0, '681', 11, '一苗', 0),
	(53, '2021-03-01 12:49:57', '2021-03-01 12:49:57', NULL, 0, '681', 41, '含盆', 0),
	(158, '2021-03-19 21:27:23', '2021-03-19 21:27:23', NULL, 0, '11', 11, '1苗', 1),
	(159, '2021-03-19 21:27:24', '2021-03-19 21:27:24', NULL, 0, '11', 12, '2苗', 1),
	(160, '2021-03-19 21:27:24', '2021-03-19 21:27:24', NULL, 0, '11', 13, '3苗', 1),
	(161, '2021-03-19 21:27:24', '2021-03-19 21:27:24', NULL, 0, '11', 41, '不含盆', 2),
	(162, '2021-03-19 21:27:25', '2021-03-19 21:27:25', NULL, 0, '11', 42, '含盆', 2),
	(175, '2021-07-12 19:57:07', '2021-07-12 19:57:07', NULL, 0, '6', 11, '2苗', 1),
	(176, '2021-07-12 19:57:07', '2021-07-12 19:57:07', NULL, 0, '6', 12, '3苗', 1),
	(177, '2021-07-12 19:57:07', '2021-07-12 19:57:07', NULL, 0, '6', 13, '4苗', 1),
	(178, '2021-07-12 19:57:08', '2021-07-12 19:57:08', NULL, 0, '6', 41, '不含盆', 2),
	(189, '2021-07-14 22:23:14', '2021-07-14 22:23:14', NULL, 0, '556', 11, '1苗', 1),
	(190, '2021-07-14 22:23:15', '2021-07-14 22:23:15', NULL, 0, '556', 12, '2苗', 1),
	(191, '2021-07-14 22:23:15', '2021-07-14 22:23:15', NULL, 0, '556', 41, '不含盆', 2);
/*!40000 ALTER TABLE `skusecond` ENABLE KEYS */;

-- 导出  表 shop.skuthird 结构
CREATE TABLE IF NOT EXISTS `skuthird` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` varchar(32) DEFAULT NULL,
  `baseid` int(11) DEFAULT NULL,
  `basename` varchar(128) DEFAULT NULL,
  `fuid` int(11) DEFAULT NULL,
  `funame` varchar(128) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `store` int(11) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.skuthird 的数据：~24 rows (大约)
DELETE FROM `skuthird`;
/*!40000 ALTER TABLE `skuthird` DISABLE KEYS */;
INSERT INTO `skuthird` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `baseid`, `basename`, `fuid`, `funame`, `price`, `store`, `pic`) VALUES
	(3, '2019-08-24 16:28:15', '2019-08-24 16:28:15', NULL, 0, '123', 11, '一苗', 41, '含盆', 2, 3, NULL),
	(4, '2019-08-24 16:28:15', '2019-08-24 16:28:15', NULL, 0, '123', 11, '一苗', 42, '不含盆', 2, 3, NULL),
	(5, '2019-08-24 18:12:25', '2019-08-24 18:12:25', NULL, 0, '5', 11, '一苗', 41, '含盆', 1, 11, NULL),
	(6, '2019-08-24 18:12:25', '2019-08-24 18:12:25', NULL, 0, '5', 12, '2苗', 41, '含盆', 2, 11, NULL),
	(20, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 11, '一苗', 42, '不含盆', 10, 100, NULL),
	(21, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 12, '2苗', 42, '不含盆', 20, 100, NULL),
	(22, '2019-09-30 23:35:44', '2019-09-30 23:35:44', NULL, 0, '0', 13, '3苗', 42, '不含盆', 30, 100, NULL),
	(23, '2019-09-30 23:35:45', '2019-09-30 23:35:45', NULL, 0, '0', 14, '4苗', 42, '不含盆', 40, 100, NULL),
	(24, '2019-09-30 23:35:45', '2019-09-30 23:35:45', NULL, 0, '0', 15, '5苗', 42, '不含盆', 50, 100, NULL),
	(39, '2021-03-01 12:48:33', '2021-03-01 12:48:33', NULL, 0, '44', 11, '一苗', 42, '不含盆', 2232, 2, NULL),
	(40, '2021-03-01 12:48:34', '2021-03-01 12:48:34', NULL, 0, '44', 12, '2苗', 42, '不含盆', 44, 3, NULL),
	(41, '2021-03-01 12:48:34', '2021-03-01 12:48:34', NULL, 0, '44', 13, '3苗', 42, '不含盆', 66, 2, NULL),
	(43, '2021-03-01 12:49:57', '2021-03-01 12:49:57', NULL, 0, '681', 11, '一苗', 42, '不含盆', 1, 1, NULL),
	(144, '2021-03-19 21:27:25', '2021-03-19 21:27:25', NULL, 0, '11', 11, '1苗', 41, '不含盆', 121, 32, 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202103190049152205.jpg'),
	(145, '2021-03-19 21:27:25', '2021-03-19 21:27:25', NULL, 0, '11', 11, '1苗', 42, '含盆', 2, 2, NULL),
	(146, '2021-03-19 21:27:26', '2021-03-19 21:27:26', NULL, 0, '11', 12, '2苗', 41, '不含盆', 1, 1, 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202103190121103918.jpg'),
	(147, '2021-03-19 21:27:26', '2021-03-19 21:27:26', NULL, 0, '11', 12, '2苗', 42, '含盆', 2, 2, NULL),
	(148, '2021-03-19 21:27:26', '2021-03-19 21:27:26', NULL, 0, '11', 13, '3苗', 41, '不含盆', 2, 3, NULL),
	(149, '2021-03-19 21:27:26', '2021-03-19 21:27:26', NULL, 0, '11', 13, '3苗', 42, '含盆', 2, 2, NULL),
	(157, '2021-07-12 19:57:08', '2021-07-12 19:57:08', NULL, 0, '6', 11, '2苗', 41, '不含盆', 18, 100, 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202107121957038454.jpg'),
	(158, '2021-07-12 19:57:08', '2021-07-12 19:57:08', NULL, 0, '6', 12, '3苗', 41, '不含盆', 27, 100, NULL),
	(159, '2021-07-12 19:57:08', '2021-07-12 19:57:08', NULL, 0, '6', 13, '4苗', 41, '不含盆', 36, 100, NULL),
	(164, '2021-07-14 22:23:15', '2021-07-15 07:46:24', NULL, 0, '556', 11, '1苗', 41, '不含盆', 1, 0, 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202107142102554970.jpg'),
	(165, '2021-07-14 22:23:15', '2021-07-14 22:23:15', NULL, 0, '556', 12, '2苗', 41, '不含盆', 2, 1, NULL);
/*!40000 ALTER TABLE `skuthird` ENABLE KEYS */;

-- 导出  表 shop.to_do__list 结构
CREATE TABLE IF NOT EXISTS `to_do__list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user` int(11) DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `tasktype` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `content` text,
  `author` int(11) DEFAULT NULL,
  `file_url` varchar(256) DEFAULT NULL,
  `is_finish` tinyint(1) DEFAULT NULL,
  `dealMethod` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.to_do__list 的数据：~162 rows (大约)
DELETE FROM `to_do__list`;
/*!40000 ALTER TABLE `to_do__list` DISABLE KEYS */;


-- 导出  表 shop.to_do__type 结构
CREATE TABLE IF NOT EXISTS `to_do__type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `type_name` varchar(64) DEFAULT NULL,
  `type_des` varchar(128) DEFAULT NULL,
  `is_use` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.to_do__type 的数据：~6 rows (大约)
DELETE FROM `to_do__type`;
/*!40000 ALTER TABLE `to_do__type` DISABLE KEYS */;
INSERT INTO `to_do__type` (`id`, `create_time`, `update_time`, `remark`, `status`, `type_name`, `type_des`, `is_use`) VALUES
	(1, '2021-04-12 11:46:43', '2021-04-12 11:46:43', NULL, 0, '泛微OA待办', '泛微待办', 1),
	(2, '2021-04-12 11:50:21', '2021-04-14 15:10:02', NULL, 0, '生活待办', NULL, 1),
	(3, '2021-04-13 08:16:37', '2021-05-30 23:11:12', NULL, 0, '蜜熊', '蜜熊网络科技待办', 1),
	(4, '2021-04-13 09:24:00', '2021-04-13 09:24:00', NULL, 0, '片仔癀', '片仔癀公司工作内容', 1),
	(5, '2021-05-30 13:32:33', '2021-08-10 08:34:00', NULL, 0, '化妆品研发与法规管理软件', '化妆品研发与法规管理软件', 1),
	(6, '2021-05-30 13:34:18', '2021-08-03 11:29:35', NULL, 0, 't2', NULL, 0);
/*!40000 ALTER TABLE `to_do__type` ENABLE KEYS */;

-- 导出  表 shop.user 结构
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `mobile` varchar(64) DEFAULT NULL,
  `phone` varchar(64) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `portrait` varchar(64) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `openid` varchar(64) DEFAULT NULL,
  `age` int(3) DEFAULT NULL COMMENT '年龄',
  `address` varchar(255) DEFAULT NULL COMMENT '联系地址',
  `signature` varchar(255) DEFAULT NULL COMMENT '个性签名',
  `credit` int(255) DEFAULT '0',
  `openid_mp` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=351 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.user 的数据：~294 rows (大约)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `create_time`, `update_time`, `remark`, `status`, `username`, `password`, `mobile`, `phone`, `name`, `portrait`, `nickname`, `openid`, `age`, `address`, `signature`, `credit`, `openid_mp`) VALUES
	(51, '2021-03-22 14:38:31', '2021-03-22 14:38:31', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1QfYharJwLasJtq6V9zftOI', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(56, '2021-04-20 18:28:48', '2021-04-20 18:28:48', NULL, 0, 'admin', 'admin', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(58, '2021-04-20 19:58:50', '2021-04-20 19:58:50', NULL, 0, 'home', 'home', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(59, '2021-04-20 19:59:40', '2021-04-20 19:59:40', NULL, 0, '456', '456', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(61, '2021-04-20 21:11:57', '2021-04-20 21:11:57', NULL, 0, '', '', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(62, '2021-04-20 21:12:57', '2021-04-20 21:12:57', NULL, 0, '12', '12', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(63, '2021-05-06 08:41:15', '2021-05-06 08:41:15', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1VJy84rkevpk-2Qzx050zpc', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(64, '2021-05-13 08:26:38', '2021-05-13 08:26:38', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1fwQN5uCaCUVu46OOjZ1Rg8', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(65, '2021-05-13 11:53:25', '2021-05-13 11:53:25', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1fOQYZTBc3n_QvV2oWfWUP4', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(66, '2021-05-16 15:12:49', '2021-05-16 15:12:49', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1Ryq0lWUwA3vclbD6X1-Gco', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(67, '2021-05-17 11:52:32', '2021-05-17 11:52:32', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1R8Y1LNcs21mYutjffsGqgU', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(68, '2021-05-17 14:53:36', '2021-05-17 14:53:36', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1RPJ-RvcMp9Tw5qiuwLfnlk', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(69, '2021-05-20 06:23:24', '2021-05-20 06:23:24', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1fsYk2SBn-atV8ZTH2o7c_M', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(70, '2021-05-20 13:21:34', '2021-05-20 13:21:34', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 'oUrkV', 'oUrkV1ajnvvI6_NTlZmADdGMTHA0', 18, NULL, '这个人很懒，什么都没留下', 0, NULL),
	(350, '2021-10-28 11:08:52', '2021-10-28 11:08:52', NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, '蜜熊YMN', NULL, 18, NULL, '这个人很懒，什么都没留下', 0, 'oo0m04kU0_YMNX_PkH8n_g6hwlNA');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

-- 导出  表 shop.user2product 结构
CREATE TABLE IF NOT EXISTS `user2product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `operate` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.user2product 的数据：~7 rows (大约)
DELETE FROM `user2product`;
/*!40000 ALTER TABLE `user2product` DISABLE KEYS */;
INSERT INTO `user2product` (`id`, `create_time`, `update_time`, `remark`, `status`, `productid`, `userid`, `operate`) VALUES
	(1, '2019-07-30 23:53:55', '2019-07-30 23:53:55', NULL, 0, 11, 0, NULL),
	(2, '2019-07-30 23:54:26', '2019-07-30 23:54:26', NULL, 0, 11, 0, NULL),
	(4, '2019-08-03 06:14:55', '2019-08-03 06:14:55', NULL, 0, 436, 2, NULL),
	(5, '2019-08-03 09:40:05', '2019-08-03 09:40:05', NULL, 0, 6, 2, NULL),
	(6, '2019-08-17 18:32:05', '2019-08-17 18:32:05', NULL, 0, 11, 2, NULL),
	(19, '2021-01-22 16:48:22', '2021-01-22 16:48:22', NULL, 0, 23, NULL, 2),
	(38, '2021-02-26 16:57:54', '2021-02-26 16:57:54', NULL, 0, 33, 24, 2);
/*!40000 ALTER TABLE `user2product` ENABLE KEYS */;

-- 导出  视图 shop.order_v 结构
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `order_v`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `order_v` AS select `o`.`id` AS `id`,`o`.`userid` AS `userid`,`o`.`addressId` AS `addressId`,`o`.`create_time` AS `create_time`,`o`.`update_time` AS `update_time`,`o`.`pruductPriceCount` AS `pruductPriceCount`,`o`.`discount` AS `discount`,`o`.`yunfei` AS `yunfei`,`o`.`status` AS `status`,`o`.`remark` AS `remark`,`o`.`orderRemark` AS `orderRemark`,`o`.`orderChangeStatus` AS `orderChangeStatus`,`o`.`orderStatus` AS `orderStatus`,`o`.`mount` AS `mount`,`o`.`orderNo` AS `orderNo`,`o`.`logisticsNo` AS `logisticsNo`,`o`.`needHelp` AS `needHelp`,`o`.`logisticsType` AS `logisticsType`,`u`.`name` AS `name`,`u`.`username` AS `username`,`u`.`nickname` AS `nickname`,`a`.`mobile` AS `mobile`,`a`.`receiver` AS `receiver`,`a`.`address` AS `address`,`a`.`area` AS `area` from ((`order` `o` left join `user` `u` on((`o`.`userid` = `u`.`id`))) left join `address` `a` on((`o`.`addressId` = `a`.`id`)));

-- 导出  视图 shop.product_order_v 结构
-- 移除临时表并创建最终视图结构
DROP TABLE IF EXISTS `product_order_v`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `product_order_v` AS select `t1`.`id` AS `id`,`t1`.`productid` AS `productid`,`t1`.`orderid` AS `orderid`,`t1`.`mount` AS `mount`,`t3`.`basename` AS `basename`,`t3`.`funame` AS `funame`,`t2`.`title` AS `title`,`t2`.`main_image` AS `main_image`,`t1`.`propid` AS `propid`,`t2`.`image800` AS `image800`,`t2`.`image400` AS `image400`,`t2`.`image200` AS `image200`,`t2`.`image100` AS `image100`,`t2`.`price` AS `price`,`t2`.`size` AS `size`,`t2`.`color` AS `color`,`t1`.`create_time` AS `create_time`,`t1`.`update_time` AS `update_time`,`t1`.`remark` AS `remark`,`t1`.`status` AS `status` from ((`product__order` `t1` left join `product` `t2` on((`t1`.`productid` = `t2`.`id`))) left join `skuthird` `t3` on((`t1`.`propid` = `t3`.`id`)));

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
