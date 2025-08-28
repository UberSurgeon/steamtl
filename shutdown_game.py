import os
import signal
import subprocess


def shutdown_game(game_task_name):
    try:
        # Find the process ID of Steam
        result = subprocess.run(
            ["tasklist", "/FI", f'IMAGENAME eq {game_task_name}.exe'],
            capture_output=True,
            text=True,
        )

        if f'{game_task_name}.exe' in result.stdout:
            # Extract the process ID
            lines = result.stdout.splitlines()
            for line in lines:
                if f'{game_task_name}.exe' in line:
                    pid = int(line.split()[1])
                    # Terminate the process
                    os.kill(pid, signal.SIGTERM)
                    print(f"{game_task_name} (PID: {pid}) has been terminated.")
                else:
                    print(f'{game_task_name} have been closed')
        print(f'{game_task_name} is not running.')

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    shutdown_game('russian_subway_dogs')
