-- Data Cleaning
CREATE TABLE layoffs_staging
Like layoffs;

Insert layoffs_staging
Select *
from layoffs;

-- Create new row,row_num to spot duplicates
Select *,
row_number() Over(Partition by company, industry, total_laid_off,
percentage_laid_off, `date`, stage, country, funds_raised_in_millions) As row_num
from layoffs_staging;

With duplicates_cte As (
Select *,
row_number() Over(Partition by company, industry, total_laid_off,
percentage_laid_off, `date`, stage, country, funds_raised_millions) As row_num
from layoffs_staging
)
Select * 
from duplicates_cte
where row_num> 1 ;

CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

Insert into layoffs_staging2
Select *,
row_number() Over(Partition by company, industry, total_laid_off,
percentage_laid_off, `date`, stage, country, funds_raised_millions) As row_num
from layoffs_staging;

Select * from layoffs_staging2;
--
Delete
from layoffs_staging2
where row_num>1;

-- Standardizing data

Select company, trim(company)
from layoffs_staging2;

Update layoffs_staging2
Set company = Trim(company);

Select *
from layoffs_staging2
where industry Like 'crypto%';

-- Update industry with Trim
Update layoffs_staging2
Set industry = 'Crypto'
Where industry Like 'Crypto%';


Select Distinct(country)
From layoffs_staging2
Order by 1;

--  Update Country column
Select distinct(country), Trim(Trailing '.' from country)
from layoffs_staging2
Order by 1; 

Update layoffs_staging2
Set country = Trim(Trailing '.' from country)
Where country like 'United States%';

-- Update Date column
Select `date`,
str_to_date(`date`, '%m/%d/%Y') as Date
from layoffs_staging2;

Update layoffs_staging2
Set date = str_to_date(`date`, '%m/%d/%Y');


-- Alter table
Alter Table layoffs_staging2
Modify Column `date` Date;
