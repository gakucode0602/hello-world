#include "opencv2/opencv.hpp"
#include "opencv2\highgui\highgui.hpp"
#include<iostream>
using namespace std;
using namespace cv;
int main()
{
    system("cls");
    VideoCapture cap(0);
    if(!cap.isOpened())
    {
        cout << "Change the camera port number " << endl;
        return -1;
    }
    while(true)
    {
        Mat frame;
        cap.read(frame);
        imshow("camera",frame);
        if(waitKey(30)==27)
        {
            return 0;
        }
    }
}
