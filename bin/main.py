import ctypes
import net_state
import sys


def __is_admin():
    """
    Return true if user has the permission of admin.
    :return: 1 or 0 that represents the true or false.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def __main():
    if __is_admin():
        # 主程序写在这里
        net_state.do_set_dns()
    else:
        # 以管理员权限重新运行程序
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == "__main__":
    __main()
