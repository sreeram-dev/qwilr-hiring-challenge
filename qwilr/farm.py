
class Farm:
  def __init__(self):
    self.crops = []

  def add(self, crop):
    """ Add a crop onto the farm """
    self.crops.append(crop)
    return True

  def get_counts(self):
    """ Get the counts per crop in the farm """
    counts = []
    for crop in self.crops:
      counts.append({
        'cropName': crop.name,
        'amount': crop.amount,
      })
    return counts

  def get_total_count(self):
    """ Get the total count of crops in the farm """
    total = 0

    curr = 1
    while curr < len(self.crops):
      total += self.crops[curr].amount
      curr += 1

    return total