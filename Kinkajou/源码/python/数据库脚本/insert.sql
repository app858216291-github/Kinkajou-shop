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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  shop.images 的数据：~2 rows (大约)
DELETE FROM `images`;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` (`id`, `create_time`, `update_time`, `remark`, `status`, `name`, `url`, `yongtu`, `pic`) VALUES
	(1, '2019-09-25 23:24:27', '2021-05-07 11:49:38', NULL, 0, 'banner', 'www.baidu.com', '轮播图', 'http://admin.heshihuan.cn/fileServer/common/banner1.jpg'),
	(2, '2019-09-25 23:26:25', '2021-03-31 17:50:00', NULL, 0, '图片2', 'www.google.com', '测试', ',https://pyshop.oss-cn-beijing.aliyuncs.com/produc'),
	(4, '2019-10-09 10:50:07', '2021-03-31 17:50:12', NULL, 0, 'ada', 'www.yahoo.com', 'sdfas', ',https://pyshop.oss-cn-beijing.aliyuncs.com/produc'),
	(5, '2021-05-07 08:02:29', '2021-05-07 11:49:45', NULL, 0, 'banner', 'www.baidu.com', NULL, 'http://admin.heshihuan.cn/fileServer/common/banner3.jpg'),
	(6, '2021-05-07 08:03:02', '2021-05-07 11:49:50', NULL, 0, 'banner', NULL, NULL, 'http://admin.heshihuan.cn/fileServer/common/banner4.jpg'),
	(7, '2021-05-07 09:45:40', '2021-05-07 12:55:20', NULL, 0, 'ad', 'www.baidu.com', '广告图', 'http://admin.heshihuan.cn/fileServer/common/ad1.jpg');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
