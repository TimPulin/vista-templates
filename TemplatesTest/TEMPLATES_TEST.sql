select *
from rbPrintTemplate rbP
where rbP.deleted = 0
  and context != ''
order by context;