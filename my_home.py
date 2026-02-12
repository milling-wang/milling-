'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','知识答题'])
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page_1():
    '''我的兴趣推荐'''
    st.snow()
    tab11, tab22,tab33 = st.tabs(['小说','电影','音乐'])
    with tab11:
        st.write('推荐的小说')
        st.write('-------------------')
    with tab22:

        st.write('我要推荐长安三万里')
        st.text('《长安三万里》该片以盛唐为背景，讲述安史之乱爆发后数年，整个长安因战争而陷入混乱，身处局势之中的高适回忆起自己与李白的过往的故事')
        st.image('长安三万里.jpg')
        st.write('-------------------')
    with tab33:
        with open('霞光.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        #st.video('https://example.com/video.mp4', caption='网络视频示例')
    

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        tab1, tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,0,1,2))
        

def page_3():
    '''我的智能词典'''
    st.header("📚智能词典",anchor=False,divider="rainbow")
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
        
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
        
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
 
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        #st.write(words_dict[word])
        info = words_dict[word]
        st.write(f'编号：{info[0]}，中文：{info[1]}')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1

        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word=='name':
            st.write('恭喜你触发彩蛋，你获得本站主的名字：apple')
        if word=='snow':
            st.snow()
        if word=='balloon':
            st.balloons()
            
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == '小迪':
            with st.chat_message('小迪'):
                st.write(i[1],':',i[2])

    name = st.selectbox('我是……', ['阿短', '编程猫','小迪'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)   
        
def page_5():
    '''知识答题'''
    pass    

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page=='知识答题':
    page_5()



