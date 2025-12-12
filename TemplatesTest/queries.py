GET_ALL_TEMPLATES_QUERY = """
    select *
    from rbPrintTemplate rbP
    where rbP.deleted = 0
      and context != ''
    order by context;
"""