-- Dealing with null and blank values

Select *
From layoffs_staging2
Where total_laid_off Is Null
And percentage_laid_off Is Null;

Select *
from layoffs_staging2
where industry is null
or industry = '';


-- Change blanks to Nulls
Update layoffs_staging2
Set industry = null
where industry = '';

-- Self Join
Select *
from layoffs_staging2 t1
Join layoffs_staging t2
	On t1.company = t2.company
Where (t1.industry is null or t1.industry = '')
And t2.industry is not null;

Update layoffs_staging2 t1
Join layoffs_staging2 t2
	On t1.company = t2.company
Set t1.industry = t2.industry
Where t1.industry is null 
And t2.industry is not null;

-- Delete
Delete
from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null;

Alter table layoffs_staging2
drop column row_num;

Select * from layoffs_staging2;




