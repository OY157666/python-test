def print_file_info(file_name):
    """

    :param file_name:
    :return:
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现异常{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    # print_file_info("E:\\o'y'j's\\Documents\\test.txt")
    append_to_file("E:\\o'y'j's\\Documents\\test.txt","qwert")