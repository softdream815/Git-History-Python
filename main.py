import argparse
import gitUtils
import fileUtils

# original_repository_path = 'E:/git_history/golang-test-original'
# new_repository_path = 'E:/git_history/golang-test'


def start_git_copy(src, dst):
    gitUtils.git_checkout_to_commit(src, 'master')
    log_data = gitUtils.git_logs(src)
    fileUtils.reset_directory(dst)
    gitUtils.git_init(dst)
    for log in log_data:
        print(f'processing {log["id"]}')
        gitUtils.git_checkout_to_commit(src, log['id'])
        fileUtils.remove_files(dst)
        fileUtils.copy_files(src, dst)
        gitUtils.git_commit(dst, log['email'], log['message'], log['date'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
Copy one repository to another replacing the git user name.
    ''')
    parser.add_argument('src', help='original repository path')
    parser.add_argument('dst', help='destination directory')
    args = parser.parse_args()

    start_git_copy(args.src, args.dst)
