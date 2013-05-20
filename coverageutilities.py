import io


def called_modules_filenames(cov):
        cov_report_output = io.StringIO()
        cov.report(file=cov_report_output)
        c = cov_report_output.getvalue().splitlines()
        good_lines = c[2:-2] if len(c)>5 else c[2:]
        return [ s.split()[0]+".py" for s in good_lines]
 
def called_coverage_data(cov):  
        ret = {}
        names= called_modules_filenames(cov)
        for n in names:
            module_fullname, stm_total, _, stm_not_executed, _ = cov.analysis2(n)
            ret[module_fullname]= len(stm_total) - len(stm_not_executed)
        return ret
    
