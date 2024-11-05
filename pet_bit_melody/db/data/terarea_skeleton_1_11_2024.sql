-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: terarea
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB-ubu2404

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ActionLoging`
--

DROP TABLE IF EXISTS `ActionLoging`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ActionLoging` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL DEFAULT current_timestamp() COMMENT 'This is the time at which the workflow occurred',
  `type` mediumtext NOT NULL DEFAULT 'API' COMMENT 'The type of action concerned',
  `action_id` bigint(20) unsigned NOT NULL COMMENT 'The id of the item that is being logged',
  `message` longtext DEFAULT NULL COMMENT 'The error message',
  `code` bigint(20) DEFAULT NULL COMMENT 'The code linked to the action',
  `level` mediumtext DEFAULT NULL COMMENT 'The level of the importance for the code',
  `resolved` tinyint(1) DEFAULT NULL COMMENT 'Inform if the current error is solved',
  PRIMARY KEY (`id`),
  KEY `WorkflowLoging_Actions_FK` (`action_id`),
  CONSTRAINT `WorkflowLoging_Actions_FK` FOREIGN KEY (`action_id`) REFERENCES `Actions` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The new loggin table.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ActionLoging`
--

LOCK TABLES `ActionLoging` WRITE;
/*!40000 ALTER TABLE `ActionLoging` DISABLE KEYS */;
/*!40000 ALTER TABLE `ActionLoging` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ActionTemplate`
--

DROP TABLE IF EXISTS `ActionTemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ActionTemplate` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL DEFAULT 'action' COMMENT 'The type of the template',
  `json` longtext NOT NULL COMMENT 'The json content for the template.',
  `action_id` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ActionTemplate_Actions_FK` (`action_id`),
  CONSTRAINT `ActionTemplate_Services_FK` FOREIGN KEY (`action_id`) REFERENCES `Services` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The table containing the templates for the action that the website has to offer.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ActionTemplate`
--

