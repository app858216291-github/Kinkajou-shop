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


-- 导出 kinkajou 的数据库结构
CREATE DATABASE IF NOT EXISTS `kinkajou` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `kinkajou`;

-- 导出  表 kinkajou.address 结构
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `orderId` int(11) DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `mobile` varchar(128) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `area` varchar(64) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.address 的数据：~0 rows (大约)
DELETE FROM `address`;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
/*!40000 ALTER TABLE `address` ENABLE KEYS */;

-- 导出  表 kinkajou.admin__user 结构
CREATE TABLE IF NOT EXISTS `admin__user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.admin__user 的数据：~0 rows (大约)
DELETE FROM `admin__user`;
/*!40000 ALTER TABLE `admin__user` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin__user` ENABLE KEYS */;

-- 导出  表 kinkajou.after_sales 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.after_sales 的数据：~0 rows (大约)
DELETE FROM `after_sales`;
/*!40000 ALTER TABLE `after_sales` DISABLE KEYS */;
/*!40000 ALTER TABLE `after_sales` ENABLE KEYS */;

-- 导出  表 kinkajou.brown_his 结构
CREATE TABLE IF NOT EXISTS `brown_his` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.brown_his 的数据：~0 rows (大约)
DELETE FROM `brown_his`;
/*!40000 ALTER TABLE `brown_his` DISABLE KEYS */;
/*!40000 ALTER TABLE `brown_his` ENABLE KEYS */;

-- 导出  表 kinkajou.car 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.car 的数据：~0 rows (大约)
DELETE FROM `car`;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
/*!40000 ALTER TABLE `car` ENABLE KEYS */;

-- 导出  表 kinkajou.category 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.category 的数据：~0 rows (大约)
DELETE FROM `category`;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;

-- 导出  表 kinkajou.dict_config 结构
CREATE TABLE IF NOT EXISTS `dict_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `key` int(11) DEFAULT NULL,
  `keyStr` varchar(64) DEFAULT NULL,
  `value` varchar(128) DEFAULT NULL,
  `desc` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.dict_config 的数据：~0 rows (大约)
DELETE FROM `dict_config`;
/*!40000 ALTER TABLE `dict_config` DISABLE KEYS */;
/*!40000 ALTER TABLE `dict_config` ENABLE KEYS */;

-- 导出  表 kinkajou.haopin 结构
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

-- 正在导出表  kinkajou.haopin 的数据：~0 rows (大约)
DELETE FROM `haopin`;
/*!40000 ALTER TABLE `haopin` DISABLE KEYS */;
/*!40000 ALTER TABLE `haopin` ENABLE KEYS */;

-- 导出  表 kinkajou.images 结构
CREATE TABLE IF NOT EXISTS `images` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.images 的数据：~0 rows (大约)
DELETE FROM `images`;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
/*!40000 ALTER TABLE `images` ENABLE KEYS */;

-- 导出  表 kinkajou.net__category 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__category 的数据：~0 rows (大约)
DELETE FROM `net__category`;
/*!40000 ALTER TABLE `net__category` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__category` ENABLE KEYS */;

-- 导出  表 kinkajou.net__company_info 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__company_info 的数据：~0 rows (大约)
DELETE FROM `net__company_info`;
/*!40000 ALTER TABLE `net__company_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__company_info` ENABLE KEYS */;

-- 导出  表 kinkajou.net__contact 结构
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
  `x` varchar(32) DEFAULT NULL,
  `y` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__contact 的数据：~0 rows (大约)
DELETE FROM `net__contact`;
/*!40000 ALTER TABLE `net__contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__contact` ENABLE KEYS */;

-- 导出  表 kinkajou.net__honour 结构
CREATE TABLE IF NOT EXISTS `net__honour` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `time` varchar(128) DEFAULT NULL,
  `content` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__honour 的数据：~0 rows (大约)
DELETE FROM `net__honour`;
/*!40000 ALTER TABLE `net__honour` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__honour` ENABLE KEYS */;

-- 导出  表 kinkajou.net__message_board 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__message_board 的数据：~0 rows (大约)
DELETE FROM `net__message_board`;
/*!40000 ALTER TABLE `net__message_board` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__message_board` ENABLE KEYS */;

-- 导出  表 kinkajou.net__news 结构
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__news 的数据：~0 rows (大约)
DELETE FROM `net__news`;
/*!40000 ALTER TABLE `net__news` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__news` ENABLE KEYS */;

-- 导出  表 kinkajou.net__product_info 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.net__product_info 的数据：~0 rows (大约)
DELETE FROM `net__product_info`;
/*!40000 ALTER TABLE `net__product_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `net__product_info` ENABLE KEYS */;

-- 导出  表 kinkajou.order 结构
CREATE TABLE IF NOT EXISTS `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `orderNo` varchar(128) DEFAULT NULL,
  `pruductPriceCount` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `yunfei` float DEFAULT NULL,
  `orderRemark` varchar(512) DEFAULT NULL,
  `mount` float DEFAULT NULL,
  `orderStatus` int(11) DEFAULT NULL,
  `orderChangeStatus` int(11) DEFAULT NULL,
  `logisticsNo` varchar(64) DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  `addressId` int(11) DEFAULT NULL,
  `needHelp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.order 的数据：~0 rows (大约)
DELETE FROM `order`;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;

-- 导出  表 kinkajou.pay_record 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.pay_record 的数据：~0 rows (大约)
DELETE FROM `pay_record`;
/*!40000 ALTER TABLE `pay_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay_record` ENABLE KEYS */;

