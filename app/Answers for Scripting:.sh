Answers for Scripting:
Exercise #1 
#!/bin/bash
read USERSTR
echo "Hello, $USERSTR"
OR
#!/bin/bash
read NAME
echo "Hello, $NAME!"

Exercise #2
#!/bin/bash
/*calling find forward slash(search everywhere get all messages and the ones I can't find do the trash
get all the matches and wc counts the lines that match the line)*/

MATCHES=$( find / -name $1 2>/dev/null)
echo "Found $(echo "$MATCHES" | wc -l) matches"
echo "$MATCHES"

Exercise #3
1. check script file is the correct problematic script
2. Assign error var to script file and send any errors and standard output from that script to somefile.txt

if [[ $1 != *.sh ]]
then
    echo "Error. Please pass in a script file."
else
    ERROR=$($1 2>&1 > somefile.txt)
    COUNT=0
    while [ $? -eq 0 ]
    do
        COUNT=$((COUNT+1))
        ERROR=$($1 2>&1 > somefile.txt)
    done

***OR***

#!/bin/bash
continue=1
loopcount=0
while [[ $continue == 1 ]]; do
        $1 > /tmp/debugstdout 2> /tmp/debugstderr
        if [[ $? != 0 ]]; then
                continue=0
        fi
        loopcount=$(($loopcount+1))
done
echo "It took $loopcount runs to fail."
echo "Standard Output:"
cat /tmp/debugstdout
echo "Standard Error:"
cat /tmp/debugstderr

Exercise #4
curl -s https://www.cryptingup.com/api/markets | jq -r '.markets | sort_by(.volume_24h) | reverse | .[] | "\(.symbol) \(.price)"' | head -10

**OR***

curl https://cryptingup.com/api/markets | jq -r  '.markets[] | [.symbol, .price] | sort_by(10) | join(" ")' |  tail -n 10

 
Exercise #5 


from datetime import datetime

startTimeString = input("Start time: ")
startTime = datetime.strptime(startTimeString, "%Y-%m-%d %H:%M:%S")
endTimeString = input("End time: ")
endTime = datetime.strptime(endTimeString, "%Y-%m-%d %H:%M:%S")

f = open("apache_access", "r")

for line in f:
	currentTime = datetime.strptime(line.split()[3], "[%d/%b/%Y:%H:%M:%S")
	if currentTime >= startTime and currentTime <= endTime:
		print(line, end="")


f.close()




    <script>
		const form = document.getElementById("form");
		form.addEventListener("submit", function (e) {
			// Prevent default behavior:
			e.preventDefault();
			// Create payload as new FormData object:
			const payload = new FormData(form);
			// Post the payload using Fetch:
			fetch("http://localhost:5000/api/timeline_post", {
				method: "POST",
				body: payload,
				mode: 'cors',
				headers: {
					"Access-Control-Allow-Origin": "*",
				},
			})
				.then((res) => res.json())
				.then((data) => console.log(data))
				.finally(() => location.reload());

		});
	</script>