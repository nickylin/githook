## Git Hook - Log Check 

we hope that the commit log is useful and standard dand, so we need check
any commit log before some push code to gitlab, so we create 'log check'


### Function

+ you can define which kind of branch need to enable this check
just config this in pre-push file

```
# log config here
PRCTECT_BRANCH_DEVELOP = 'develop'
PRCTECT_BRANCH_MASTER = 'master'
...and more here
```

+ you can config which temple you like to use for standard nd log

```
FEATURE: some feature dic
REVIEWER: xxxname
REVIEWURL:https://xxx.com/code/id
```
if we found that you commit lack of some key tag, it will block this push

```
➜  LogCheck git:(develop) git push
Your branch which to push is <develop>, need to check
You have 1 commits ahead of origin
-----------------------------------------------------------
| Error Info: commitId: abcd88d
| commit log lack of key tag: REVIEWER
| This project have enable Log Check function
| Your commit is not pass the Log Check step
| Plz check the Log Check temple:
| FEATURE/OPTIMIZE/BUGFIX/NONCODE: xxx
| REVIEWER: xxx
| REVIEWURL: https://your—review-url.com/code/id
| if you have any question of that, plz contact nicky
-----------------------------------------------------------
error: failed to push some refs to 'git@gitlab.xxx/githook.git'

```
for example:

some one commit log is 

```
FEATURE: xxx

```

it will fail, cause it lack of REVIEWER & REVIEWURL
so the hook will be block this push and remind you

+ calculate how many commits of this push, you must make sure each commit log is 
correct, otherwise, you can't push success. we also e will remind you need to combine 
the multi commits to just one, so that the log list line will be more useful and beautiful 


### How to use

git hook have many event in its lifecycle, so we choose the pre-push event

```
pre-push
post-push
pre-xxx
pre-commit
..
```

1. put this folder(githook) to your workspace
   you can put it in your root dir with some workspace
   
2. if your project is AS, you can config this to your build.gradle, this is example.
you can put this everywhere, 
but this py file must execure before you pust
that mean you must execute the ./githook/githook.py

```
python {your-workspace-path}/githook/githook.py
```
.
3. after that, it will cp the pre-push file to .git/hooks/pre-push
git will be execute this hook file before it push, in that time ,we can block it and 
have time to do our checking.

### file list:
**githook.py**: use for mkdir some dir and cp the pre-push file to dst dir 
**pre-push**: the biz script file and config your temple here



