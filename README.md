# jsondatamanipulation
The main goal of this project is to manipulate a json based on certain requirements

<h1>Project description</h1>
<p>In the <strong>source_file.json</strong> file there is a few projects. Each projects has it's managers, watchers and the priority of the
project itself. The main objective was to generate a json file with the name of the manager and the projects from which it is responsible
for it, ordered by project priority. The same it had to be done with the watchers. The results was generated in the <strong>managers.json</strong> file and the <strong>watchers.json</strong> file</p>

<h3>Observation</h3>
<p>The code in <strong>dataOrganizer.py</strong> and <strong>dataProjManagementWatcher.py</strong> files, which are responsible for
generate the resulted json, is not very well optimized. I will modularize and work on it in a later moment.</p>
