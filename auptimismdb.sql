-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema auptimism
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema auptimism
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `auptimism` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
USE `auptimism` ;

-- -----------------------------------------------------
-- Table `auptimism`.`auptimism_main_therapist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auptimism_main_therapist` (
  `therapist_id` INT NOT NULL AUTO_INCREMENT,
  `therapist_name` VARCHAR(255) NOT NULL,
  `profile_pic` VARCHAR(100) NOT NULL,
  `phone_no` INT NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `gender` VARCHAR(255) NOT NULL,
  `institute_name` VARCHAR(255) NOT NULL,
  `Designation` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`therapist_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auptimism_main_students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auptimism_main_students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `Father_name` VARCHAR(255) NOT NULL,
  `Mother_name` VARCHAR(255) NOT NULL,
  `email_father` VARCHAR(254) NOT NULL,
  `email_mother` VARCHAR(254) NOT NULL,
  `phoneno_father` INT NOT NULL,
  `phoneno_mother` INT NOT NULL,
  `address` LONGTEXT NOT NULL,
  `gender` VARCHAR(255) NOT NULL,
  `DOB` DATE NOT NULL,
  `profile_pic` VARCHAR(100) NOT NULL,
  `Medical_report` VARCHAR(100) NOT NULL,
  `past_report` VARCHAR(100) NOT NULL,
  `created_at` DATETIME(6) NOT NULL,
  `Updated_at` DATETIME(6) NOT NULL,
  `therapist_id_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `auptimism_main_stude_therapist_id_id_2141718f_fk_auptimism` (`therapist_id_id` ASC) VISIBLE,
  CONSTRAINT `auptimism_main_stude_therapist_id_id_2141718f_fk_auptimism`
    FOREIGN KEY (`therapist_id_id`)
    REFERENCES `auptimism`.`auptimism_main_therapist` (`therapist_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auptimism_main_activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auptimism_main_activity` (
  `activity_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` LONGTEXT NOT NULL,
  `tags` VARCHAR(255) NOT NULL,
  `level` VARCHAR(255) NOT NULL,
  `age` INT NOT NULL,
  `media` VARCHAR(100) NOT NULL,
  `student_id_id` INT NOT NULL,
  PRIMARY KEY (`activity_id`),
  INDEX `auptimism_main_activ_student_id_id_3c9a0c0c_fk_auptimism` (`student_id_id` ASC) VISIBLE,
  CONSTRAINT `auptimism_main_activ_student_id_id_3c9a0c0c_fk_auptimism`
    FOREIGN KEY (`student_id_id`)
    REFERENCES `auptimism`.`auptimism_main_students` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auptimism_main_iep`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auptimism_main_iep` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `therapist_name` VARCHAR(255) NOT NULL,
  `skill` VARCHAR(255) NOT NULL,
  `therapy_type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auptimism_main_institute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auptimism_main_institute` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `i_name` VARCHAR(255) NOT NULL,
  `i_description` LONGTEXT NOT NULL,
  `i_email` VARCHAR(254) NOT NULL,
  `i_phone` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `auptimism`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 49
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_group_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `auptimism`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `auptimism`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_user_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `auptimism`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `auptimism`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`auth_user_user_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `auptimism`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `auptimism`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `auptimism`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `auptimism`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`django_migrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `auptimism`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `auptimism`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
