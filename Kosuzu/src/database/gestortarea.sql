-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-03-2026 a las 17:58:02
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestortarea`
--
CREATE DATABASE IF NOT EXISTS `gestortarea` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `gestortarea`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tareas`
--

CREATE TABLE IF NOT EXISTS `tareas` (
  `ID_tarea` int(11) NOT NULL,
  `ID_usuario` int(11) NOT NULL,
  `Nombre_tarea` varchar(256) NOT NULL,
  `completada` tinyint(1) NOT NULL,
  `tipo` enum('a','a','a','') NOT NULL,
  `Estado` enum('a','a','a','','') NOT NULL,
  `prioridad` enum('a','a','a','') NOT NULL,
  `descripcion` varchar(256) NOT NULL,
  `fecha_lim` date NOT NULL,
  `fecha_com` date NOT NULL,
  PRIMARY KEY (`ID_tarea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncar tablas antes de insertar `tareas`
--

TRUNCATE TABLE `tareas`;
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID_usuario` int(11) NOT NULL,
  `Nombre` varchar(256) NOT NULL,
  `apellido` varchar(256) NOT NULL,
  `contra` varchar(256) NOT NULL,
  `correo` varchar(256) NOT NULL,
  `fecha_regis` date NOT NULL,
  `ultimo_acce` date NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `foto_per` varchar(265) NOT NULL,
  PRIMARY KEY (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncar tablas antes de insertar `usuarios`
--

TRUNCATE TABLE `usuarios`;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
