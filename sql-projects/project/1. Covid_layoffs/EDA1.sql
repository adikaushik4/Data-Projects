-- Exploratory Data Analysis

Select * from
layoffs_staging2;

Select Max(total_laid_off), Max(percentage_laid_off) -- 1 mean complete staff got laid off (
from layoffs_staging2;

Select *
from layoffs_staging2
where percentage_laid_off = 1
Order by funds_raised_millions DESC;

Select company, Sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 DESC;

Select min(`date`), max(`date`)
from layoffs_staging2;

Select industry, Sum(total_laid_off)
From layoffs_staging2
Group by industry
Order by 2 DESC;

Select country, Sum(total_laid_off)
From layoffs_staging2
Group by country
Order by 2 DESC;

Select year(`date`), Sum(total_laid_off)
from layoffs_staging2
group by year(`date`)
order by 1 desc;

Select company, Sum(percentage_laid_off)
from layoffs_staging2
group by company
order by 2 desc;


-- Rolling Totals
Select substring(`date`, 1, 7) as `Month`, sum(total_laid_off)
from layoffs_staging2
Where substring(`date`, 1, 7) is not null
Group by `Month`
Order by 1 Asc;

With Rolling_Total As
(
Select substring(`date`, 1, 7) as `Month`, sum(total_laid_off) as total_off
from layoffs_staging2
Where substring(`date`, 1, 7) is not null
Group by `Month`
Order by 1 Asc
)
Select `Month`, total_off,
Sum(total_off) Over(Order By `Month`) As rolling_total
from Rolling_Total;

-- Let's take a look at companies
Select company, Year(`date`), Sum(total_laid_off)
from layoffs_staging2
group by company, Year(`date`)
order by 3 ASC;




