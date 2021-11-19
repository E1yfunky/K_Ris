select Flight_number, Flight_Date, SUM(Bonus_miles) as Bonus
from b_miles.ticket join b_miles.scale on Minimum<=Cost and Cost<=Maximum
group by Flight_number, Flight_Date