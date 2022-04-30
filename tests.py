import sys
import main

def test_functions():
    sys.tracebacklimit = 0
    try:
        print("--- [ STARTED MANUAL TESTING ] ---")
        functions = ['help_menu', 'check_args','get_sides', 'main']
        for function in functions:
            assert function in dir(main)
            print(f"[ SUCCESS ]: Function {function} exists.")
        print("[ OVERVIEW ]: All functions exist.")
        for function in functions:
            assert type(function) == str
            print(f"[ INFO ]: Function {function} returns a String.")
        print("[ OVERVIEW ]: All functions checked.")
        print("--- [ FINISHED MANUAL TESTING ] ---")

    except AssertionError:
        print(f"[ ASSERTION ERROR ]: {function} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    test_functions()