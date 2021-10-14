from television_program import TelevisionProgram

def main():
    #write your code below this line
    shows = []
    while True:
        tv_name = input("Name:")
        if not tv_name:
            break
        tv_duration = input("Duration:")
        show = TelevisionProgram(tv_name, tv_duration)
        shows.append(show)
    max = input("Program's maximum duration?")
    for show in shows:
        if (show.get_duration() <= max):
            print(show)

if __name__ == '__main__':
    main()
