class Doctor:
  def __init__(self,doctorId, doctorName, specialization, consultationFee):
    self.doctorId = doctorId
    self.doctorName = doctorName
    self.specialization = specialization
    self.consultationFee = consultationFee

class Hospital:
  def searchByDoctorName(self, doctorName, doctorDB):
    for i in doctorDB.values():
      if i.doctorName == doctorName:
        print(i.doctorId)
        print(i.doctorName)
        print(i.specialization)
        print(i.consultationFee)
      
    print('No Doctor Exists with the given DoctorName')

  def calculateConsultationFeeBySpecialization(self, specialization, doctorDB):
    totalfee = 0
    for i in doctorDB.values():
      if i.specialization == specialization:
        totalfee += i.consultationFee
    if totalfee == 0:
      print('No Doctor with the given specialization')
    else:
      print(totalfee)


if __name__ == '__main__':
  run = int(input())
  doctorDB = dict()
  for i in range(run):
    doctorId = int(input())
    doctorName = input()
    specialization = input()
    consultationFee = int(input())
    doctorDB[i+1] = Doctor(doctorId, doctorName, specialization, consultationFee)

  h = Hospital()
  doctorName = input()
  specialization = input()
  h.searchByDoctorName(doctorName, doctorDB)
  h.calculateConsultationFeeBySpecialization(specialization, doctorDB)
