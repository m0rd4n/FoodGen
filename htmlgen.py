import mealgen

def genhtml(mon_meal, genMonday):
    week = mealgen.genmeal(mon_meal, genMonday)
    mon = week[0]
    tue = week[1]
    wed = week[2]
    thu = week[3]
    fri = week[4]
    sat = week[5]
    sun = week[6]

    f = open("output/plan.html", "w")
    f.write("""<header>
        <meta charset="utf-8">
        <title>Essensplan</title>
        <style>
            table, th, td {border: 2px solid;}
            thead {background-color: #4d90fe}
            #plan {border-collapse: collapse;}
        </style>
    </header>
    
    <body>
        <h1><u>Essensplan</u></h1><br>
        <table id="plan" cellpadding="25">
            <thead>
                <tr>
                    <th>Montag</th>
                    <th>Dienstag</th>
                    <th>Mittwoch</th>
                    <th>Donnerstag</th>
                    <th>Freitag</th>
                    <th>Samstag</th>
                    <th>Sonntag</th>
                </tr>
            </thead>""")
    f = open("output/plan.html", "a")
    f.write(f"""        <tbody>
                <tr>
                    <td>{mon.frühstück}</td>
                    <td>{tue.frühstück}</td>
                    <td>{wed.frühstück}</td>
                    <td>{thu.frühstück}</td>
                    <td>{fri.frühstück}</td>
                    <td>{sat.frühstück}</td>
                    <td>{sun.frühstück}</td>
                </tr>
                <tr>
                    <td>{mon.mittag}</td>
                    <td>{tue.mittag}</td>
                    <td>{wed.mittag}</td>
                    <td>{thu.mittag}</td>
                    <td>{fri.mittag}</td>
                    <td>{sat.mittag}</td>
                    <td>{sun.mittag}</td>
                </tr>
                <tr>
                    <td>{mon.abend}</td>
                    <td>{tue.abend}</td>
                    <td>{wed.abend}</td>
                    <td>{thu.abend}</td>
                    <td>{fri.abend}</td>
                    <td>{sat.abend}</td>
                    <td>{sun.abend}</td>
                </tr>
                <tr>
                    <td>{mon.snack}</td>
                    <td>{tue.snack}</td>
                    <td>{wed.snack}</td>
                    <td>{thu.snack}</td>
                    <td>{fri.snack}</td>
                    <td>{sat.snack}</td>
                    <td>{sun.snack}</td>
                </tr>
            </tbody>
        </table>
    </body>""")
