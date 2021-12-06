-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.21-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para redsocial
CREATE DATABASE IF NOT EXISTS `redsocial` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `redsocial`;

-- Volcando estructura para tabla redsocial.amigos
CREATE TABLE IF NOT EXISTS `amigos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_ID` int(11) DEFAULT NULL,
  `amigos_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_ID` (`usuario_ID`),
  KEY `amigos_ID` (`amigos_ID`),
  CONSTRAINT `amigos_ibfk_1` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`id`),
  CONSTRAINT `amigos_ibfk_2` FOREIGN KEY (`amigos_ID`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.amigos: ~69 rows (aproximadamente)
/*!40000 ALTER TABLE `amigos` DISABLE KEYS */;
INSERT INTO `amigos` (`id`, `usuario_ID`, `amigos_ID`) VALUES
	(6, 2, 3),
	(8, 2, 4),
	(10, 2, 6),
	(11, 2, 7),
	(12, 2, 8),
	(13, 2, 9),
	(14, 2, 10),
	(15, 2, 11),
	(16, 2, 12),
	(17, 3, 2),
	(18, 3, 4),
	(19, 3, 5),
	(20, 3, 6),
	(21, 3, 7),
	(22, 3, 8),
	(23, 4, 2),
	(24, 4, 3),
	(25, 4, 5),
	(26, 4, 9),
	(27, 4, 10),
	(28, 4, 11),
	(29, 4, 12),
	(30, 5, 2),
	(31, 5, 3),
	(32, 5, 4),
	(33, 5, 8),
	(34, 5, 7),
	(35, 5, 9),
	(36, 6, 2),
	(37, 6, 3),
	(38, 6, 7),
	(39, 6, 12),
	(40, 6, 11),
	(41, 6, 10),
	(42, 6, 9),
	(43, 7, 2),
	(44, 7, 3),
	(45, 7, 5),
	(46, 7, 12),
	(47, 7, 11),
	(48, 7, 10),
	(49, 7, 9),
	(50, 8, 2),
	(51, 8, 5),
	(52, 8, 11),
	(53, 9, 2),
	(54, 9, 4),
	(55, 9, 5),
	(56, 9, 6),
	(57, 9, 12),
	(58, 9, 11),
	(59, 10, 2),
	(60, 10, 4),
	(61, 10, 6),
	(62, 10, 7),
	(63, 10, 11),
	(64, 10, 12),
	(65, 11, 2),
	(66, 11, 4),
	(67, 11, 6),
	(68, 11, 7),
	(69, 11, 8),
	(70, 11, 9),
	(71, 11, 10),
	(72, 12, 2),
	(73, 12, 9),
	(74, 12, 10),
	(76, 27, 33),
	(78, 36, 35),
	(79, 36, 27);
/*!40000 ALTER TABLE `amigos` ENABLE KEYS */;

-- Volcando estructura para tabla redsocial.ciudad
CREATE TABLE IF NOT EXISTS `ciudad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `provincia_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `provincia_ID` (`provincia_ID`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`provincia_ID`) REFERENCES `provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.ciudad: ~15 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` (`id`, `nombre`, `provincia_ID`) VALUES
	(1, 'CABA', 1),
	(2, 'Rosario', 2),
	(3, 'General Pico', 3),
	(4, 'Cataluña', 4),
	(5, 'Carmelo', 5),
	(6, 'Montevideo', 6),
	(7, 'Concordia', 7),
	(8, 'La Paz', 8),
	(9, 'Potosi', 9),
	(10, 'Trinidad', 10),
	(11, 'Rio de Janeiro', 11),
	(12, 'Cuiaba', 11),
	(13, 'Berlin', 12),
	(14, 'Hamburgo', 13),
	(15, 'Valparaiso', 14);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;

-- Volcando estructura para vista redsocial.datos_usuarios
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `datos_usuarios` (
	`nombre` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`apellido` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Situacion Sentimental` VARCHAR(30) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Cantidad de amigos` BIGINT(21) NOT NULL
) ENGINE=MyISAM;

-- Volcando estructura para vista redsocial.domicilio_usuarios
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `domicilio_usuarios` (
	`Nombre usuario` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Ciudad` VARCHAR(50) NULL COLLATE 'utf8mb4_general_ci',
	`Provincia` VARCHAR(50) NULL COLLATE 'utf8mb4_general_ci',
	`Pais` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para tabla redsocial.pais
CREATE TABLE IF NOT EXISTS `pais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.pais: ~16 rows (aproximadamente)
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` (`id`, `nombre`) VALUES
	(1, 'Argentina'),
	(2, 'Bolivia'),
	(3, 'Brasil'),
	(4, 'Alemania'),
	(5, 'España'),
	(6, 'Uruguay'),
	(7, 'Chile'),
	(8, 'Colombia'),
	(9, 'Ecuador'),
	(10, 'Guyana'),
	(11, 'Guyana Francesa'),
	(12, 'Venezuela'),
	(13, 'Mexico'),
	(14, 'Puerto Rico'),
	(15, 'Paraguay'),
	(16, 'Peru');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;

-- Volcando estructura para tabla redsocial.posteo
CREATE TABLE IF NOT EXISTS `posteo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `usuario_ID` int(11) DEFAULT NULL,
  `tipoPosteo_ID` int(11) DEFAULT NULL,
  `creacionPosteo` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tipoPosteo_ID` (`tipoPosteo_ID`),
  KEY `usuario_ID` (`usuario_ID`),
  CONSTRAINT `posteo_ibfk_1` FOREIGN KEY (`tipoPosteo_ID`) REFERENCES `tipoposteo` (`id`),
  CONSTRAINT `posteo_ibfk_2` FOREIGN KEY (`usuario_ID`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.posteo: ~15 rows (aproximadamente)
/*!40000 ALTER TABLE `posteo` DISABLE KEYS */;
INSERT INTO `posteo` (`id`, `titulo`, `usuario_ID`, `tipoPosteo_ID`, `creacionPosteo`) VALUES
	(1, 'Nacimiento', 2, 4, '2021-01-01'),
	(2, 'Casamiento', 3, 1, '2006-01-01'),
	(3, 'Dia con amigos', 5, 1, '2010-01-01'),
	(4, 'Baile', 6, 5, '2015-01-01'),
	(5, 'Comida', 12, 2, '2019-01-01'),
	(6, 'Recuperandome', 8, 9, '2021-01-01'),
	(7, 'Navidad', 4, 2, '2011-01-01'),
	(8, 'Selfie', 5, 10, '2021-01-01'),
	(9, 'Mi hija', 3, 2, '2016-01-01'),
	(10, 'Recibido!', 8, 4, '2010-01-01'),
	(11, 'Selfie', 12, 1, '2021-11-26'),
	(12, 'Con mi novio!', 2, 10, '2021-08-26'),
	(13, 'Mis nietos!', 4, 1, '2020-08-26'),
	(14, 'Mirando una peli!', 12, 10, '2021-05-26'),
	(15, 'De pase por Tigre!', 2, 10, '2016-10-18');
/*!40000 ALTER TABLE `posteo` ENABLE KEYS */;

-- Volcando estructura para vista redsocial.posteo_informacion
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `posteo_informacion` (
	`titulo` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`nombre usuario` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Tipo de posteo` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`creacionPosteo` DATE NULL
) ENGINE=MyISAM;

-- Volcando estructura para tabla redsocial.provincia
CREATE TABLE IF NOT EXISTS `provincia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `pais_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pais_ID` (`pais_ID`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`pais_ID`) REFERENCES `pais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.provincia: ~24 rows (aproximadamente)
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
INSERT INTO `provincia` (`id`, `nombre`, `pais_ID`) VALUES
	(1, 'Buenos Aires', 1),
	(2, 'Santa Fe', 1),
	(3, 'La Pampa', 1),
	(4, 'Cataluña', 5),
	(5, 'Colonia', 6),
	(6, 'Montevideo', 6),
	(7, 'Entre Rios', 1),
	(8, 'La Paz', 2),
	(9, 'Potosi', 2),
	(10, 'Beni', 2),
	(11, 'Rio de Janeiro', 3),
	(12, 'Mato Grosso', 3),
	(13, 'Berlin', 4),
	(14, 'Hamburgo', 4),
	(15, 'Valparaiso', 7),
	(16, 'Termuco', 7),
	(17, 'Antioquia', 8),
	(18, 'Santa Elena', 9),
	(19, 'Demerara-Mahaica', 10),
	(20, 'Bolivar', 12),
	(21, 'Guadalajara', 13),
	(22, 'San Sebastian', 14),
	(23, 'San Pedro', 15),
	(24, 'Cuzco', 16);
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;

-- Volcando estructura para tabla redsocial.sentimental
CREATE TABLE IF NOT EXISTS `sentimental` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.sentimental: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `sentimental` DISABLE KEYS */;
INSERT INTO `sentimental` (`id`, `nombre`) VALUES
	(1, 'soltero/a'),
	(2, 'casado/a'),
	(3, 'en una relacion monogama'),
	(4, 'en una relacion abierta'),
	(5, 'es complicado'),
	(6, 'divorciado/a'),
	(7, 'sin apuros'),
	(8, 'desesperao/a'),
	(9, 'viudo/a'),
	(10, 'comprometido/a'),
	(11, 'en union civil');
/*!40000 ALTER TABLE `sentimental` ENABLE KEYS */;

-- Volcando estructura para tabla redsocial.tipoposteo
CREATE TABLE IF NOT EXISTS `tipoposteo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.tipoposteo: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `tipoposteo` DISABLE KEYS */;
INSERT INTO `tipoposteo` (`id`, `nombre`) VALUES
	(1, 'imagen'),
	(2, 'video'),
	(3, 'texto'),
	(4, 'evento'),
	(5, 'publicidad'),
	(6, 'contenido de marca'),
	(7, 'encuesta'),
	(8, 'articulo'),
	(9, 'recuerdos'),
	(10, 'historia instantanea');
/*!40000 ALTER TABLE `tipoposteo` ENABLE KEYS */;

-- Volcando estructura para tabla redsocial.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `contrasenia` varchar(50) NOT NULL,
  `ccontrasenia` varchar(50) NOT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `imagenPerfil` varchar(255) DEFAULT NULL,
  `imagenPortada` varchar(255) DEFAULT NULL,
  `biografia` text DEFAULT NULL,
  `fechaCreacionCuenta` date NOT NULL,
  `sentimental_ID` int(11) DEFAULT NULL,
  `ciudad_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sentimental_ID` (`sentimental_ID`),
  KEY `ciudad_ID` (`ciudad_ID`),
  CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`sentimental_ID`) REFERENCES `sentimental` (`id`) ON UPDATE NO ACTION,
  CONSTRAINT `usuario_ibfk_3` FOREIGN KEY (`ciudad_ID`) REFERENCES `ciudad` (`id`) ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla redsocial.usuario: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `email`, `celular`, `contrasenia`, `ccontrasenia`, `sexo`, `imagenPerfil`, `imagenPortada`, `biografia`, `fechaCreacionCuenta`, `sentimental_ID`, `ciudad_ID`) VALUES
	(2, 'Carla', 'Lopez', 'carlalopez@gmail.com', '1139876356', 'perro', 'perro', 'M', 'URL1', 'URL2', NULL, '2015-05-01', 1, 1),
	(3, 'Carina', 'Lopez', 'carinalopez@gmail.com', '1138765384', 'mueble123', 'mueble123', 'M', 'URL3', 'URL4', NULL, '2004-11-01', 2, 2),
	(4, 'Graciela Gladis', 'Martinez', 'gracielaGM@live.com', '1192384826', 'campo193', 'campo193', 'M', 'URL5', 'URL6', NULL, '1966-04-01', 5, 3),
	(5, 'German Alexis', 'Gonzalez', 'germangonzalez187@gmail.com', '3454176267', 'pueblo987', 'pueblo987', 'H', 'URL7', 'URL8', NULL, '2013-08-01', 1, 7),
	(6, 'Juan Ignacio', 'Madrid', 'jimadrid@gmail.com', '1187364765', 'computadoras', 'computadoras', 'H', 'URL9', 'URL10', NULL, '2010-10-01', 3, 1),
	(7, 'Rolando', 'Lopez', 'rolo@gmail.com', '1187264564', 'plomeria', 'plomeria', 'H', 'URL11', 'URL12', NULL, '1970-04-01', 6, 9),
	(8, 'Emiliano', 'Fernandez', 'emifernandez@gmail.com', '872654365', 'sistemas', 'sistemas', 'H', 'URL13', 'URL14', NULL, '2001-05-01', 7, 10),
	(9, 'Jesus', 'Aguirre', 'jesusaguirre@hotmail.com', '11873564764', 'peluqueria', 'peluqueria', 'H', 'URL15', 'URL16', NULL, '2010-08-01', 1, 1),
	(10, 'Mayra', 'Monteagudo', 'mayra@hotmail.com', '1189765456', 'esculpidas', 'esculpidas', 'M', 'URL17', 'URL18', NULL, '2015-03-01', 8, 1),
	(11, 'Celeste', 'Dominguez', 'celesdominguez@hotmail.com', '873876356', 'patines', 'patines', 'M', 'URL19', 'URL20', NULL, '2015-08-01', 6, 1),
	(12, 'Cintia', 'Almiron', 'cintiaalmiron@gmail.com', '871342642', 'tortas', 'tortas', 'M', 'URL21', 'URL22', NULL, '2005-04-01', 6, 7),
	(13, 'Valeria', 'Acosta', 'valeacosta@gmail.com', '113746553', 'programacion', 'programacion', 'M', 'URL23', 'URL24', NULL, '2021-01-23', 2, 1),
	(25, 'Lucas', 'Croci', 'lucascroci@gmail.com', '123456789011', 'THVjYXNDcm9jaTk5QA==', 'THVjYXNDcm9jaTk5QA==', 'H', 'a', 'a', 'A', '2021-12-02', 1, 1),
	(26, 'Pedro', 'Lopez', 'pedrolopez@gmail.com', '123455675323', 'cGVkcm9Mb3Blejk5QA==', 'cGVkcm9Mb3Blejk5QA==', 'H', 'null', 'null', 'Null', '2021-12-02', 1, 3),
	(27, 'Chico', 'Lopez', 'chiquito@gmail.com', '1111111111111', 'Q2hpcXVpdG85OUA=', 'Q2hpcXVpdG85OUA=', 'M', 'Selfie!', 'Paisaje', 'Perro adoptado', '2021-12-02', 9, 3),
	(29, 'Luisa', 'Martinez', 'martinez@gmail.com', '113908076543', 'THVpc2E5OUA=', 'THVpc2E5OUA=', 'M', 'null', 'null', 'Null', '2021-12-03', 2, 4),
	(30, 'Martin', 'Martinez', 'martinezmartin@gmail.com', '78676536478', 'TWFydGluOTlA', 'TWFydGluOTlA', 'H', 'a', 'a', 'A', '2021-12-03', 6, 3),
	(31, 'Cintia', 'Almiron', 'almironcintia@gmail.com', '12365478398', 'Q2ludGlhOTlA', 'Q2ludGlhOTlA', 'M', 'url', 'url', 'Url', '2021-12-03', 8, 3),
	(33, 'Silvia', 'Bel', 'silviabel@gmail.com', '67487635623', 'U2lsdmlhOTlA', 'U2lsdmlhOTlA', 'M', 'a', 'a', 'A', '2021-12-03', 4, 7),
	(34, 'Ramiro', 'Ruibio', 'ramiro@gmail.com', '1234565454345', 'UmFtaXJvOTlA', 'UmFtaXJvOTlA', 'H', 'null', 'null', 'Null', '2021-12-06', 6, 12),
	(35, 'Nacho', 'Naxo', 'nacho@gmail.com', '67654567879', 'TmFjaG85OUA=', 'TmFjaG85OUA=', 'H', NULL, NULL, NULL, '2021-12-06', 8, 6),
	(36, 'Joel', 'Lopez', 'joellopez@gmail.com', '787656454345', 'TG9wZXo5OUA=', 'TG9wZXo5OUA=', 'H', NULL, NULL, NULL, '2021-12-06', 8, 9);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

-- Volcando estructura para vista redsocial.datos_usuarios
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `datos_usuarios`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `datos_usuarios` AS SELECT usuario.nombre,usuario.apellido,sentimental.nombre AS "Situacion Sentimental", COUNT(amigos.usuario_ID) AS "Cantidad de amigos" 
FROM usuario
JOIN sentimental ON sentimental.id = usuario.sentimental_id 
JOIN amigos ON amigos.usuario_id = usuario.id
GROUP BY usuario.nombre ;

-- Volcando estructura para vista redsocial.domicilio_usuarios
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `domicilio_usuarios`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `domicilio_usuarios` AS SELECT usuario.nombre AS "Nombre usuario", ciudad.nombre AS "Ciudad", provincia.nombre AS "Provincia", pais.nombre AS "Pais" FROM usuario
JOIN ciudad ON ciudad.id = usuario.ciudad_ID
JOIN provincia ON provincia.id = ciudad.provincia_ID
JOIN pais ON pais.id = provincia.pais_ID ;

-- Volcando estructura para vista redsocial.posteo_informacion
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `posteo_informacion`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `posteo_informacion` AS SELECT posteo.titulo, usuario.nombre AS "nombre usuario", tipoposteo.nombre AS "Tipo de posteo", posteo.creacionPosteo FROM posteo
JOIN usuario ON usuario.id = posteo.usuario_ID 
JOIN tipoposteo ON tipoposteo.id = posteo.tipoposteo_id ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