LOCK TABLES `ActionTemplate` WRITE;
/*!40000 ALTER TABLE `ActionTemplate` DISABLE KEYS */;
/*!40000 ALTER TABLE `ActionTemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actions`
--

DROP TABLE IF EXISTS `Actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(400) NOT NULL DEFAULT 'zero two, darling, darling... DARLING !!!',
  `trigger` mediumtext NOT NULL DEFAULT 'Elle est où la pierre ?',
  `consequences` mediumtext DEFAULT 'DANS LA POCHE !!!',
  `user_id` bigint(20) unsigned NOT NULL COMMENT 'The author of the current action',
  `tags` longtext DEFAULT NULL COMMENT 'The tags used to find the the actions the user created.',
  `running` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'L''information sur si le l''action est en fonctionnement',
  `description` varchar(2000) NOT NULL DEFAULT 'Some description' COMMENT 'The description of the workflow.',
  `colour` varchar(100) NOT NULL DEFAULT '#f1f1f1' COMMENT 'The colour of the workflow.',
  `favicon` mediumtext DEFAULT NULL COMMENT 'The link to the icon of the workflow.',
  `frequency` bigint(20) unsigned NOT NULL DEFAULT 0 COMMENT 'The amount of times the action is used',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Actions_UNIQUE` (`name`),
  KEY `Actions_Users_FK` (`user_id`),
  CONSTRAINT `Actions_Users_FK` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='triggers and actions of ifttt\nexample: if bad_guy then nuts';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actions`
--

LOCK TABLES `Actions` WRITE;
/*!40000 ALTER TABLE `Actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ActiveOauths`
--

DROP TABLE IF EXISTS `ActiveOauths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ActiveOauths` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `token` mediumtext DEFAULT NULL COMMENT 'The token temporarily provided by the sso',
  `token_expiration` datetime DEFAULT current_timestamp() COMMENT 'The date when it expires',
  `token_lifespan` bigint(20) unsigned DEFAULT NULL COMMENT 'The time for which a token is alive before being invalidated',
  `refresh_link` varchar(2048) DEFAULT NULL COMMENT 'The link to be used to refresh the login token',
  `service_id` bigint(20) unsigned NOT NULL COMMENT 'The id of the service that is concerned',
  `user_id` bigint(20) unsigned NOT NULL COMMENT 'The id of the user to which this token belongs to',
  PRIMARY KEY (`id`),
  KEY `ActiveOauths_Services_FK` (`service_id`),
  KEY `ActiveOauths_Users_FK` (`user_id`),
  CONSTRAINT `ActiveOauths_Services_FK` FOREIGN KEY (`service_id`) REFERENCES `Services` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `ActiveOauths_Users_FK` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The current OAuths that are still valid.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ActiveOauths`
--

LOCK TABLES `ActiveOauths` WRITE;
/*!40000 ALTER TABLE `ActiveOauths` DISABLE KEYS */;
/*!40000 ALTER TABLE `ActiveOauths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Connections`
--

DROP TABLE IF EXISTS `Connections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Connections` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(900) DEFAULT NULL COMMENT 'The token of the user.',
  `user_id` bigint(20) unsigned DEFAULT NULL COMMENT 'The e-mail of the user.',
  `expiration_date` datetime DEFAULT NULL COMMENT 'The date at which the token is invalidated.',
  PRIMARY KEY (`id`),
  KEY `Connections_Users_FK` (`user_id`),
  CONSTRAINT `Connections_Users_FK` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The active connections of the server.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Connections`
--

LOCK TABLES `Connections` WRITE;
/*!40000 ALTER TABLE `Connections` DISABLE KEYS */;
/*!40000 ALTER TABLE `Connections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Services`
--

DROP TABLE IF EXISTS `Services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Services` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL COMMENT 'The name of the service.',
  `url` varchar(2048) NOT NULL COMMENT 'The url that will be used to access the service.',
  `api_key` varchar(1024) NULL COMMENT 'The api token.',
  `category` varchar(200) NOT NULL COMMENT 'This is the type of service offered by the api.',
  `frequency` bigint(20) unsigned NOT NULL DEFAULT 0 COMMENT 'The amount of times the service is used.',
  `type` varchar(200) NOT NULL DEFAULT 'service' COMMENT 'The type of the api.',
  `tags` longtext DEFAULT NULL COMMENT 'The keywords to search for the api',
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `oauth` tinyint(1) DEFAULT NULL COMMENT 'Inform the code if the service is authenticated via OAuth.',
  `colour` varchar(1024) NULL COMMENT 'The colour of the service.',
  `description` mediumtext NULL COMMENT 'The description for the service.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Services_UNIQUE_1` (`name`),
  UNIQUE KEY `Services_UNIQUE` (`url`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Info about the api''s and what they have to offer.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Services`
--

LOCK TABLES `Services` WRITE;
/*!40000 ALTER TABLE `Services` DISABLE KEYS */;
/*!40000 ALTER TABLE `Services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserOauthConnection`
--

DROP TABLE IF EXISTS `UserOauthConnection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserOauthConnection` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `provider_name` mediumtext NOT NULL COMMENT 'The name of the service provider.',
  `client_id` mediumtext NOT NULL COMMENT 'The id of the initial account that allows us to start the OAuth process, here noreply-terarea@gmail.com.',
  `client_secret` mediumtext NOT NULL COMMENT 'The secret of the initial account that allows us to start the OAuth process, here noreply-terarea@gmail.com.',
  `provider_scope` mediumtext NOT NULL COMMENT 'The information that is queried from the provider.',
  `authorisation_base_url` varchar(2048) NOT NULL COMMENT 'The url that allows the front-end to spawn a login page with the provider.',
  `token_grabber_base_url` varchar(2048) NOT NULL COMMENT 'The link allowing the backend to get the information returned by the provider during the login.',
  `user_info_base_url` varchar(2048) NOT NULL COMMENT 'Get the user info.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `UserOauthConnection_UNIQUE_1` (`provider_name`) USING HASH,
  UNIQUE KEY `UserOauthConnection_UNIQUE_2` (`client_id`) USING HASH,
  UNIQUE KEY `UserOauthConnection_UNIQUE` (`client_secret`) USING HASH,
  UNIQUE KEY `UserOauthConnection_UNIQUE_3` (`token_grabber_base_url`) USING HASH,
  UNIQUE KEY `UserOauthConnection_UNIQUE_4` (`user_info_base_url`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The table containing the information for the OAuths that will be used to allow users to log into their accounts.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserOauthConnection`
--

LOCK TABLES `UserOauthConnection` WRITE;
/*!40000 ALTER TABLE `UserOauthConnection` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserOauthConnection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserServices`
--

DROP TABLE IF EXISTS `UserServices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserServices` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `area_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UserServices_Users_FK` (`user_id`),
  KEY `UserServices_Actions_FK` (`area_id`),
  CONSTRAINT `UserServices_Actions_FK` FOREIGN KEY (`area_id`) REFERENCES `Actions` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `UserServices_Users_FK` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='services user subscribed to';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserServices`
--

LOCK TABLES `UserServices` WRITE;
/*!40000 ALTER TABLE `UserServices` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserServices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL COMMENT 'The user''s username.',
  `email` varchar(320) NOT NULL COMMENT 'The email that the user provided.',
  `password` varchar(1000) DEFAULT NULL COMMENT 'The hashed password of the user.',
  `method` varchar(200) DEFAULT NULL COMMENT 'The method the user used to log in: local, google, github, etc...',
  `favicon` varchar(900) DEFAULT NULL COMMENT 'The link to the icon of the user account.',
  `admin` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Informs the server if the user is an administrator or not.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Users_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='The table in charge of tracking the user accounts.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Verification`
--

DROP TABLE IF EXISTS `Verification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Verification` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `term` mediumtext DEFAULT NULL COMMENT 'This is the identification for the code reference.',
  `definition` mediumtext NOT NULL COMMENT 'This is the content you want to store, i.e: the verification code.',
  `expiration` datetime DEFAULT NULL COMMENT 'The time left before the code expires.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Verification_UNIQUE` (`definition`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='This is the table in charge of storing the verification codes for user side events.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Verification`
--

LOCK TABLES `Verification` WRITE;
/*!40000 ALTER TABLE `Verification` DISABLE KEYS */;
/*!40000 ALTER TABLE `Verification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'terarea'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-1  0:00:00