-- 导出  表 kinkajou.product 结构
CREATE TABLE IF NOT EXISTS `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `orderId` int(11) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `main_image` varchar(4096) DEFAULT NULL,
  `detail_image` varchar(4096) DEFAULT NULL,
  `image800` varchar(512) DEFAULT NULL,
  `image400` varchar(512) DEFAULT NULL,
  `image200` varchar(512) DEFAULT NULL,
  `image100` varchar(512) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `sales` int(11) DEFAULT NULL,
  `store` int(11) DEFAULT NULL,
  `brownCount` int(11) DEFAULT NULL,
  `size` varchar(64) DEFAULT NULL,
  `color` varchar(64) DEFAULT NULL,
  `category` varchar(16) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `propId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.product 的数据：~0 rows (大约)
DELETE FROM `product`;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- 导出  表 kinkajou.product_order_v 结构
CREATE TABLE IF NOT EXISTS `product_order_v` (
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
  `funame` varchar(64) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `main_image` varchar(64) DEFAULT NULL,
  `image800` varchar(64) DEFAULT NULL,
  `image400` varchar(64) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `size` varchar(64) DEFAULT NULL,
  `color` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.product_order_v 的数据：~0 rows (大约)
DELETE FROM `product_order_v`;
/*!40000 ALTER TABLE `product_order_v` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_order_v` ENABLE KEYS */;

-- 导出  表 kinkajou.product__order 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.product__order 的数据：~0 rows (大约)
DELETE FROM `product__order`;
/*!40000 ALTER TABLE `product__order` DISABLE KEYS */;
/*!40000 ALTER TABLE `product__order` ENABLE KEYS */;

-- 导出  表 kinkajou.pyshop_constant 结构
CREATE TABLE IF NOT EXISTS `pyshop_constant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `key` varchar(64) DEFAULT NULL,
  `value` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.pyshop_constant 的数据：~0 rows (大约)
DELETE FROM `pyshop_constant`;
/*!40000 ALTER TABLE `pyshop_constant` DISABLE KEYS */;
/*!40000 ALTER TABLE `pyshop_constant` ENABLE KEYS */;

-- 导出  表 kinkajou.pzh_constant 结构
CREATE TABLE IF NOT EXISTS `pzh_constant` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `erpVersion` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.pzh_constant 的数据：~0 rows (大约)
DELETE FROM `pzh_constant`;
/*!40000 ALTER TABLE `pzh_constant` DISABLE KEYS */;
/*!40000 ALTER TABLE `pzh_constant` ENABLE KEYS */;

-- 导出  表 kinkajou.rate 结构
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
  `basename` varchar(256) DEFAULT NULL,
  `funame` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.rate 的数据：~0 rows (大约)
DELETE FROM `rate`;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;

-- 导出  表 kinkajou.skufirst 结构
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.skufirst 的数据：~0 rows (大约)
DELETE FROM `skufirst`;
/*!40000 ALTER TABLE `skufirst` DISABLE KEYS */;
/*!40000 ALTER TABLE `skufirst` ENABLE KEYS */;

-- 导出  表 kinkajou.skusecond 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.skusecond 的数据：~0 rows (大约)
DELETE FROM `skusecond`;
/*!40000 ALTER TABLE `skusecond` DISABLE KEYS */;
/*!40000 ALTER TABLE `skusecond` ENABLE KEYS */;

-- 导出  表 kinkajou.skuthird 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.skuthird 的数据：~0 rows (大约)
DELETE FROM `skuthird`;
/*!40000 ALTER TABLE `skuthird` DISABLE KEYS */;
/*!40000 ALTER TABLE `skuthird` ENABLE KEYS */;

-- 导出  表 kinkajou.to_do__list 结构
CREATE TABLE IF NOT EXISTS `to_do__list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `tasktype` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `content` text,
  `author` int(11) DEFAULT NULL,
  `file_url` varchar(256) DEFAULT NULL,
  `is_finish` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.to_do__list 的数据：~0 rows (大约)
DELETE FROM `to_do__list`;
/*!40000 ALTER TABLE `to_do__list` DISABLE KEYS */;
/*!40000 ALTER TABLE `to_do__list` ENABLE KEYS */;

-- 导出  表 kinkajou.to_do__type 结构
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.to_do__type 的数据：~0 rows (大约)
DELETE FROM `to_do__type`;
/*!40000 ALTER TABLE `to_do__type` DISABLE KEYS */;
/*!40000 ALTER TABLE `to_do__type` ENABLE KEYS */;

-- 导出  表 kinkajou.user 结构
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
  `portrait` varchar(256) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `openid` varchar(64) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  `signature` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.user 的数据：~2 rows (大约)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `create_time`, `update_time`, `remark`, `status`, `username`, `password`, `mobile`, `phone`, `name`, `portrait`, `nickname`, `openid`, `age`, `address`, `signature`) VALUES
	(1, '2021-05-07 13:26:23', '2021-05-07 13:26:23', NULL, 0, '', '', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下'),
	(2, '2021-05-07 13:26:46', '2021-05-07 13:26:46', NULL, 0, 'admin', 'admin1234', NULL, NULL, NULL, NULL, NULL, NULL, 18, NULL, '这个人很懒，什么都没留下');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

-- 导出  表 kinkajou.user2product 结构
CREATE TABLE IF NOT EXISTS `user2product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `operate` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  kinkajou.user2product 的数据：~0 rows (大约)
DELETE FROM `user2product`;
/*!40000 ALTER TABLE `user2product` DISABLE KEYS */;
/*!40000 ALTER TABLE `user2product` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
