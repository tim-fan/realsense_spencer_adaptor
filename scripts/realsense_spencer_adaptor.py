#!/usr/bin/env python

#realsense_spencer_adaptor.py
# node for connecting realsence d435i output to spencer tracking package

import rospy
import cv_bridge
import cv2
from sensor_msgs.msg import Image

def convertDepthEncoding(imageMsg, bridge):
    """
    convert given image from 16UC1 in mm to 32FC1 m
    using given cv bridge
    Refer https://github.com/spencer-project/spencer_people_tracking/issues/4
    """
    #convert from 16UC1 in mm to 32FC1 m
    cvImg = bridge.imgmsg_to_cv2(imageMsg)
    cvImg32F = cvImg.astype('float32') / 1000.0
    convertedImageMsg = bridge.cv2_to_imgmsg(cvImg32F)
    convertedImageMsg.header = imageMsg.header
    return convertedImageMsg

def convertMonoEncoding(imageMsg):
    """
    Resolves the error: "cv_bridge exception: [8UC1] is not a color format. but [bgr8] is."
    which arises when processing mono images from realsense using opencv.
    Note this is not required for using spencer tracking
    """
    imageMsg.encoding = "mono8"
    return imageMsg


def runAdaptor():
    rospy.init_node('realsense_spencer_adaptor')
    bridge = cv_bridge.CvBridge()
    
    pubDepth = rospy.Publisher('depth/image_rect', Image, queue_size=10)
    callbackDepth = lambda imgMsg : pubDepth.publish(convertDepthEncoding(imgMsg, bridge))
    subDepth = rospy.Subscriber('depth/image_rect_raw', Image, callbackDepth)

    pubInfra = rospy.Publisher('infra1/image_rect_raw_mono', Image, queue_size=10)
    callbackInfra = lambda imgMsg : pubInfra.publish(convertMonoEncoding(imgMsg))
    subInfra = rospy.Subscriber('infra1/image_rect_raw', Image, callbackInfra)

    rospy.spin()

if __name__ == '__main__':
    runAdaptor()
