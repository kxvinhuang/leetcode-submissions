-- Write your PostgreSQL query statement below
SELECT
    s.student_id
    ,s.student_name
    ,SU.subject_name,
    COUNT(e.student_id) as attended_exams
FROM Students s
CROSS JOIN Subjects su -- make a table where every student has every subject
LEFT JOIN Examinations e -- left join so rows without an exam are preserved (e.student_id is null)
ON e.student_id = s.student_id
AND e.subject_name = su.subject_name
GROUP BY s.student_id, s.student_name, su.subject_name
ORDER BY student_id
