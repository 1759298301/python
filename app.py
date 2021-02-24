# vega
# ---------------------------
# app
# ---------------------------
# Administrator 2021/2/23 11:15 
# ---------------------------

from colorama import Style,Fore
from service.user_service import UserService
from service.new_service import NewsService
from service.role_service import RoleService
from getpass import getpass
import os
import sys
from time import sleep

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()

while True:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX,'\n\t=================')
    print(Fore.LIGHTBLUE_EX,'\n\t欢迎来到新闻管理系统')
    print(Fore.LIGHTBLUE_EX,'\n\t=================')
    print(Fore.LIGHTYELLOW_EX,'\n\t1.登录系统')
    print(Fore.LIGHTYELLOW_EX,'\n\t2.退出系统')
    print(Style.RESET_ALL)
    opt = input('\n\t请输入操作编号:')
    if opt == '1':
        username = input('\n\t请输入用户名:')
        password = getpass('\n\t请输入密码:')
        # 比较登录的结果
        result = __user_service.login(username,password)

        # 登录成功
        if result == True:
            os.system('cls')
            print(Fore.LIGHTMAGENTA_EX,'\n\t登录成功(2秒后跳转)')
            sleep(3)
            # 验证权限
            role = __user_service.sear_user_role(username)
            while True:
                os.system('cls')
                if role == '编辑者':
                    print('编辑者')
                elif role == '管理员':
                    print(Fore.LIGHTBLUE_EX, '\n\t1.新闻管理')
                    print(Fore.LIGHTBLUE_EX, '\n\t2.用户管理')
                    print(Fore.LIGHTGREEN_EX, '\n\tback.退出登录')
                    print(Fore.LIGHTGREEN_EX, '\n\texit.退出系统')
                    print(Style.RESET_ALL)
                    opt = input('\n\t请输入操作编号:')
                    if opt == 'back':
                        break
                    elif opt == 'exit':
                        sys.exit(0)
                    # 进入新闻管理
                    elif opt == '1':
                        while True:
                            os.system('cls')
                            print(Fore.LIGHTBLUE_EX, '\n\t1.审批新闻')
                            print(Fore.LIGHTBLUE_EX, '\n\t2.删除新闻')
                            print(Fore.LIGHTBLUE_EX, '\n\tback.返回上一层')
                            print(Style.RESET_ALL)
                            opt = input('\n\t请输入操作编号:')
                            # 审批新闻
                            if opt == '1':
                                page = 1
                                while True:
                                    os.system('cls')
                                    result = __news_service.search_unreview_news(page)
                                    page_count = __news_service.search_unreview_news_page_count()

                                    # 每页展示的新闻数量
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX, '\n\t{}\t{}\t\t{}\t{}'.format((index+1)+(page-1)*5,one[1],one[2],one[3]))
                                    print(Fore.LIGHTGREEN_EX,'\n\t{}/{}'.format(page,page_count))
                                    print(Fore.LIGHTYELLOW_EX,'\n\t------------------------------')
                                    print(Fore.LIGHTBLUE_EX, '\n\tback.上一层')
                                    print(Fore.LIGHTBLUE_EX, '\n\tprev.上一页')
                                    print(Fore.LIGHTBLUE_EX, '\n\tnext.下一页')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t请输入操作编号:')
                                    try:
                                        if opt == 'prev' and page == 1 or opt == 'next' and page==page_count:
                                            continue
                                        if opt == 'back':
                                            break
                                        elif opt == 'prev':
                                            page-=1
                                        elif opt == 'next':
                                            page+=1
                                        elif int(opt)>(page-1)*5 and int(opt)<=(page-1)*5+len(result):
                                            __news_service.update_unreview_news(result[int(opt)-5*page+4][0])
                                            # 实时查询待审批新闻的数量
                                            page_count = __news_service.search_unreview_news_page_count()
                                            if page_count < page:
                                                page-=1
                                    except Exception as e:
                                        pass
                            # 删除新闻
                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    page_count = __news_service.search_news_page_count()
                                    result = __news_service.search_news(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print('\n\t{}\t{}\t{}\t{}'.format((page-1)*5+index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTYELLOW_EX, '\n\t{}/{}'.format(page,page_count))
                                    print(Fore.LIGHTGREEN_EX,'\n\t-------------------------------')
                                    print(Fore.LIGHTRED_EX, '\n\tback.返回上一层')
                                    print(Fore.LIGHTRED_EX, '\n\tprev.返回上一层')
                                    print(Fore.LIGHTRED_EX, '\n\tnext.返回上一层')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t请输入操作编号:')
                                    try:
                                        if opt == 'prev' and page == 1 or opt == 'next' and page == page_count:
                                            continue
                                        if opt == 'back':
                                            break
                                        elif opt == 'prev':
                                            page -= 1
                                        elif opt == 'next':
                                            page += 1
                                        elif int(opt) > (page - 1) * 5 and int(opt) <= (page - 1) * 5 + len(result):
                                            __news_service.delete_news_by_id(result[int(opt) - 5 * page + 4][0])
                                            # 实时查询总新闻的页数
                                            page_count = __news_service.search_news_page_count()
                                            if page_count < page:
                                                page -= 1
                                    except Exception as e:
                                        pass
                            # 返回上一层
                            elif opt == 'back':
                                break
                    # 进入用户管理
                    elif opt == '2':
                        while True:
                            os.system('cls')
                            print(Fore.LIGHTBLUE_EX, '\n\t1.添加用户')
                            print(Fore.LIGHTBLUE_EX, '\n\t2.修改用户')
                            print(Fore.LIGHTBLUE_EX, '\n\t3.删除用户')
                            print(Fore.LIGHTBLUE_EX, '\n\tback.上一层')
                            print(Fore.LIGHTYELLOW_EX,'\n\t----------')
                            print(Style.RESET_ALL)
                            opt = input('\n\t请输入操作编号:')
                            # 添加用户
                            if opt == '1':
                                # 控制添加用户的次数，失败3次强制返回上一级
                                input_count = 0
                                while True:
                                    os.system('cls')
                                    if input_count >= 3:
                                        print(Fore.LIGHTRED_EX,'\n\t失败次数过多,强制返回上一级')
                                        sleep(2)
                                        break
                                    username = input('\n\t请输入用户名:')
                                    password = input('\n\t请输入密码:')
                                    secend_password = input('\n\t请确认密码:')
                                    if password != secend_password:
                                        print(Fore.LIGHTRED_EX,'\n\t两次密码不一致，2秒后返回')
                                        sleep(2)
                                        break
                                    email = input('\n\t请输入邮箱:')
                                    role = __role_service.search_role()
                                    for index in range(len(role)):
                                        print(Fore.LIGHTBLUE_EX, '\n\t{}.{}'.format(index+1,role[index][1]))
                                    role_id = input('\n\t请选择权限:')
                                    print(Fore.LIGHTYELLOW_EX, '\n\t---------------')
                                    # 获取用户表中的已有用户名
                                    user_name = __user_service.search_username()
                                    usernameList = []
                                    for value in user_name:
                                        usernameList.append(value[0])
                                    if username in usernameList:
                                        print(Fore.LIGHTRED_EX, '\n\t用户名重复，2秒后返回')
                                        sleep(2)
                                        break
                                    try:
                                        if int(role_id) >= 1 and int(role_id) <= len(role):
                                            true_role_id = role[int(role_id)-1][0]
                                            __user_service.insert_user(username,password,email,true_role_id)
                                            print(Fore.LIGHTRED_EX,'\n\t添加成功，2秒后返回')
                                            sleep(2)
                                            break
                                        else:
                                            print(Fore.LIGHTRED_EX, '\n\t输入不合法，重新输入')
                                            input_count += 1
                                            sleep(2)
                                            print(Style.RESET_ALL)
                                    except Exception as e:
                                        print(Fore.LIGHTRED_EX,'\n\t输入不合法，重新输入')
                                        input_count += 1
                                        sleep(2)
                                        print(Style.RESET_ALL)
                            # 修改用户
                            elif opt == '2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    page_count = __user_service.search_user_page_count()
                                    result = __user_service.search_user(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,'\n\t{}\t{}\t{}\t{}'.format((page-1)*5+index+1,one[0],one[1],one[2]))
                                    print(Fore.LIGHTRED_EX,'\n\t{}/{}'.format(page,page_count))
                                    print(Fore.LIGHTYELLOW_EX,'\n\t-------------------------')
                                    print(Fore.LIGHTCYAN_EX,'\n\tback.上一层')
                                    print(Fore.LIGHTCYAN_EX, '\n\tprev.上一页')
                                    print(Fore.LIGHTCYAN_EX, '\n\tnext.下一层')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\t请输入操作编号:')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page-=1
                                    elif opt == 'next' and page < page_count:
                                        page+=1
                                    elif int(opt)>(page-1)*5 and int(opt)<=(page-1)*5+len(result):
                                        old_username = result[int(opt)-(page-1)*5-1][0]
                                        while True:
                                            os.system('cls')
                                            print(Style.RESET_ALL)
                                            username = input('\n\t请输入用户名:')
                                            password = input('\n\t请输入密码:')
                                            second_pwd = input('\n\t请确认密码:')
                                            if password != second_pwd:
                                                os.system('cls')
                                                print(Fore.LIGHTRED_EX,'\n\t两次密码输入不一致,请重新选择')
                                                sleep(1)
                                            email = input('\n\t请输入邮箱:')
                                            # 展示权限列表
                                            index_list = []
                                            role_list = __role_service.search_role()
                                            for index in range(len(role_list)):
                                                one = role_list[index]
                                                print(Fore.LIGHTGREEN_EX,'\n\t{}\t{}'.format(index+1,one[1]))
                                                index_list.append(str(index+1))
                                            print(Style.RESET_ALL)
                                            opt = input('\n\t请选择权限')
                                            while True:
                                                if opt in index_list:
                                                    break
                                            role_id = role_list[int(opt)-1][0]
                                            __user_service.update_user_by_username(username,password,email,role_id,old_username)
                                            os.system('cls')
                                            print(Fore.LIGHTRED_EX,'\n\t修改成功，2秒后返回')
                                            sleep(2)
                                            break

                    # 其他选项
                    else:
                        print(Fore.LIGHTRED_EX,'\n\t没有此选项，请重新输入')
                        sleep(1)
                        os.system('cls')
        # 登录失败
        else:
            os.system('cls')
            print(Fore.LIGHTMAGENTA_EX,'\n\t登录失败(2秒后返回)')
            sleep(3)
# 退出登录
    elif opt == '2':
        sys.exit(0)


