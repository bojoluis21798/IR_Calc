from math import sin, radians, sqrt

GS = 100

def toDegrees(degrees): 
  return (degrees + 360) % 360

def getVectorDetails(
  currentDme, 
  currentRadial, 
  radialToIntercept, 
  interceptionAngle, 
  direction
):
  if direction == "left":
    interceptionHeading = abs(toDegrees(radialToIntercept - interceptionAngle))
  else:
    interceptionHeading = abs(toDegrees(radialToIntercept + interceptionAngle))

  print("\nInterception Angle:", interceptionAngle)
  print("\nInterception Heading: ", interceptionHeading)

  radialDiff = abs(currentRadial - radialToIntercept)
  turnAngle = 180 - radialDiff - interceptionAngle

  sinCurrentPos = currentDme / sin(radians(interceptionAngle));

  print("Distance Traveled: ", sin(radians(radialDiff)) * sinCurrentPos)
  print("Distance to station: ", sin(radians(turnAngle)) * sinCurrentPos)
  print("Angles:", radialDiff, turnAngle, interceptionAngle)

  print("==========\n")

def pythaA(h, b):
  return sqrt(h**2 - b**2)

def sohO(angle, h):
  return sin(radians(angle)) * h

getVectorDetails(8.1, 350 - 90, 350, 30, "right")
getVectorDetails(8.1, 350 - 90, 350, 45, "right")
getVectorDetails(8.1, 350 - 90, 350, 60, "right")