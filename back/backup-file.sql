-- MySQL dump 10.17  Distrib 10.3.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: tiles
-- ------------------------------------------------------
-- Server version	10.3.12-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('bd93a50e80ef');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(240) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `article` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `reflect` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `article` (`article`),
  UNIQUE KEY `name` (`name`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `material_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `material_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (21,'ламинат коричневый',4,'МАТ20',600,600,50),(22,'Плитка каменная',1,'МАТ21',400,300,7);
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_category`
--

DROP TABLE IF EXISTS `material_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(240) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_category`
--

LOCK TABLES `material_category` WRITE;
/*!40000 ALTER TABLE `material_category` DISABLE KEYS */;
INSERT INTO `material_category` VALUES (1,'Керамическая плитка и керамогранит'),(4,'Ламинат'),(5,'Виниловый пол'),(6,'Линолеум'),(7,'Обои');
/*!40000 ALTER TABLE `material_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plane`
--

DROP TABLE IF EXISTS `plane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plane` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `points` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `scene_id` int(11) DEFAULT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scene_id` (`scene_id`),
  CONSTRAINT `plane_ibfk_1` FOREIGN KEY (`scene_id`) REFERENCES `scene` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
INSERT INTO `plane` VALUES (26,'[[101,15],[691,13],[690,404],[106,404]]',8,3800,2700),(27,'[[687,13],[804,-58],[804,482],[691,404]]',8,2700,2700),(28,'[[113,400],[684,400],[978,609],[-175,604]]',8,3800,3800),(29,'[[160,120],[640,120],[640,480],[160,480]]',NULL,3500,2700),(30,'[[160,120],[640,120],[640,480],[160,480]]',NULL,3500,2700),(31,'[[328,27],[785,-25],[787,405],[335,327]]',11,4000,2700);
/*!40000 ALTER TABLE `plane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scene`
--

DROP TABLE IF EXISTS `scene`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scene` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(240) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `scene_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `scene_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scene`
--

LOCK TABLES `scene` WRITE;
/*!40000 ALTER TABLE `scene` DISABLE KEYS */;
INSERT INTO `scene` VALUES (8,'test',3,'2019-04-15 00:02:48'),(11,'test',1,'2019-05-10 14:51:57');
/*!40000 ALTER TABLE `scene` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scene_category`
--

DROP TABLE IF EXISTS `scene_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scene_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(240) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scene_category`
--

LOCK TABLES `scene_category` WRITE;
/*!40000 ALTER TABLE `scene_category` DISABLE KEYS */;
INSERT INTO `scene_category` VALUES (1,'Гостинные'),(2,'Кухни'),(3,'Спальные'),(4,'Ванные комнаты'),(5,'Пользовательские');
/*!40000 ALTER TABLE `scene_category` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-11 16:18:27
