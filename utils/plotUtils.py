import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plotBoxes(centroids, SEM, annotations=None, saveImg=False, saveImgPath=None):

    box_size = [100,100]
    plt.rcParams['figure.figsize'] = (16, 10)
    _, ax = plt.subplots(1)
    fig = plt.imshow(SEM,cmap='gray')
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    for i in range(len(centroids)):
        rect = patches.Rectangle((centroids[i][1]-box_size[1]/2.,centroids[i][0]-box_size[0]/2.),
                                box_size[0],box_size[1],linewidth=1,edgecolor='r',facecolor='none')
        ax.add_patch(rect)

    if annotations!=None:
        for i in range(len(annotations)):
            plt.text(centroids[i][1]-box_size[1]/2, centroids[i][0]+box_size[0]/2+30,
                    annotations[i],fontsize=10,color='red')

    if saveImg:
        plt.savefig(saveImgPath)

    plt.show()
