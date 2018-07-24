/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50710
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50710
File Encoding         : 65001

Date: 2018-02-26 17:25:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for golddata
-- ----------------------------
DROP TABLE IF EXISTS `golddata`;
CREATE TABLE `golddata` (
  `date` varchar(255) DEFAULT NULL,
  `contract_name` varchar(255) DEFAULT NULL,
  `latest_price` double DEFAULT NULL,
  `high_price` double DEFAULT NULL,
  `low_price` double DEFAULT NULL,
  `open_price` double DEFAULT NULL,
  `now_date` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
