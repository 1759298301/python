/*
 Navicat MySQL Data Transfer

 Source Server         : wl连接
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : vega

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 24/02/2021 16:32:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_news
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标题',
  `editor_id` int UNSIGNED NOT NULL,
  `type_id` int UNSIGNED NOT NULL,
  `content_id` char(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_top` tinyint UNSIGNED NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` enum('草稿','待审批','已审批','隐藏') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `editor_id`(`editor_id`) USING BTREE,
  INDEX `type_id`(`type_id`) USING BTREE,
  INDEX `state`(`state`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES (1, '马云卸任', 2, 1, '哈哈哈', 1, '2021-01-01 13:39:39', '2021-02-23 13:39:53', '待审批');
INSERT INTO `t_news` VALUES (2, '科比死了', 2, 2, '唉，难受', 2, '2021-02-23 13:41:44', '2021-02-23 13:41:44', '待审批');
INSERT INTO `t_news` VALUES (3, '我要吃饭', 2, 3, '唉，没饭吃', 2, '2021-02-23 13:41:44', '2021-02-23 13:41:44', '待审批');
INSERT INTO `t_news` VALUES (4, '习近平当主席', 2, 1, '唉，高兴', 1, '2021-01-01 13:41:44', '2021-02-23 13:41:44', '待审批');
INSERT INTO `t_news` VALUES (5, '腾讯炸了', 2, 3, '妈的', 1, '2021-01-20 13:39:39', '2021-02-23 13:39:53', '待审批');
INSERT INTO `t_news` VALUES (6, '王宝强被绿', 2, 4, '宝强很苦', 6, '2021-01-24 13:39:39', '2021-02-23 13:39:53', '待审批');
INSERT INTO `t_news` VALUES (7, '台湾被收复了', 2, 5, '爽啊', 3, '2021-01-24 13:39:39', '2021-02-23 13:39:53', '待审批');

-- ----------------------------
-- Table structure for t_role
-- ----------------------------
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `role` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `role`(`role`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_role
-- ----------------------------
INSERT INTO `t_role` VALUES (1, '管理员');
INSERT INTO `t_role` VALUES (2, '编辑者');

-- ----------------------------
-- Table structure for t_type
-- ----------------------------
DROP TABLE IF EXISTS `t_type`;
CREATE TABLE `t_type`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `type`(`type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_type
-- ----------------------------
INSERT INTO `t_type` VALUES (2, '体育');
INSERT INTO `t_type` VALUES (5, '历史');
INSERT INTO `t_type` VALUES (4, '娱乐');
INSERT INTO `t_type` VALUES (3, '科技');
INSERT INTO `t_type` VALUES (1, '要闻');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role_id` int UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `username_2`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES (1, 'admin', '37E31E685743DF7B9267E42DAFA3B889', 'admin@163.com', 1);
INSERT INTO `t_user` VALUES (2, '王蕾', '8441AB08F2B4AA3CABC9A423E439F487', 'wanglei@163.com', 2);
INSERT INTO `t_user` VALUES (3, 'wang', 'F15F1F801CC71962E0E3332F68702E0C', '193@163.com', 2);
INSERT INTO `t_user` VALUES (4, 'wang1', 'F15F1F801CC71962E0E3332F68702E0C', '193@163.com', 2);
INSERT INTO `t_user` VALUES (5, 'wang2', 'F15F1F801CC71962E0E3332F68702E0C', '193@163.com', 2);
INSERT INTO `t_user` VALUES (15, 'wang333', '81F44672F7707F551EA23C36B66F7AFE', '123', 1);

SET FOREIGN_KEY_CHECKS = 1;
