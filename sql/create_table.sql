-- MySQL
CREATE TABLE `price_tracker`.`table_name` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `price` DECIMAL(7, 2),
  `date` DATE,
  `time` TIME,
  PRIMARY KEY (`id`));

-- SQL Server
CREATE TABLE price_tracker.table_name (
  id INT IDENTITY(1,1) PRIMARY KEY,
  price DECIMAL(7, 2),
  date DATE,
  time TIME);
