-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medicinas`
--

DROP TABLE IF EXISTS `medicinas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicinas` (
  `idmedicinas` int NOT NULL AUTO_INCREMENT,
  `nombremed` varchar(45) NOT NULL,
  `preciosmed` double NOT NULL,
  `casa farmaceutica` varchar(45) NOT NULL,
  `principio activo` varchar(45) NOT NULL,
  PRIMARY KEY (`idmedicinas`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicinas`
--

LOCK TABLES `medicinas` WRITE;
/*!40000 ALTER TABLE `medicinas` DISABLE KEYS */;
INSERT INTO `medicinas` VALUES (1,'Acetaminofen',0.07,'MK','paracetamol'),(2,'Acetosil',0.06,'Laboratorios Suizos','paracetamol'),(3,'Dorival',0.25,'Bayer','ibuprofeno'),(4,'Azitrosil',3.65,'Laboratorios Suizos','azitromicina'),(5,'Claritisil',1.06,'Laboratorios Suizos','desloratadina'),(6,'Alerfín',0.13,'Laboratorios López','clorfeniramina'),(7,'Nervitrán',0.2,'Laboratorios Suizos','lúpulo'),(8,'Celedexa',0.4,'Medikem Laboratorios','dexclorfeniramina'),(9,'Ciproxil LS',1.06,'Laboratorios Suizos','ciprofloxacina'),(10,'Nor-gerom forte',0.25,'Laboratorios Teramed','cinarizina'),(11,'Calsil Plus',0.18,'Laboratorios Suizos','calcio'),(12,'Propal10',0.08,'Pharmedic','propanolol'),(13,'Tavalam 160/5',0.9,'Pharmedic','valsartan'),(14,'Alamo 16',0.9,'Pharmedic','candesartan'),(15,'Budek plus',0.48,'Exeltis','budesonida');
/*!40000 ALTER TABLE `medicinas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-10 22:54:34
