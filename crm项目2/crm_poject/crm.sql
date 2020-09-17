-- MySQL dump 10.13  Distrib 5.6.45, for Win64 (x86_64)
--
-- Host: localhost    Database: crm
-- ------------------------------------------------------
-- Server version	5.6.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `crm`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `crm` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `crm`;

--
-- Table structure for table `app01_campuses`
--

DROP TABLE IF EXISTS `app01_campuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_campuses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `address` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_campuses`
--

LOCK TABLES `app01_campuses` WRITE;
/*!40000 ALTER TABLE `app01_campuses` DISABLE KEYS */;
INSERT INTO `app01_campuses` VALUES (1,'上海校区','上海东方明珠'),(2,'北京校区','北京昌平区沙河镇');
/*!40000 ALTER TABLE `app01_campuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_classlist`
--

DROP TABLE IF EXISTS `app01_classlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_classlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(64) NOT NULL,
  `semester` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `memo` varchar(100) DEFAULT NULL,
  `start_date` date NOT NULL,
  `graduate_date` date DEFAULT NULL,
  `class_type` varchar(64) DEFAULT NULL,
  `campuses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_classlist_course_semester_campuses_id_ba9d2f2c_uniq` (`course`,`semester`,`campuses_id`),
  KEY `app01_classlist_campuses_id_45af4e65_fk_app01_campuses_id` (`campuses_id`),
  CONSTRAINT `app01_classlist_campuses_id_45af4e65_fk_app01_campuses_id` FOREIGN KEY (`campuses_id`) REFERENCES `app01_campuses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_classlist`
--

LOCK TABLES `app01_classlist` WRITE;
/*!40000 ALTER TABLE `app01_classlist` DISABLE KEYS */;
INSERT INTO `app01_classlist` VALUES (1,'Linux',2,10000,NULL,'2019-11-20','2019-11-30','online',1),(2,'PythonFullStack',1,10000,NULL,'2019-11-20','2019-11-23','fulltime',2),(3,'Linux',1,10000,NULL,'2019-11-20','2019-11-23','fulltime',1);
/*!40000 ALTER TABLE `app01_classlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_classlist_teachers`
--

DROP TABLE IF EXISTS `app01_classlist_teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_classlist_teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classlist_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_classlist_teachers_classlist_id_userprofile_3205eb68_uniq` (`classlist_id`,`userprofile_id`),
  KEY `app01_classlist_teac_userprofile_id_81fc8cae_fk_app01_use` (`userprofile_id`),
  CONSTRAINT `app01_classlist_teac_classlist_id_d9486686_fk_app01_cla` FOREIGN KEY (`classlist_id`) REFERENCES `app01_classlist` (`id`),
  CONSTRAINT `app01_classlist_teac_userprofile_id_81fc8cae_fk_app01_use` FOREIGN KEY (`userprofile_id`) REFERENCES `app01_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_classlist_teachers`
--

LOCK TABLES `app01_classlist_teachers` WRITE;
/*!40000 ALTER TABLE `app01_classlist_teachers` DISABLE KEYS */;
INSERT INTO `app01_classlist_teachers` VALUES (1,1,1),(2,2,2),(3,3,4);
/*!40000 ALTER TABLE `app01_classlist_teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_consultrecord`
--

DROP TABLE IF EXISTS `app01_consultrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_consultrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` longtext NOT NULL,
  `status` varchar(8) NOT NULL,
  `date` datetime(6) NOT NULL,
  `delete_status` tinyint(1) NOT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_consultrecord_consultant_id_01ffd4e4_fk_app01_use` (`consultant_id`),
  KEY `app01_consultrecord_customer_id_5728417f_fk_app01_customer_id` (`customer_id`),
  CONSTRAINT `app01_consultrecord_consultant_id_01ffd4e4_fk_app01_use` FOREIGN KEY (`consultant_id`) REFERENCES `app01_userprofile` (`id`),
  CONSTRAINT `app01_consultrecord_customer_id_5728417f_fk_app01_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `app01_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_consultrecord`
--

LOCK TABLES `app01_consultrecord` WRITE;
/*!40000 ALTER TABLE `app01_consultrecord` DISABLE KEYS */;
INSERT INTO `app01_consultrecord` VALUES (1,'这是跟进内容dsamklmas','F','2019-11-25 12:20:17.815327',0,4,2),(2,'dasdass','D','2019-11-25 12:20:30.380755',0,4,1),(3,'vdasacvda','A','2019-11-25 13:02:42.229009',0,4,1),(4,'zheshi xinzengshuju','D','2019-11-25 13:31:07.773866',0,4,2),(5,'你好','F','2019-11-25 13:40:04.250073',0,4,2),(6,'这是第二条数据','H','2019-11-25 13:43:04.893724',0,4,2);
/*!40000 ALTER TABLE `app01_consultrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_courserecord`
--

DROP TABLE IF EXISTS `app01_courserecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_courserecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day_num` int(11) NOT NULL,
  `date` date NOT NULL,
  `course_title` varchar(64) DEFAULT NULL,
  `course_memo` longtext,
  `has_homework` tinyint(1) NOT NULL,
  `homework_title` varchar(64) DEFAULT NULL,
  `homework_memo` longtext,
  `scoring_point` longtext,
  `re_class_id` int(11) NOT NULL,
  `recorder_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_courserecord_re_class_id_day_num_9467c419_uniq` (`re_class_id`,`day_num`),
  KEY `app01_courserecord_recorder_id_6d09acbf_fk_app01_userprofile_id` (`recorder_id`),
  KEY `app01_courserecord_teacher_id_4476c694_fk_app01_userprofile_id` (`teacher_id`),
  CONSTRAINT `app01_courserecord_re_class_id_224ae9c9_fk_app01_classlist_id` FOREIGN KEY (`re_class_id`) REFERENCES `app01_classlist` (`id`),
  CONSTRAINT `app01_courserecord_recorder_id_6d09acbf_fk_app01_userprofile_id` FOREIGN KEY (`recorder_id`) REFERENCES `app01_userprofile` (`id`),
  CONSTRAINT `app01_courserecord_teacher_id_4476c694_fk_app01_userprofile_id` FOREIGN KEY (`teacher_id`) REFERENCES `app01_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_courserecord`
--

LOCK TABLES `app01_courserecord` WRITE;
/*!40000 ALTER TABLE `app01_courserecord` DISABLE KEYS */;
INSERT INTO `app01_courserecord` VALUES (1,1,'2019-11-26',NULL,'',1,NULL,'','',2,2,4),(2,1,'2019-11-26','这是以个标题','',1,NULL,'','',1,4,2);
/*!40000 ALTER TABLE `app01_courserecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_customer`
--

DROP TABLE IF EXISTS `app01_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qq` varchar(64) NOT NULL,
  `qq_name` varchar(64) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `sex` varchar(16) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `source` varchar(64) NOT NULL,
  `course` varchar(21) NOT NULL,
  `class_type` varchar(64) NOT NULL,
  `customer_note` longtext,
  `status` varchar(64) NOT NULL,
  `last_consult_date` date NOT NULL,
  `next_date` date DEFAULT NULL,
  `consultant_id` int(11) DEFAULT NULL,
  `introduce_from_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `qq` (`qq`),
  KEY `app01_customer_consultant_id_8032bb08_fk_app01_userprofile_id` (`consultant_id`),
  KEY `app01_customer_introduce_from_id_ee31cbdd_fk_app01_customer_id` (`introduce_from_id`),
  CONSTRAINT `app01_customer_consultant_id_8032bb08_fk_app01_userprofile_id` FOREIGN KEY (`consultant_id`) REFERENCES `app01_userprofile` (`id`),
  CONSTRAINT `app01_customer_introduce_from_id_ee31cbdd_fk_app01_customer_id` FOREIGN KEY (`introduce_from_id`) REFERENCES `app01_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_customer`
--

LOCK TABLES `app01_customer` WRITE;
/*!40000 ALTER TABLE `app01_customer` DISABLE KEYS */;
INSERT INTO `app01_customer` VALUES (1,'326393044',NULL,'长城出版社','male','1990-11-21',13000000000,'office_direct','Linux,PythonFullStack','online','','studying','2019-11-20','2019-11-21',2,NULL),(2,'599010465','你好','赫翊辰','male','1990-11-21',18870414853,'qq','Linux,PythonFullStack','weekend','','paid_in_full','2019-11-21','2019-11-21',8,1),(3,'23@qq.com',NULL,NULL,'male',NULL,NULL,'qq','Linux,PythonFullStack','fulltime','','unregistered','2019-11-21',NULL,2,NULL),(4,'67@qq.com',NULL,NULL,'male',NULL,NULL,'qq','Linux,PythonFullStack','weekend','','studying','2019-11-21',NULL,2,NULL),(5,'89@qq.com','你好','长城出版社','male','1990-11-21',17770414853,'qq','Linux','fulltime','','unregistered','2019-11-21',NULL,8,NULL),(6,'fabjka','你好','长城出版社','male','1990-11-21',NULL,'qq','PythonFullStack','fulltime','','studying','2019-11-21',NULL,4,NULL),(7,'asddasnl',NULL,NULL,'male',NULL,NULL,'qq','PythonFullStack','fulltime','','unregistered','2019-11-22',NULL,4,NULL),(8,'dsaa',NULL,NULL,'male',NULL,NULL,'qq','Linux','fulltime','','unregistered','2019-11-22',NULL,4,NULL),(9,'daadsdas',NULL,NULL,'female',NULL,NULL,'qq','Linux','fulltime','','unregistered','2019-11-22',NULL,4,NULL),(10,'dsadasdaf',NULL,NULL,'male',NULL,NULL,'qq','PythonFullStack','fulltime','','unregistered','2019-11-22',NULL,4,NULL),(11,'ffaa',NULL,'苏教出版社','male',NULL,NULL,'qq','Linux','fulltime','','unregistered','2019-11-23',NULL,4,NULL),(12,'fsajkasn',NULL,'苏教出版社','male',NULL,NULL,'qq','Linux','fulltime','','unregistered','2019-11-23',NULL,4,NULL),(13,'asdhakasd',NULL,'苏教出版社','male',NULL,NULL,'qq','Linux','fulltime','','unregistered','2019-11-23',NULL,4,NULL),(14,'nsncA<Nc',NULL,NULL,'male',NULL,NULL,'qq','PythonFullStack','fulltime','','unregistered','2019-11-23',NULL,4,NULL);
/*!40000 ALTER TABLE `app01_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_customer_class_list`
--

DROP TABLE IF EXISTS `app01_customer_class_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_customer_class_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `classlist_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_customer_class_list_customer_id_classlist_id_2868a8ae_uniq` (`customer_id`,`classlist_id`),
  KEY `app01_customer_class_classlist_id_c3575f10_fk_app01_cla` (`classlist_id`),
  CONSTRAINT `app01_customer_class_classlist_id_c3575f10_fk_app01_cla` FOREIGN KEY (`classlist_id`) REFERENCES `app01_classlist` (`id`),
  CONSTRAINT `app01_customer_class_customer_id_d7a92dfe_fk_app01_cus` FOREIGN KEY (`customer_id`) REFERENCES `app01_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_customer_class_list`
--

LOCK TABLES `app01_customer_class_list` WRITE;
/*!40000 ALTER TABLE `app01_customer_class_list` DISABLE KEYS */;
INSERT INTO `app01_customer_class_list` VALUES (1,1,1),(2,1,2),(3,2,1),(4,4,1),(5,5,1),(6,5,2);
/*!40000 ALTER TABLE `app01_customer_class_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_department`
--

DROP TABLE IF EXISTS `app01_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_department`
--

LOCK TABLES `app01_department` WRITE;
/*!40000 ALTER TABLE `app01_department` DISABLE KEYS */;
INSERT INTO `app01_department` VALUES (1,'销售',10),(2,'公关',5),(3,'讲师',3);
/*!40000 ALTER TABLE `app01_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_enrollment`
--

DROP TABLE IF EXISTS `app01_enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_enrollment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `why_us` longtext,
  `your_expectation` longtext,
  `contract_agreed` tinyint(1) NOT NULL,
  `contract_approved` tinyint(1) NOT NULL,
  `enrolled_date` datetime(6) NOT NULL,
  `memo` longtext,
  `delete_status` tinyint(1) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `enrolment_class_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_enrollment_enrolment_class_id_customer_id_ad9b37f7_uniq` (`enrolment_class_id`,`customer_id`),
  KEY `app01_enrollment_customer_id_99adc3d9_fk_app01_customer_id` (`customer_id`),
  KEY `app01_enrollment_school_id_bf0b6a99_fk_app01_campuses_id` (`school_id`),
  CONSTRAINT `app01_enrollment_customer_id_99adc3d9_fk_app01_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `app01_customer` (`id`),
  CONSTRAINT `app01_enrollment_enrolment_class_id_2b7b93c6_fk_app01_cla` FOREIGN KEY (`enrolment_class_id`) REFERENCES `app01_classlist` (`id`),
  CONSTRAINT `app01_enrollment_school_id_bf0b6a99_fk_app01_campuses_id` FOREIGN KEY (`school_id`) REFERENCES `app01_campuses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_enrollment`
--

LOCK TABLES `app01_enrollment` WRITE;
/*!40000 ALTER TABLE `app01_enrollment` DISABLE KEYS */;
INSERT INTO `app01_enrollment` VALUES (1,'因为爱学习','目标找到工作',1,1,'2019-11-25 14:30:19.732523','这是一个文档',0,2,2,2),(2,'亲爱哒','10K',1,1,'2019-11-26 07:50:24.838285','亲爱哒',0,5,1,1),(3,'被长城坑了','走向人生叠风',1,1,'2019-11-26 08:40:08.091643','',0,2,1,2);
/*!40000 ALTER TABLE `app01_enrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_paymentrecord`
--

DROP TABLE IF EXISTS `app01_paymentrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_paymentrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pay_type` varchar(64) NOT NULL,
  `paid_fee` int(11) NOT NULL,
  `note` longtext,
  `date` datetime(6) NOT NULL,
  `course` varchar(64) DEFAULT NULL,
  `class_type` varchar(64) DEFAULT NULL,
  `delete_status` tinyint(1) NOT NULL,
  `status` int(11) NOT NULL,
  `confirm_date` datetime(6) DEFAULT NULL,
  `confirm_user_id` int(11) DEFAULT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `enrolment_class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_paymentrecord_confirm_user_id_76394a49_fk_app01_use` (`confirm_user_id`),
  KEY `app01_paymentrecord_consultant_id_b57e45a6_fk_app01_use` (`consultant_id`),
  KEY `app01_paymentrecord_customer_id_e51ad199_fk_app01_customer_id` (`customer_id`),
  KEY `app01_paymentrecord_enrolment_class_id_ab1c7df4_fk_app01_cla` (`enrolment_class_id`),
  CONSTRAINT `app01_paymentrecord_confirm_user_id_76394a49_fk_app01_use` FOREIGN KEY (`confirm_user_id`) REFERENCES `app01_userprofile` (`id`),
  CONSTRAINT `app01_paymentrecord_consultant_id_b57e45a6_fk_app01_use` FOREIGN KEY (`consultant_id`) REFERENCES `app01_userprofile` (`id`),
  CONSTRAINT `app01_paymentrecord_customer_id_e51ad199_fk_app01_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `app01_customer` (`id`),
  CONSTRAINT `app01_paymentrecord_enrolment_class_id_ab1c7df4_fk_app01_cla` FOREIGN KEY (`enrolment_class_id`) REFERENCES `app01_classlist` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_paymentrecord`
--

LOCK TABLES `app01_paymentrecord` WRITE;
/*!40000 ALTER TABLE `app01_paymentrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `app01_paymentrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_studyrecord`
--

DROP TABLE IF EXISTS `app01_studyrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_studyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendance` varchar(64) NOT NULL,
  `score` int(11) NOT NULL,
  `homework_note` varchar(255) DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `note` varchar(255) DEFAULT NULL,
  `homework` varchar(100) DEFAULT NULL,
  `course_record_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_studyrecord_course_record_id_student_id_db81a8d8_uniq` (`course_record_id`,`student_id`),
  KEY `app01_studyrecord_student_id_11107852_fk_app01_customer_id` (`student_id`),
  CONSTRAINT `app01_studyrecord_course_record_id_09c56fb0_fk_app01_cou` FOREIGN KEY (`course_record_id`) REFERENCES `app01_courserecord` (`id`),
  CONSTRAINT `app01_studyrecord_student_id_11107852_fk_app01_customer_id` FOREIGN KEY (`student_id`) REFERENCES `app01_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_studyrecord`
--

LOCK TABLES `app01_studyrecord` WRITE;
/*!40000 ALTER TABLE `app01_studyrecord` DISABLE KEYS */;
INSERT INTO `app01_studyrecord` VALUES (1,'checked',-1,NULL,'2019-11-26 14:37:48.021774',NULL,'',1,1),(2,'checked',-1,NULL,'2019-11-26 14:37:48.039726',NULL,'',2,1),(3,'checked',-1,NULL,'2019-11-26 14:37:48.039726',NULL,'',2,4);
/*!40000 ALTER TABLE `app01_studyrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_userprofile`
--

DROP TABLE IF EXISTS `app01_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(128) NOT NULL,
  `name` varchar(32) NOT NULL,
  `mobile` varchar(32) DEFAULT NULL,
  `memo` longtext,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `app01_userprofile_department_id_bab0384f_fk_app01_department_id` (`department_id`),
  CONSTRAINT `app01_userprofile_department_id_bab0384f_fk_app01_department_id` FOREIGN KEY (`department_id`) REFERENCES `app01_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_userprofile`
--

LOCK TABLES `app01_userprofile` WRITE;
/*!40000 ALTER TABLE `app01_userprofile` DISABLE KEYS */;
INSERT INTO `app01_userprofile` VALUES (1,'hyc','hyc123','hyc',NULL,NULL,'2019-11-19 13:30:21.560000',1,NULL),(2,'326393044@qq.com','202cb962ac59075b964b07152d234b70','赫翊辰','18870414853',NULL,'2019-11-20 04:38:24.173554',1,2),(4,'32@qq.com','4297f44b13955235245b2497399d7a93','长城出版社','18870414853',NULL,'2019-11-21 02:20:42.944423',1,1),(5,'hyc123@qq.com','25f9e794323b453885f5181f1b624d0b','赫翊辰','18870414853',NULL,'2019-12-16 14:19:13.047375',1,3),(6,'admin@qq.com','25d55ad283aa400af464c76d713c07ad','贾超麟','18870414853',NULL,'2019-12-16 14:26:12.415502',1,2),(7,'zxc123@qq.com','4297f44b13955235245b2497399d7a93','赫翊辰','18870414853',NULL,'2020-02-18 11:34:55.482834',1,1),(8,'root@qq.com','4297f44b13955235245b2497399d7a93','贾超麟','18870414853',NULL,'2020-02-18 11:40:06.635024',1,3);
/*!40000 ALTER TABLE `app01_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add campuses',7,'add_campuses'),(20,'Can change campuses',7,'change_campuses'),(21,'Can delete campuses',7,'delete_campuses'),(22,'Can add class list',8,'add_classlist'),(23,'Can change class list',8,'change_classlist'),(24,'Can delete class list',8,'delete_classlist'),(25,'Can add consult record',9,'add_consultrecord'),(26,'Can change consult record',9,'change_consultrecord'),(27,'Can delete consult record',9,'delete_consultrecord'),(28,'Can add course record',10,'add_courserecord'),(29,'Can change course record',10,'change_courserecord'),(30,'Can delete course record',10,'delete_courserecord'),(31,'Can add customer',11,'add_customer'),(32,'Can change customer',11,'change_customer'),(33,'Can delete customer',11,'delete_customer'),(34,'Can add department',12,'add_department'),(35,'Can change department',12,'change_department'),(36,'Can delete department',12,'delete_department'),(37,'Can add enrollment',13,'add_enrollment'),(38,'Can change enrollment',13,'change_enrollment'),(39,'Can delete enrollment',13,'delete_enrollment'),(40,'Can add payment record',14,'add_paymentrecord'),(41,'Can change payment record',14,'change_paymentrecord'),(42,'Can delete payment record',14,'delete_paymentrecord'),(43,'Can add study record',15,'add_studyrecord'),(44,'Can change study record',15,'change_studyrecord'),(45,'Can delete study record',15,'delete_studyrecord'),(46,'Can add user profile',16,'add_userprofile'),(47,'Can change user profile',16,'change_userprofile'),(48,'Can delete user profile',16,'delete_userprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$ZFVGMRPvt49V$UYroq3xehZrAIJOIX2tl/qxbKXtKp4MQUuobO/OpLlg=','2019-12-16 14:25:19.673139',1,'root','','','',1,1,'2019-11-20 07:37:43.741805');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-11-20 07:48:00.395649','1','Customer object',1,'[{\"added\": {}}]',11,1),(2,'2019-11-20 08:05:01.266398','1','Campuses object',1,'[{\"added\": {}}]',7,1),(3,'2019-11-20 08:05:39.205209','2','Campuses object',1,'[{\"added\": {}}]',7,1),(4,'2019-11-20 08:06:07.618844','1','Linux',1,'[{\"added\": {}}]',8,1),(5,'2019-11-20 08:06:25.841663','2','PythonFullStack',1,'[{\"added\": {}}]',8,1),(6,'2019-11-20 08:06:41.894612','1','Customer object',2,'[{\"changed\": {\"fields\": [\"class_list\"]}}]',11,1),(7,'2019-11-21 02:28:35.813159','2','Customer object',1,'[{\"added\": {}}]',11,1),(8,'2019-11-25 12:20:17.817323','1','ConsultRecord object',1,'[{\"added\": {}}]',9,1),(9,'2019-11-25 12:20:30.382723','2','ConsultRecord object',1,'[{\"added\": {}}]',9,1),(10,'2019-11-25 12:31:52.677484','2','ConsultRecord object',2,'[{\"changed\": {\"fields\": [\"consultant\"]}}]',9,1),(11,'2019-11-25 12:31:58.794140','1','ConsultRecord object',2,'[{\"changed\": {\"fields\": [\"consultant\"]}}]',9,1),(12,'2019-11-25 14:30:19.736516','1','Enrollment object',1,'[{\"added\": {}}]',13,1),(13,'2019-11-25 14:36:06.528537','1','Enrollment object',2,'[{\"changed\": {\"fields\": [\"memo\"]}}]',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app01','campuses'),(8,'app01','classlist'),(9,'app01','consultrecord'),(10,'app01','courserecord'),(11,'app01','customer'),(12,'app01','department'),(13,'app01','enrollment'),(14,'app01','paymentrecord'),(15,'app01','studyrecord'),(16,'app01','userprofile'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-11-19 12:53:44.767201'),(2,'auth','0001_initial','2019-11-19 12:53:45.328531'),(3,'admin','0001_initial','2019-11-19 12:53:45.468157'),(4,'admin','0002_logentry_remove_auto_add','2019-11-19 12:53:45.488103'),(5,'app01','0001_initial','2019-11-19 12:53:47.425358'),(6,'contenttypes','0002_remove_content_type_name','2019-11-19 12:53:47.536061'),(7,'auth','0002_alter_permission_name_max_length','2019-11-19 12:53:47.591913'),(8,'auth','0003_alter_user_email_max_length','2019-11-19 12:53:47.659732'),(9,'auth','0004_alter_user_username_opts','2019-11-19 12:53:47.683667'),(10,'auth','0005_alter_user_last_login_null','2019-11-19 12:53:47.736525'),(11,'auth','0006_require_contenttypes_0002','2019-11-19 12:53:47.751487'),(12,'auth','0007_alter_validators_add_error_messages','2019-11-19 12:53:47.778413'),(13,'auth','0008_alter_user_username_max_length','2019-11-19 12:53:47.841248'),(14,'sessions','0001_initial','2019-11-19 12:53:47.896099');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8rjexjjrn1kyzyrgt9o5ikq6my5ulzrq','ZjViYThmYTQxN2ZhYzU4ZTg4ZmMxODFkOGRkYTY4ZTc3ODFhOTc4Njp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwicGsiOjQsImlzX2xvZ2luIjp0cnVlfQ==','2019-12-07 09:58:11.400117'),('9y8onmxull1cjaa383gulihq68mbmh41','N2EwNWQwMGUxYTdmMjRhYjg2NzI0NmZlOTA4ZDU4Y2UzNTk5ZGUxZjp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwicGsiOjQsImlzX2xvZ2luIjp0cnVlLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjU5ZTgxZjA5MTIwMmVmNjU0NjUxNmI1ZTQyYTBkN2MxMWY0ZGEwYiJ9','2019-12-09 12:19:50.711802'),('da09btncr0izjtuf982cqko68prfyhv0','YTI5MzNmNWZkNDkyMDNjZjk2MzZiNmE4OWNjZDk0NzU5YWNjZDA3Nzp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwiaXNfbG9naW4iOnRydWV9','2019-12-05 13:55:42.827992'),('fquw7jasry6s339cotq6bj3br7bm9d9p','ZjViYThmYTQxN2ZhYzU4ZTg4ZmMxODFkOGRkYTY4ZTc3ODFhOTc4Njp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwicGsiOjQsImlzX2xvZ2luIjp0cnVlfQ==','2019-12-07 07:30:36.618900'),('ihg6yi6bewu1w1tqgnuqep8h69froul7','NjVjNDAxOTNmZGNkYzBhNzQ1OWIwYWUzMjM0MDgyMTJkN2Y0ZjZmYzp7InVzZXJuYW1lIjoicm9vdEBxcS5jb20iLCJwayI6OCwiaXNfbG9naW4iOnRydWV9','2020-03-03 11:40:17.261534'),('sllpcxz9y6pd4kygt6gm49ds8j8ypqx6','YTcwOGQyODc1NzNjMDE5NDdjOWM0M2M5MjdlNTYwNTRiZmI3NjFmYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTllODFmMDkxMjAyZWY2NTQ2NTE2YjVlNDJhMGQ3YzExZjRkYTBiIiwidXNlcm5hbWUiOiJhZG1pbkBxcS5jb20iLCJwayI6NiwiaXNfbG9naW4iOnRydWV9','2019-12-30 14:26:17.624614'),('stdqv0qteeeas4bqgusfwr2aew7lbl9i','ZjViYThmYTQxN2ZhYzU4ZTg4ZmMxODFkOGRkYTY4ZTc3ODFhOTc4Njp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwicGsiOjQsImlzX2xvZ2luIjp0cnVlfQ==','2019-12-10 09:28:38.996506'),('z2226hfh77azy0nmm109x81gwobzow49','ZjViYThmYTQxN2ZhYzU4ZTg4ZmMxODFkOGRkYTY4ZTc3ODFhOTc4Njp7InVzZXJuYW1lIjoiMzJAcXEuY29tIiwicGsiOjQsImlzX2xvZ2luIjp0cnVlfQ==','2019-12-09 07:12:03.362707');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-20 22:58:15
