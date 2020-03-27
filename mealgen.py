import random


class Wochentag(object):
    def __init__(self, frühstück, mittag, abend, snack):
        self.frühstück = frühstück
        self.mittag = mittag
        self.abend = abend
        self.snack = snack

    def __str__(self):
        return f"================\n{self.frühstück}\n{self.mittag}\n{self.abend}\n{self.snack}\n================\n"

def genmeal(mon_meal, genMonday):
    f_meals = [line.rstrip() for line in open("gerichte/frühstück.txt")]
    m_meals = [line.rstrip() for line in open("gerichte/mittagessen.txt")]
    a_meals = [line.rstrip() for line in open("gerichte/abendessen.txt")]
    s_meals = [line.rstrip() for line in open("gerichte/snacks.txt")]

    if genMonday:
        mittag = random.choice(m_meals)
        mon = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        tue = Wochentag(random.choice(f_meals), mon.mittag, random.choice(a_meals), random.choice(s_meals))
        m_meals.remove(mittag)
        mittag = random.choice(m_meals)
        wed = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        thu = Wochentag(random.choice(f_meals), wed.mittag, random.choice(a_meals), random.choice(s_meals))
        m_meals.remove(mittag)
        mittag = random.choice(m_meals)
        fri = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        sat = Wochentag(random.choice(f_meals), fri.mittag, random.choice(a_meals), random.choice(s_meals))
        m_meals.remove(mittag)
        mittag = random.choice(m_meals)
        sun = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
    else:
        mon = Wochentag(random.choice(f_meals), str(mon_meal + "\n"), random.choice(a_meals), random.choice(s_meals))
        mittag = random.choice(m_meals)
        tue = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        wed = Wochentag(random.choice(f_meals), tue.mittag, random.choice(a_meals), random.choice(s_meals))
        m_meals.remove(mittag)
        mittag = random.choice(m_meals)
        thu = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        fri = Wochentag(random.choice(f_meals), thu.mittag, random.choice(a_meals), random.choice(s_meals))
        m_meals.remove(mittag)
        mittag = random.choice(m_meals)
        sat = Wochentag(random.choice(f_meals), mittag, random.choice(a_meals), random.choice(s_meals))
        sun = Wochentag(random.choice(f_meals), sat.mittag, random.choice(a_meals), random.choice(s_meals))

    return [mon, tue, wed, thu, fri, sat, sun]
