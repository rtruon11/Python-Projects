drugs = {
    'Prinivil': {
        'Lisinopril': {
            'Strengths': ['10 mg'],
        }
    },

    'Zocor': {
        'Simvastatin': {
            'Strengths': ['10 mg'],
        }
    },

    'Synthroid': {
        'Levothyroxine': {
            'Strengths': ['10 mg'],
        }
    },

    'Amoxil': {
        'Amoxicillin': {
            'Strengths': ['10 mg'],
        }
    },

    'Zithromax': {
        'Azithromycin': {
            'Strengths': ['10 mg'],
        }
    },

    'Microzide': {
        'Hydro-chlorothiazide': {
            'Strengths': ['10 mg'],
        }
    },

    'Norvasc': {
        'Amlodipine': {
            'Strengths': ['10 mg'],
        }
    },

    'Xanax': {
        'Alprazolam': {
            'Strengths': ['10 mg'],
        }
    },

    'Glucophage': {
        'Metformin': {
            'Strengths': ['10 mg'],
        }
    },

    'Lipitor': {
        'Atorvastatin': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

    'Prilosec': {
        'Omeprazole': {
            'Strengths': ['10 mg'],
        }
    },

}

while 1 == 1:

    code = int(input('Enter code number 1-7 (Enter 6 for instructions or 7 to exit): '))

    def brand():
        brandsearch = str(input('name of Brand drug: '))
        if brandsearch in drugs:
            print(drugs[brandsearch])

        else:
            print("Artist not found")

    def generic():
        genericsearch = str(input('name of album:  '))
        for k in drugs:
            if genericsearch in drugs[k]:
                print(k, (drugs[k][genericsearch]['Strengths']))

    def all_artists():
        for k in drugs.keys():
            print(k)

    def all_albumns():
        for artist in drugs:
            print(artist)
            for album in drugs[artist].keys():
                print(album, drugs[artist][album]['Strengths'])

    def all_songs():
        for artist in drugs:
            for album in drugs[artist].keys():
                print (drugs[artist][album]['songs'])

    def instructions():
        print ('This program searches for artist, album, song, and year')
        print ('Please enter the numeric code to determine the operation.')
        print ('Code = 1 Search artist for album')
        print ('Code = 2 Search album for artist')
        print ('Code = 3 Displays all artist')
        print ('Code = 4 Displays all albums')
        print ('Code = 5 Displays all songs')
        print ('Code = 6 Print instructions')
        print ('Code = 7 Quit')

    if (code == 1):
        brand()

    if (code == 2):
        generic()

    if (code == 3):
        all_artists()

    if (code == 4):
        all_albumns()

    if (code == 5):
        all_songs()

    if (code == 6):
        instructions()

    if (code == 7):
        quit()
