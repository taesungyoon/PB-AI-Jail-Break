import click

def main_banner():
    print(r"""
  _____      _                   _                    _
 |  __ \    (_)                 | |                  | |
 | |__) | __ _ ___  ___  _ __   | |__  _ __ ___  __ _| | __
 |  ___/ '__| / __|/ _ \| '_ \  | '_ \| '__/ _ \/ _` | |/ /
 | |   | |  | \__ \ (_) | | | | | |_) | | |  __/ (_| |   <
 |_|   |_|  |_|___/\___/|_| |_| |_.__/|_|  \___|\__,_|_|\_\

                       |___/ |___/                
    """)

# @click.command()
# @click.option(
#     '--fruit',
#     type=click.Choice(['apple', 'banana', 'cherry'], case_sensitive=False),
#     prompt='Choose a fruit',
#     help='선택 가능한 과일: apple, banana, cherry'
# )
# @click.option(
#     '--color',
#     type=click.Choice(['red', 'green', 'blue'], case_sensitive=True),
#     prompt='Choose a color',
#     help='선택 가능한 색상: red, green, blue'
# )
# def choose(fruit, color):
#     """선택지로 과일과 색상을 선택하는 프로그램."""
#     main_banner()  # 프로그램 시작 시 배너 출력
#     click.echo(f"You chose the fruit: {fruit}")
#     click.echo(f"You chose the color: {color}")

if __name__ == '__main__':
    main_banner()
    # choose()


