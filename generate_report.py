import os
"""It will generate consolidated html report from junit reports"""
def report_data(sstep, sdescrip, sstatus, stime):
    if sstatus.lower().strip() == 'passed':
        status_code = '&#9989;'
    elif sstatus.lower().strip() == 'failed':
        status_code = '&#10060;'
    else:
        status_code = sstatus
    if sstep == "Feature":
        step_code = '#F8F8FF'
    elif sstep == "Scenario":
        step_code = '36B2C1'
    else:
        step_code = 'B0C4DE'
    htmltag3 = '<tr style="background-color:' + step_code + ';"><td width="100" style="font-weight:bold">' + sstep
    htmltag3 = htmltag3 + '</td><td width="725" style="font-weight:bold">' + sdescrip
    htmltag3 = htmltag3 + '</td><td width="75" style="font-weight:bold;">' + status_code
    htmltag3 = htmltag3 + '</td><td width="100" style="font-weight:bold">' + stime + '</td></tr>'
    return htmltag3


def generate_html_report():

    html = '<html><body style="background-color:#F8F8FF;font-family:callibri;"><title>Execution Report</title>'
    html = html + '<table width="1000" align="center" border="0" style="table-layout:fixed"><tr style="background-color:B0C4DE;">'
    html = html + '<td width="100" style="font-weight:bold">Step</td><td width="725" style="font-weight:bold">Description</td>'
    html = html + '<td width="75" style="font-weight:bold">Status</td><td width="100" style="font-weight:bold;">Time</td></tr>'
    htmltag2 = '</table></body></html>'

    report_dir = os.getcwd() + "/reports/"
    ff = open(report_dir + 'feature.html', "w")
    f = open(report_dir + 'feature.html', "at")
    f.write(html)

    for file in os.listdir(report_dir):
        if file.endswith(".xml"):
            with open(report_dir + file) as input_file:
                lines = input_file.readlines()
                for line in lines:
                    line = line.lower().strip()
                    if "<testsuite" in line:
                        desc = line.split('" name="')[1].split('."')[0]
                        status = line.split('failures="')[1].split('"')[0]
                        stime = line.split('time="')[1].split('"')[0]
                        if int(status) > 0:
                            status = 'failed'
                        f.write(report_data("Feature", desc, status, stime))
                    elif "failing step:" in line:
                        scenario_status = 'failed'
                        scenario_time = line.split('failed in ')
                        pass
                    elif "scenario:" in line:

                        data_str = line.split('scenario:')
                        f.write(report_data("Scenario", data_str[1], scenario_status, ""))
                    elif "given" in line:

                        str_given = line.split('...')
                        given_status = str_given[1].split(' in ')
                        f.write(report_data("Step", str_given[0], given_status[0], given_status[1]))
                    elif "when" in line:
                        str_when = line.split('...')
                        when_status = str_when[1].split(' in ')
                        f.write(report_data("Step", str_when[0], when_status[0], when_status[1]))

                    elif "then" in line:

                        str_then = line.split('...')
                        then_status = str_then[1].split(' in ')
                        f.write(report_data("Step", str_then[0], then_status[0], then_status[1]))

    f.write(htmltag2)

# if __name__ == '__main__':
#     generateHtmlReport()
