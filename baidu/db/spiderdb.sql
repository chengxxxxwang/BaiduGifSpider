/*
 Navicat Premium Data Transfer

 Source Server         : MyLocalHost
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost
 Source Database       : duitangDB

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : utf-8

 Date: 10/11/2016 11:28:13 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `spiderdb`
-- ----------------------------
DROP TABLE IF EXISTS `spiderdb`;
CREATE TABLE `spiderdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `target_id` varchar(255) DEFAULT NULL COMMENT 'md5',
  `group_id` varchar(255) DEFAULT NULL,
  `dimensions` varchar(255) DEFAULT NULL,
  `size` float DEFAULT NULL,
  `frame` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `data_category` varchar(255) DEFAULT NULL,
  `data_source` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `gif_detail_url` varchar(255) DEFAULT NULL,
  `gif_static_url` varchar(255) DEFAULT NULL,
  `gif_thumb_url` varchar(255) DEFAULT NULL,
  `gif_original_url` varchar(255) DEFAULT NULL,
  `source_web_url` varchar(255) DEFAULT NULL COMMENT '原始网页地址',
  `source_thumb_url` varchar(255) DEFAULT NULL COMMENT '原始缩略图地址',
  `source_thumb_url_on` tinyint(1) DEFAULT NULL,
  `source_original_url` varchar(255) DEFAULT '' COMMENT '原图地址',
  `source_original_url_on` tinyint(1) DEFAULT NULL,
  `is_image_download` tinyint(10) DEFAULT '0',
  `publish_time` datetime DEFAULT NULL,
  `image_download_time` datetime DEFAULT NULL,
  `image_download_failed` tinyint(10) DEFAULT '0',
  `image_download_failedtime` datetime DEFAULT NULL,
  `is_sync` tinyint(10) DEFAULT NULL,
  `sync_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `scrawl_time` datetime DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `status` tinyint(10) DEFAULT '0' COMMENT '状态：0-新建  1-审核通过 -1-删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10335 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
