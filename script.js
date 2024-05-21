function showStudentForm() {
    document.getElementById('studentFields').classList.remove('hidden');
    document.getElementById('teacherFields').classList.add('hidden');
}

function showTeacherForm() {
    document.getElementById('teacherFields').classList.remove('hidden');
    document.getElementById('studentFields').classList.add('hidden');
}
