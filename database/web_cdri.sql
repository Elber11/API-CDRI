-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 08-05-2019 a las 14:35:53
-- Versión del servidor: 10.3.14-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `web_cdri`
--
CREATE DATABASE web_cdri CHARACTER SET 'UTF8Mb4' COLLATE 'utf8mb4_general_ci';
USE web_cdri;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client`
--

CREATE TABLE `client` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `cedula` varchar(8) NOT NULL,
  `client_status_id` tinyint(4) NOT NULL DEFAULT 1,
  `client_type_id` tinyint(4) UNSIGNED NOT NULL,
  `name` varchar(256) NOT NULL,
  `last_name` varchar(256) DEFAULT NULL,
  `address` varchar(256) NOT NULL,
  `email` varchar(256) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client_status`
--

CREATE TABLE `client_status` (
  `id` tinyint(4) NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `client_status`
--

INSERT INTO `client_status` (`id`, `code`, `description`) VALUES
(-1, 'ELIMINADO', 'Cliente eliminado'),
(1, 'ACTIVO', 'Cliente activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client_type`
--

CREATE TABLE `client_type` (
  `id` tinyint(4) UNSIGNED NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `client_type`
--

INSERT INTO `client_type` (`id`, `code`, `description`) VALUES
(1, 'NATURAL', 'Cliente natural'),
(2, 'JURÍDICO', 'Cliente jurídico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventory_flow`
--

CREATE TABLE `inventory_flow` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `inventory_flow_type_id` tinyint(4) UNSIGNED NOT NULL,
  `provider_id` bigint(20) UNSIGNED DEFAULT NULL,
  `product_id` bigint(20) UNSIGNED NOT NULL,
  `quantity` int(11) UNSIGNED NOT NULL,
  `unity_price` float NOT NULL,
  `total_price` float NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventory_flow_type`
--

CREATE TABLE `inventory_flow_type` (
  `id` tinyint(4) UNSIGNED NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inventory_flow_type`
--

INSERT INTO `inventory_flow_type` (`id`, `code`, `description`) VALUES
(1, 'COMPRO', 'Ingreso de productos por compras'),
(2, 'VENPRO', 'Salida de productos por ventas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(64) NOT NULL,
  `product_category_id` smallint(5) UNSIGNED NOT NULL,
  `product_status_id` tinyint(4) NOT NULL,
  `product_commercial_brand_id` smallint(5) UNSIGNED NOT NULL,
  `model` varchar(64) NOT NULL,
  `existence` int(10) UNSIGNED NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product_category`
--

CREATE TABLE `product_category` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `name` varchar(128) NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product_commercial_brand`
--

CREATE TABLE `product_commercial_brand` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `name` varchar(128) NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product_status`
--

CREATE TABLE `product_status` (
  `id` tinyint(4) NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `product_status`
--

INSERT INTO `product_status` (`id`, `code`, `description`) VALUES
(-1, 'ELIMINADO', 'Producto eliminado'),
(1, 'DISPONIBLE', 'Producto disponible para la venta'),
(2, 'NO DISPONIBLE', 'Producto a la espera de ser marcado como disponible'),
(3, 'AGOTADO', 'Producto agotado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provider`
--

CREATE TABLE `provider` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `rif` varchar(16) NOT NULL,
  `name` varchar(256) NOT NULL,
  `provider_status_id` tinyint(4) NOT NULL,
  `provider_reputation_id` tinyint(4) UNSIGNED NOT NULL,
  `fiscal_address` varchar(256) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `city` varchar(256) NOT NULL,
  `state` varchar(256) NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provider_reputation`
--

CREATE TABLE `provider_reputation` (
  `id` tinyint(4) UNSIGNED NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `provider_reputation`
--

INSERT INTO `provider_reputation` (`id`, `code`, `description`) VALUES
(1, 'Excelente', 'Excelente reputación del proveedor'),
(2, 'Buena', 'Buena reputación del proveedor'),
(3, 'Mala', 'Mala reputación del proveedor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provider_status`
--

CREATE TABLE `provider_status` (
  `id` tinyint(4) NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `provider_status`
--

INSERT INTO `provider_status` (`id`, `code`, `description`) VALUES
(-1, 'ELIMINADO', 'Proveedor Eliminado'),
(1, 'ACTIVO', 'Proveedor activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sale`
--

CREATE TABLE `sale` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` smallint(5) UNSIGNED DEFAULT NULL,
  `client_id` bigint(20) UNSIGNED DEFAULT NULL,
  `sale_status_id` tinyint(4) NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sale_status`
--

CREATE TABLE `sale_status` (
  `id` tinyint(4) NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sale_status`
--

INSERT INTO `sale_status` (`id`, `code`, `description`) VALUES
(-2, 'CANCELADA', 'Venta cancelada por el cliente'),
(-1, 'ELIMINADA', 'Venta eliminada'),
(1, 'COMPLETADA', 'Venta completa con éxito'),
(2, 'ESPERA', 'Venta a la espera de confirmación');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sold_products`
--

CREATE TABLE `sold_products` (
  `sale_id` bigint(20) UNSIGNED NOT NULL,
  `product_id` bigint(20) UNSIGNED NOT NULL,
  `quantity` smallint(6) NOT NULL,
  `unity_price` float NOT NULL,
  `total_price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(5) UNSIGNED NOT NULL,
  `name` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `user_level_id` tinyint(4) UNSIGNED NOT NULL,
  `user_status_id` tinyint(4) NOT NULL,
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `name`, `password`, `user_level_id`, `user_status_id`, `creation_date`) VALUES
(1, 'elber', '1234', 1, 1, '2019-03-04 20:23:32'),
(2, 'admin', '1234', 1, 1, '2019-03-18 00:10:23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_level`
--

CREATE TABLE `user_level` (
  `id` tinyint(4) UNSIGNED NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_level`
--

INSERT INTO `user_level` (`id`, `code`, `description`) VALUES
(1, 'ADMIN', 'Usuario administrador, completo acceso al sistema');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_status`
--

CREATE TABLE `user_status` (
  `id` tinyint(4) NOT NULL,
  `code` varchar(16) NOT NULL,
  `description` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_status`
--

INSERT INTO `user_status` (`id`, `code`, `description`) VALUES
(-2, 'SUSPENDIDO', 'Usuario suspendido del sistema'),
(-1, 'ELIMINADO', 'Usuario eliminado'),
(1, 'ACTIVO', 'Usuario activo para utilizar el sistema');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD KEY `client_status_id` (`client_status_id`),
  ADD KEY `client_type_id` (`client_type_id`);

--
-- Indices de la tabla `client_status`
--
ALTER TABLE `client_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `client_type`
--
ALTER TABLE `client_type`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventory_flow`
--
ALTER TABLE `inventory_flow`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_flow_type_id` (`inventory_flow_type_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `provider_id` (`provider_id`);

--
-- Indices de la tabla `inventory_flow_type`
--
ALTER TABLE `inventory_flow_type`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `product_category_id` (`product_category_id`),
  ADD KEY `product_status_id` (`product_status_id`),
  ADD KEY `product_commercial_brand_id` (`product_commercial_brand_id`);

--
-- Indices de la tabla `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `product_commercial_brand`
--
ALTER TABLE `product_commercial_brand`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `product_status`
--
ALTER TABLE `product_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `provider`
--
ALTER TABLE `provider`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rif` (`rif`),
  ADD KEY `provider_status_id` (`provider_status_id`),
  ADD KEY `provider_reputation_id` (`provider_reputation_id`);

--
-- Indices de la tabla `provider_reputation`
--
ALTER TABLE `provider_reputation`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `provider_status`
--
ALTER TABLE `provider_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sale`
--
ALTER TABLE `sale`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `sale_status_id` (`sale_status_id`);

--
-- Indices de la tabla `sale_status`
--
ALTER TABLE `sale_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sold_products`
--
ALTER TABLE `sold_products`
  ADD PRIMARY KEY (`sale_id`,`product_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`name`),
  ADD KEY `user_level_id` (`user_level_id`),
  ADD KEY `user_status_id` (`user_status_id`);

--
-- Indices de la tabla `user_level`
--
ALTER TABLE `user_level`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user_status`
--
ALTER TABLE `user_status`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `client`
--
ALTER TABLE `client`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `client_type`
--
ALTER TABLE `client_type`
  MODIFY `id` tinyint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `inventory_flow`
--
ALTER TABLE `inventory_flow`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventory_flow_type`
--
ALTER TABLE `inventory_flow_type`
  MODIFY `id` tinyint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `product`
--
ALTER TABLE `product`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `product_category`
--
ALTER TABLE `product_category`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `product_commercial_brand`
--
ALTER TABLE `product_commercial_brand`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `provider`
--
ALTER TABLE `provider`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `provider_reputation`
--
ALTER TABLE `provider_reputation`
  MODIFY `id` tinyint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sale`
--
ALTER TABLE `sale`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `client`
--
ALTER TABLE `client`
  ADD CONSTRAINT `client_ibfk_1` FOREIGN KEY (`client_status_id`) REFERENCES `client_status` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `client_ibfk_2` FOREIGN KEY (`client_type_id`) REFERENCES `client_type` (`id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `inventory_flow`
--
ALTER TABLE `inventory_flow`
  ADD CONSTRAINT `inventory_flow_ibfk_1` FOREIGN KEY (`inventory_flow_type_id`) REFERENCES `inventory_flow_type` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `inventory_flow_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `inventory_flow_ibfk_3` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`id`);

--
-- Filtros para la tabla `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_3` FOREIGN KEY (`product_status_id`) REFERENCES `product_status` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `product_ibfk_4` FOREIGN KEY (`product_category_id`) REFERENCES `product_category` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `product_ibfk_5` FOREIGN KEY (`product_commercial_brand_id`) REFERENCES `product_commercial_brand` (`id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `provider`
--
ALTER TABLE `provider`
  ADD CONSTRAINT `provider_ibfk_2` FOREIGN KEY (`provider_status_id`) REFERENCES `provider_status` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `provider_ibfk_3` FOREIGN KEY (`provider_reputation_id`) REFERENCES `provider_reputation` (`id`);

--
-- Filtros para la tabla `sale`
--
ALTER TABLE `sale`
  ADD CONSTRAINT `sale_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sale_ibfk_5` FOREIGN KEY (`sale_status_id`) REFERENCES `sale_status` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sale_ibfk_6` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `sold_products`
--
ALTER TABLE `sold_products`
  ADD CONSTRAINT `sold_products_ibfk_2` FOREIGN KEY (`sale_id`) REFERENCES `sale` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `sold_products_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_level_id`) REFERENCES `user_level` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`user_status_id`) REFERENCES `user_status` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
