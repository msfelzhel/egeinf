f = open('ME9qo8qZq.txt').readline()
print(
    f.count('BOSS') - f.count('JBOSS') - f.count('BOSSJ') + f.count('JBOSSJ')
)