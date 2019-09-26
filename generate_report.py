import os

"""It will generate consolidated html report from junit reports"""

def report_data(sstep, sdescrip, sstatus, stime):

    if sstatus.lower().strip() == 'passed':
        status_code = '&#10004;'
        status_color = '"color:green;'
    elif sstatus.lower().strip() == 'failed':
        status_code = '&#10060;'
        status_color = '"color:red;'
    elif sstatus.lower().strip() == 'skipped':
        status_code = '&#128693;skipped'
        status_color = '"color:blue;'
    else:
        status_code = ''

    if sstep == "Feature":
        if sstatus.lower().strip() == 'failed':
            step_code = '#FA8F78'
            status_code = sstatus.lower().strip().capitalize()
            status_color = '"color:black;'
        else:
            step_code = '#B9EC95'
            status_code = sstatus.lower().strip().capitalize()
            status_color = '"color:black;'

    elif sstep == "Scenario":
        step_code = '#36B2C1'
    else:
        step_code = '#B0C4DE'

    htmltag3 = '<tr style="background-color:' + step_code + ';"><td width="100" style="font-weight:bold">' + sstep
    htmltag3 = htmltag3 + '</td><td width="710" style="font-weight:bold">' + sdescrip
    htmltag3 = htmltag3 + '</td><td width="90" align="center" style="font-weight:bold;' + status_color + '">' + status_code
    htmltag3 = htmltag3 + '</td><td width="100" align="center" style="font-weight:bold">' + stime + '</td></tr>'
    return htmltag3


def generate_html_report():
    html = '<html><body style="background-color:#F8F8FF;font-family:callibri;"><title>Execution Report</title>'
    html = html + '<table width="1000" align="center" border="0" style="table-layout:fixed"><tr style="background-color:B0C4DE;">'
    html = html + '<td width="100" align="center" style="font-weight:bold">Step Details</td><td width="710" align="center" style="font-weight:bold">Step Description</td>'
    html = html + '<td width="90" align="center" style="font-weight:bold">Status</td><td width="100" align="center" style="font-weight:bold;">Run Time</td></tr>'
    htmltag2 = '</table></body></html>'
    scenario_status = ''
    report_dir = os.getcwd() + "/reports/"
    open(report_dir + 'feature.html', "w")
    f = open(report_dir + 'feature.html', "at")
    f.write(html)

    for file in os.listdir(report_dir):

        if file.endswith(".xml"):

            with open(report_dir + file) as input_file:
                lines = input_file.readlines()

                for line in lines:
                    line = line.lower().strip()

                    if "<testsuite" in line:
                        desc = line.split('" name="')[1].split('" skipped="')[0]
                        str_fail = line.split('failures="')[1].split('"')[0]
                        str_error = line.split('errors="')[1].split('"')[0]
                        int_time = line.split('time="')[1].split('"')[0]

                        if (int(str_fail) > 0) or (int(str_error) > 0):
                            status = 'failed'
                        else:
                            status = 'passed'
                        f.write(report_data("Feature", desc, status, int_time))

                    elif "failing step:" in line:
                        scenario_status = 'failed'
                        # scenario_time = line.split('failed in ')
                        pass

                    elif "scenario:" in line:
                        step_counter = 0
                        data_str = line.split('scenario:')
                        if not scenario_status == 'failed':
                            scenario_status = 'passed'
                            pass

                        f.write(report_data("Scenario", data_str[1], scenario_status, ""))
                        scenario_status = ''
                        pass

                    elif "given" in line:
                        str_given = line.split('...')
                        step_counter = int(step_counter) + 1
                        given_status = str_given[1].split(' in ')
                        f.write(report_data("Step-"+ str(step_counter), str_given[0], given_status[0], given_status[1]))
                        pass

                    elif "when" in line:
                        step_counter = int(step_counter) + 1
                        str_when = line.split('...')
                        when_status = str_when[1].split(' in ')
                        f.write(report_data("Step-"+ str(step_counter), str_when[0], when_status[0], when_status[1]))
                        pass

                    elif "then" in line:
                        step_counter = int(step_counter) + 1
                        str_then = line.split('...')
                        then_status = str_then[1].split(' in ')
                        f.write(report_data("Step-" + str(step_counter), str_then[0], then_status[0], then_status[1]))
                        pass

                    elif "and" in line:
                        step_counter = int(step_counter) + 1
                        str_and = line.split('...')
                        and_status = str_then[1].split(' in ')
                        f.write(report_data("Step-" + str(step_counter), str_and[0], and_status[0], and_status[1]))
                        pass

                    elif "but" in line:
                        step_counter = int(step_counter) + 1
                        str_but = line.split('...')
                        but_status = str_then[1].split(' in ')
                        f.write(report_data("Step-" + str(step_counter), str_but[0], but_status[0], but_status[1]))
                        pass
    f.write(htmltag2)


if __name__ == '__main__':
    generate_html_report()
