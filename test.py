cornerimg = kernelApply(sobelKernelF, n_image)
cornerimg = kernelApply(sobelKernelS, n_image)
cornerimg = kernelApply(robertsKernelF, n_image)
cornerimg = kernelApply(robertsKernelS, n_image)



n_image = np.around(np.divide(gray_image, 255.0), decimals=1)



BoxLayout:
        size: root.width,root.height
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            size_hint:1, 1
            TextInput:
                id: desired
                multiline: False
                font_size: 40
            TextInput:
                id: quantity
                multiline: False
                font_size: 40
            TextInput:
                id: value
                multiline: False
                font_size: 40
        Button:
            id: insert
            background_normal: ""
            background_color: utils.get_color_from_hex('#A76EDE')
            text:"Insert"
            on_release:
                root.inputValues()
        Button:
            text:"Solve"
            on_release:
                root.appSolver()
        Label:
            id: answer
            font_size: 40
            color: utils.get_color_from_hex('#A967D5')




    quantity: quantity
    value: value
    desired: desired
    answer: answer
    insert: insert




m,n = data.shape
with open('DataSet.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    for i in range(0,len(data)):
        image = imread("dataSet/letters/"+data[i][2])
        shmolldata = [data[i][0],data[i][1],image]
        print(shmolldata)
        writer.writerow(shmolldata)



            for i in range(0,len(data)):
        image = cv2.imread("dataSet/letters/"+data[i][2])
        shmolldata = [data[i][0],data[i][1],image]
        print(shmolldata)
        writer.writerow(shmolldata)






        Camera:
            id: camera
            resolution: 640, 640
            play:False
            index:-1