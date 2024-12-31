USE autisite;
CREATE TABLE registration (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each user',
    guardian_name VARCHAR(150) NOT NULL COMMENT 'Guardian’s full name',
    patient_name VARCHAR(150) NOT NULL COMMENT 'Patient’s full name',
    registration_date DATE NOT NULL COMMENT 'Registration date (mm/dd/yyyy format)',
    email VARCHAR(255) NOT NULL UNIQUE COMMENT 'User’s email address',
    password VARCHAR(200) NOT NULL COMMENT 'User password (hashed)',
    patient_birth_date DATE NOT NULL COMMENT 'Patient’s date of birth',
    genetic_history TEXT DEFAULT NULL COMMENT 'Details about genetic history',
    pregnancy_disease TEXT DEFAULT NULL COMMENT 'Details of any pregnancy-related diseases',
    other_disorders TEXT DEFAULT NULL COMMENT 'Details of any other disorders',
    terms_accepted BOOLEAN NOT NULL DEFAULT 0 COMMENT 'Whether terms and conditions are accepted (0/1)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Record creation timestamp',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Last updated timestamp'
) 
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
SHOW TABLES;
DESCRIBE registration;
